# -*- coding: utf-8 -*-

import time

from pyelong.request import SyncRequest, AsyncRequest
from pyelong.api.hotel import Hotel
from pyelong.api.ihotel import Ihotel
from pyelong.api.common import Common
from pyelong.util import des_encrypt


class Client(object):
    def __init__(self, user, app_key, secret_key,
                 use_tornado=False, cert=None, **kwargs):
        """ 初始化一个客户端对象
        :param str user: API 账号，需要在艺龙注册后得到
        :param str app_key: API 调用的身份标识，需要在艺龙注册后得到
        :param str secret_key: API 调用的密钥，用于签名，需要在艺龙注册后得到
        :param bool use_tornado: 默认使用 requests，如果为 True 使用 AsyncHTTPClient
        :param str cert: SSL 证书文件路径，如果不为 None，则会检查服务器的证书
        :param kwargs: 可选参数：
                    - host: 指定 API 的 host，默认是：api.elong.com/rest
                    - version: 指定 API 版本
                    - local: 指定语言，默认是 zh_CN
        """
        request_class = AsyncRequest if use_tornado else SyncRequest
        self.request = request_class(user, app_key, secret_key, cert, **kwargs)

    @property
    def hotel(self):
        return Hotel(self)

    @property
    def ihotel(self):
        return Ihotel(self)

    @property
    def common(self):
        return Common(self)

    @property
    def _encrypt_key(self):
        return self.request.app_key[-8:]

    def encrypt_credit_card_fields(self, kvs, timestamp=None):
        """ 加密信用卡信息
        :param dict kvs: 字典类型的信用卡信息
        :param timestamp: 时间戳
        :return: 把 kvs 里的每个值加密后返回
        """
        if not timestamp:
            timestamp = str(int(time.time()))
        key = self._encrypt_key
        rv = {}
        for field, value in kvs.iteritems():
            data = '%s#%s' % (timestamp, value)
            rv[field] = des_encrypt(data=data, key=key, iv=key)
        return rv
