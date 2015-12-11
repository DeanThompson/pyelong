# -*- coding: utf-8 -*-

import time

from .request import SyncRequest, AsyncRequest
from .api.hotel import Hotel
from .api.ihotel import Ihotel
from .api.common import Common
from .util import des_encrypt, retry


class Client(object):
    def __init__(self, user, app_key, secret_key,
                 use_tornado=False, cert=None, statsd_client=None,
                 raise_api_error=True, codes_could_retry=None,
                 proxy_host=None, proxy_port=None, **kwargs):
        """ 初始化一个客户端对象
        :param str user: API 账号，需要在艺龙注册后得到
        :param str app_key: API 调用的身份标识，需要在艺龙注册后得到
        :param str secret_key: API 调用的密钥，用于签名，需要在艺龙注册后得到
        :param bool use_tornado: 默认使用 requests，如果为 True 使用 AsyncHTTPClient
        :param str cert: SSL 证书文件路径，如果不为 None，则会检查服务器的证书
        :param statsd_client: StatsD 客户端对象，如果不为 None，将会发送 API 调用统计
        :param raise_api_error: 如果为 True，API 调用失败时将抛出异常
        :param codes_could_retry: 可以重试的错误码，会覆盖程序默认的错误码，是一个 set
        :param proxy_host: 代理服务器 host
        :param proxy_port: 代理服务器 port
        :param kwargs: 可选参数：
                    - host: 指定 API 的 host，默认是：api.elong.com/rest
                    - version: 指定 API 版本
                    - local: 指定语言，默认是 zh_CN
        """
        self.user = user
        self.app_key = app_key
        self.secret_key = secret_key
        self.cert = cert
        self.statsd_client = statsd_client
        self.raise_api_error = raise_api_error
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port

        if codes_could_retry:
            retry._codes_could_retry = set(codes_could_retry)

        request_class = AsyncRequest if use_tornado else SyncRequest
        self.request = request_class(self, **kwargs)

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
