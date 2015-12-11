# -*- coding: utf-8 -*-

import hashlib
import json
import time
import urllib

import requests
from requests import RequestException, ConnectionError, Timeout
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

from .api import ApiSpec
from .exceptions import ElongException, ElongAPIError, \
    RetryableException, RetryableAPIError
from .response import RequestsResponse, TornadoResponse, logger
from .util.retry import retry_on_error, is_retryable


class Request(object):
    def __init__(self, client,
                 host=ApiSpec.host,
                 version=ApiSpec.version,
                 local=ApiSpec.local):
        self.client = client
        self.verify_ssl = self.client.cert is not None

        self.host = host
        self.version = version
        self.local = local

    def do(self, api, params, https, raw=False):
        raise NotImplementedError()

    def prepare(self, api, params, https, raw):
        timestamp = str(int(time.time()))
        data = self.build_data(params, raw)
        scheme = 'https' if https else 'http'
        url = "%s://%s" % (scheme, self.host)
        params = {
            'method': api,
            'user': self.client.user,
            'timestamp': timestamp,
            'data': data,
            'signature': self.signature(data, timestamp),
            'format': 'json'
        }
        return url, params

    def build_data(self, params, raw=False):
        if not raw:
            data = {
                'Version': self.version,
                'Local': self.local,
                'Request': params
            }
        else:
            data = params
        return json.dumps(data, separators=(',', ':'))

    def signature(self, data, timestamp):
        s = self._md5(data + self.client.app_key)
        return self._md5("%s%s%s" % (timestamp, s, self.client.secret_key))

    @staticmethod
    def _md5(data):
        return hashlib.md5(data.encode('utf-8')).hexdigest()

    def check_response(self, resp):
        if not resp.ok and self.client.raise_api_error:
            logger.error('pyelong calling api failed, url: %s', resp.url)
            if is_retryable(resp.code):
                raise RetryableAPIError(resp.code, resp.error)
            raise ElongAPIError(resp.code, resp.error)
        return resp

    def timing(self, api, delta):
        if self.client.statsd_client and \
                hasattr(self.client.statsd_client, 'timing'):
            self.client.statsd_client.timing(api, delta)


class SyncRequest(Request):
    @property
    def session(self):
        if not hasattr(self, '_session') or not self._session:
            self._session = requests.Session()
            if self.client.proxy_host and self.client.proxy_port:
                p = '%s:%s' % (self.client.proxy_host, self.client.proxy_port)
                self._session.proxies = {'http': p, 'https': p}
        return self._session

    @retry_on_error(retry_api_error=True, logger=logger)
    def do(self, api, params, https, raw=False):
        url, params = self.prepare(api, params, https, raw)
        try:
            result = self.session.get(url=url,
                                      params=params,
                                      verify=self.verify_ssl,
                                      cert=self.client.cert)
        except (ConnectionError, Timeout) as e:
            logger.exception('pyelong catches ConnectionError or Timeout, '
                             'url: %s, params: %s', url, params)
            raise RetryableException('ConnectionError or Timeout: %s' % e)
        except RequestException as e:
            logger.exception('pyelong catches RequestException, url: %s,'
                             ' params: %s', url, params)
            raise ElongException('RequestException: %s' % e)
        except Exception as e:
            logger.exception('pyelong catches unknown exception, url: %s, '
                             'params: %s', url, params)
            raise ElongException('unknown exception: %s' % e)

        resp = RequestsResponse(result)
        self.timing(api, resp.request_time)
        return self.check_response(resp)


class AsyncRequest(Request):
    @property
    def proxy_config(self):
        if not getattr(self, '_proxy_config', None):
            if self.client.proxy_host and self.client.proxy_port:
                self._proxy_config = {
                    'proxy_host': self.client.proxy_host,
                    'proxy_port': self.client.proxy_port
                }
            else:
                self._proxy_config = {}
        return self._proxy_config

    @staticmethod
    def _encode_params(data):
        """
        :param dict data: params

        Taken from requests.models.RequestEncodingMixin._encode_params
        """
        result = []
        for k, vs in data.iteritems():
            if isinstance(vs, basestring) or not hasattr(vs, '__iter__'):
                vs = [vs]
            for v in vs:
                if v is not None:
                    result.append(
                        (k.encode('utf-8') if isinstance(k, str) else k,
                         v.encode('utf-8') if isinstance(v, str) else v))
        return urllib.urlencode(result, doseq=True)

    def _prepare_url(self, url, params):
        if url.endswith('/'):
            url = url.strip('/')
        return '%s?%s' % (url, self._encode_params(params))

    @gen.coroutine
    def do(self, api, params, https, raw=False):
        url, params = self.prepare(api, params, https, raw)
        # use the default SimpleAsyncHTTPClient
        resp = yield AsyncHTTPClient().fetch(self._prepare_url(url, params),
                                             validate_cert=self.verify_ssl,
                                             ca_certs=self.client.cert,
                                             **self.proxy_config)
        resp = TornadoResponse(resp)
        self.timing(api, resp.request_time)
        raise gen.Return(self.check_response(resp))
