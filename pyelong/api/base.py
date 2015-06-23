# -*- coding: utf-8 -*-

class ApiBase(object):
    _category = ''

    def __init__(self, client):
        self._client = client

    def _request(self, method, https=False, raw=False, **kwargs):
        api = self._build_api(method)
        return self._client.request.do(api, kwargs, https, raw)

    def _build_api(self, method):
        class_name = self.__class__.__name__
        api = '.'.join([self._category, class_name, method]).lower()
        return api.strip('.')
