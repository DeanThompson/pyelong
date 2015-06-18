# -*- coding: utf-8 -*-

import time
import hashlib
import json

import requests

from pyelong.api import ApiSpec
from pyelong.response import Response


class Request(object):
    def __init__(self, user, app_key, secret_key, host=ApiSpec.host,
                 version=ApiSpec.version, local=ApiSpec.local):
        self.user = user
        self.app_key = app_key
        self.secret_key = secret_key

        self.host = host
        self.version = version
        self.local = local

    def do(self, api, params, https):
        self.timestamp = str(int(time.time()))
        self.data = self.build_data(params)
        scheme = 'https' if https else 'http'
        url = "%s://%s" % (scheme, self.host)
        return Response(requests.get(url, params=self.build_params(api)))

    def build_params(self, api):
        return {
            'method': api,
            'user': self.user,
            'timestamp': self.timestamp,
            'data': self.data,
            'signature': self.signature(),
            'format': 'json'  # 只支持 JSON
        }

    def build_data(self, params):
        return json.dumps({
            'Version': self.version,
            'Local': self.local,
            'Request': params
        })

    def signature(self):
        s = self._md5(self.data + self.app_key)
        return self._md5("%s%s%s" % (self.timestamp, s, self.secret_key))

    def _md5(self, data):
        return hashlib.md5(data).hexdigest()
