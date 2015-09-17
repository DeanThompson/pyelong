# -*- coding: utf-8 -*-

__author__ = 'leon'

import time
import logging


class Retry(object):
    def __init__(self, max_retries=5, delay=0.1, backoff=2, logger=None):
        self.max_retries = max_retries
        self.delay = delay
        self.backoff = backoff

        if logger is None:
            logger = logging.getLogger(__name__)
        self.logger = logger

    def should_retry(self, resp):
        return resp.status_code == 500

    def __call__(self, func):
        def decorator(*args, **kwargs):
            delay = self.delay
            tries = 0
            while True:
                resp = func(*args, **kwargs)
                if not self.should_retry(resp) or tries >= self.max_retries:
                    return resp
                self.logger.warn('retry [%d], delay: %s ms', tries,
                                 delay * 1000)
                tries += 1
                time.sleep(delay)
                delay *= self.backoff

        return decorator


class _ServerErrorMixin(object):
    def is_server_error(self, status_code):
        return 500 <= status_code <= 599


class _APIErrorMixin(object):
    codes_could_retry = {
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

    def api_error_could_retry(self, code):
        return code in self.codes_could_retry


class retry_on_server_error(_ServerErrorMixin, Retry):
    def should_retry(self, resp):
        return self.is_server_error(resp.status_code)


class retry_on_api_error(_APIErrorMixin, Retry):
    def should_retry(self, resp):
        return self.api_error_could_retry(resp.code)


class retry_on_error(_APIErrorMixin, _ServerErrorMixin, Retry):
    def should_retry(self, resp):
        is_server_error = self.is_server_error(resp.status_code)
        return is_server_error or self.api_error_could_retry(resp.code)
