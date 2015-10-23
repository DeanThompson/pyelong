# -*- coding: utf-8 -*-

__author__ = 'leon'

import time
import logging

from pyelong.exceptions import ElongAPIError


class retry_on_error(object):
    _codes_could_retry = {
        'I-0004',  # inner system exception
        'I-0005',  # unknown system exception

        # http://open.elong.com/wiki/%E5%B9%B3%E5%8F%B0%E9%94%99%E8%AF%AF%E7%A0%81
        'A105020003',  # 虚拟卡获取超时
        'A105020005',  # 获取虚拟卡系统错误
        'A103010101',  # 系统错误-国际酒店接口连接失败
        'A203010301',  # 超时重试
        'A103010303',  # 酒店系统错误
        'A203010201',  # 超时重试
        'A101010014',  # 系统错误：Redis连接失败
        'A204010001',  # 超时或系统错误，重试失败请联系艺龙
        'A204010002',  # 加载文件成功，请重试
        'A103050101',  # 系统错误-礼品卡接口 common.giftcard 连接失败
        'A103010401',  # 系统错误-接口连接失败

        # http://open.elong.com/wiki/%E5%9B%BD%E5%86%85%E9%85%92%E5%BA%97%E9%94%99%E8%AF%AF%E7%A0%81
        'H099999999',  # 未知错误
        'H100999',  # 系统异常
        'H101093',  # 底层提交订单保存异常,请重试
    }

    def __init__(self, max_retries=5, delay=0.1, backoff=2,
                 retry_api_error=True, logger=None):
        self.max_retries = max_retries
        self.delay = delay
        self.backoff = backoff
        self.retry_api_error = retry_api_error

        if logger is None:
            logger = logging.getLogger(__name__)
        self.logger = logger

    def is_server_error(self, resp):
        return 500 <= resp.status_code <= 599

    def __call__(self, func):
        def decorator(*args, **kwargs):
            delay = self.delay
            tries = 0
            while 1:
                try:
                    resp = func(*args, **kwargs)
                except ElongAPIError as e:
                    if not self.retry_api_error:
                        raise
                    resp = e.resp
                    if resp.code not in self._codes_could_retry:
                        raise
                if not self.is_server_error(resp) or tries >= self.max_retries:
                    return resp
                self.logger.warn('retry [%d], delay: %s ms', tries,
                                 delay * 1000)
                tries += 1
                time.sleep(delay)
                delay *= self.backoff

        return decorator
