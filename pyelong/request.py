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
            'format': 'json'  # 只支持 json
        }
        resp = Response(requests.get(url, params=params))
        self._log('request:', resp.url)
        self._log("response:", resp)
        return resp

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

    def _md5(self, data):
        return hashlib.md5(data.encode('utf-8')).hexdigest()

    def _log(self, *args):
        if not self.debug:
            return
        prefix = '%s - pyelong -' % datetime.datetime.now()
        msg = '%s ' * len(args) % args
        print prefix, msg.encode('utf-8')
