# -*- coding: utf-8 -*-

import hashlib
import json
import logging
import time
import urllib

import requests
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

from pyelong.api import ApiSpec
from pyelong.response import RequestsResponse, TornadoResponse

_logger = logging.getLogger(__name__)


class Request(object):
    def __init__(self, user, app_key, secret_key,
                 host=ApiSpec.host,
                 version=ApiSpec.version,
                 local=ApiSpec.local):
        self.user = user
        self.app_key = app_key
        self.secret_key = secret_key

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
            'user': self.user,
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
        s = self._md5(data + self.app_key)
        return self._md5("%s%s%s" % (timestamp, s, self.secret_key))

    @staticmethod
    def _md5(data):
        return hashlib.md5(data.encode('utf-8')).hexdigest()

    @staticmethod
    def _log_resp(resp):
        _logger.debug('request: %s', resp.url)
        _logger.debug('response: %s', resp)
        _logger.debug('elapsed: %s', resp.request_time)


class SyncRequest(Request):
    @property
    def session(self):
        if not hasattr(self, '_session') or not self._session:
            self._session = requests.Session()
        return self._session

    def do(self, api, params, https, raw=False):
        url, params = self.prepare(api, params, https, raw)
        resp = RequestsResponse(self.session.get(url, params=params))
        self._log_resp(resp)
        return resp


class AsyncRequest(Request):
    @staticmethod
    def _encode_params(data):
        """
        :param data: type of dict

        token from requests.models.RequestEncodingMixin._encode_params
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
        resp = yield AsyncHTTPClient().fetch(self._prepare_url(url, params))
        resp = TornadoResponse(resp)
        self._log_resp(resp)
        raise gen.Return(resp)
