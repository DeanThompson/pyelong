# -*- coding: utf-8 -*-

import tornado.escape


class Response(object):
    def __init__(self, resp, content_getter):
        if not callable(content_getter):
            raise ValueError('content_getter must be callable')
        self._resp = resp
        self._content_getter = content_getter
        self.parse_content()

    def parse_content(self):
        """
        详情见：http://open.elong.com/wiki/%E5%B9%B3%E5%8F%B0%E5%8D%8F%E8%AE%AE
        """
        if self.ok:
            #: Elong API 请求返回的结果代码
            #: 0 表示成功完成了请求；有些请求逻辑是否成功需要继续判断 Result
            content = self._content_getter(self._resp)
            self.code = content['Code']

            if '|' in self.code:
                self.code, self.error = self.code.split('|', 1)
            else:
                self.error = ''

            #: Elong API 请求返回的结果数据对象
            self.result = content.get('Result', None)
        else:
            # 请求出现异常
            self.code = str(self.status_code)
            self.reason = self._resp.reason
            self.result = None

    @property
    def ok(self):
        return True

    @property
    def url(self):
        return None

    @property
    def status_code(self):
        return 200

    @property
    def headers(self):
        return self._resp.headers

    @property
    def request_time(self):
        """
        :return: milliseconds from request start to finish
        """
        return 0

    def to_json(self):
        return {
            'url': self.url,
            'status_code': self.status_code,
            'request_time': self.request_time,
            'code': self.code,
            'error': self.error,
            'result': self.result
        }

    def __str__(self):
        return '%s %s %s' % (self.code, self.error, self.result)


class RequestsResponse(Response):
    def __init__(self, resp):
        super(RequestsResponse, self).__init__(resp, lambda x: x.json())

    @property
    def ok(self):
        return self._resp.status_code == 200

    @property
    def url(self):
        return self._resp.url

    @property
    def status_code(self):
        return self._resp.status_code

    @property
    def request_time(self):
        """
        :return: milliseconds from request start to finish
        """
        return int(self._resp.elapsed.total_seconds() * 1000)


class TornadoResponse(Response):
    def __init__(self, resp):
        content_getter = lambda x: tornado.escape.json_decode(x.body)
        super(TornadoResponse, self).__init__(resp, content_getter)

    @property
    def ok(self):
        return self._resp.error is None

    @property
    def url(self):
        return self._resp.effective_url

    @property
    def status_code(self):
        return self._resp.code

    @property
    def request_time(self):
        """
        :return: milliseconds from request start to finish
        """
        return int(self._resp.request_time * 1000)
