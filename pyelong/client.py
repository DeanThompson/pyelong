# -*- coding: utf-8 -*-

from pyelong.request import SyncRequest, AsyncRequest
from pyelong.api.hotel import Hotel
from pyelong.api.ihotel import Ihotel
from pyelong.api.common import Common


class Client(object):
    def __init__(self, user, app_key, secret_key, use_tornado=False, **kwargs):
        """ 初始化一个客户端对象
        :param user: API 账号，需要在艺龙注册后得到
        :param app_key: API 调用的身份标识，需要在艺龙注册后得到
        :param secret_key: API 调用的密钥，用于签名，需要在艺龙注册后得到
        :param use_tornado: 默认使用 requests，如果为 True 使用 AsyncHTTPClient
        :param kwargs: 可选参数：
                    - host: 指定 API 的 host，默认是：api.elong.com/rest
                    - version: 指定 API 版本
                    - local: 指定语言，默认是 zh_CN

        Usage::

            >>> from pyelong import Client
            >>> client = Client(user='', app_key='', secret_key='')
            >>> client.hotel.list()

            >>> from pyelong import Client
            >>> from tornado import gen
            >>> client = Client(user='', app_key='', secret_key='', use_tornado=True)
            >>> @gen.coroutine
            ... def get(self):
            ...     resp = yield client.hotel.list()
            ...     self.write(resp.to_json()))
        """
        request_class = AsyncRequest if use_tornado else SyncRequest
        self.request = request_class(user, app_key, secret_key, **kwargs)

    @property
    def hotel(self):
        return Hotel(self)

    @property
    def ihotel(self):
        return Ihotel(self)

    @property
    def common(self):
        return Common(self)
