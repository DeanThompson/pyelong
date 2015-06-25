# -*- coding: utf-8 -*-

class Response(object):
    def __init__(self, resp):
        """ 初始化 Response 对象
        :param resp: requests.models.Response 类型
        """
        #: HTTP 响应状态码
        self.status_code = resp.status_code

        #: HTTP 响应头
        self.headers = resp.headers

        #: 请求的 URL 地址
        self.url = resp.url

        #: 请求耗时
        self.elapsed = resp.elapsed

        if self.status_code == 200:
            #: HTTP 请求成功完成，从响应解析出 code 和 result
            #: 详情见：http://open.elong.com/wiki/%E5%B9%B3%E5%8F%B0%E5%8D%8F%E8%AE%AE
            _content = resp.json()

            #: Elong API 请求返回的结果代码
            #: 0 表示成功完成了请求；有些请求逻辑是否成功需要继续判断 Result
            self.code = _content['Code']

            if '|' in self.code:
                self.code, self.error = self.code.split('|', 1)
            else:
                self.error = ''

            #: Elong API 请求返回的结果数据对象
            self.result = _content.get('Result', None)
        else:
            # 请求出现异常
            self.code = self.status_code
            self.reason = resp.reason
            self.result = None

    @property
    def __dict__(self):
        return {
            'url': self.url,
            'status_code': self.status_code,
            'headers': self.headers,
            'code': self.code,
            'error': self.error,
            'result': self.result
        }

    def __str__(self):
        return '%s %s %s' % (self.code, self.error, self.result)
