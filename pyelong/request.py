# -*- coding: utf-8 -*-

import datetime
import time
import hashlib
import json

import requests

from pyelong.api import ApiSpec
from pyelong.response import Response


class Request(object):
    def __init__(self, user, app_key, secret_key,
                 host=ApiSpec.host,
                 version=ApiSpec.version,
                 local=ApiSpec.local,
                 debug=False):
        self.user = user
        self.app_key = app_key
        self.secret_key = secret_key

        self.host = host
        self.version = version
        self.local = local

        self.debug = debug

    def do(self, api, params, https, raw=False):
        self.timestamp = str(int(time.time()))
        self.data = self.build_data(params, raw)
        scheme = 'https' if https else 'http'
        url = "%s://%s" % (scheme, self.host)
        resp = Response(requests.get(url, params=self.build_params(api)))
        self._log('request:', resp.url)
        self._log("response:", resp)
        return resp

    def build_params(self, api):
        return {
            'method': api,
            'user': self.user,
            'timestamp': self.timestamp,
            'data': self.data,
            'signature': self.signature(),
            'format': 'json'  # 只支持 JSON
        }

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

    def signature(self):
        s = self._md5(self.data + self.app_key)
        return self._md5("%s%s%s" % (self.timestamp, s, self.secret_key))

    def _md5(self, data):
        return hashlib.md5(data).hexdigest()

    def _log(self, *args):
        if not self.debug:
            return
        prefix = '%s - pyelong -' % datetime.datetime.now()
        msg = '%s ' * len(args) % args
        print prefix, msg
