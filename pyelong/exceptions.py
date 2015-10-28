# -*- coding: utf-8 -*-

__author__ = 'leon'

from .util import utf8


class ElongException(Exception):
    """Base exception class used by :mod:`~pyelong`"""


class RetryableException(ElongException):
    """可以重试的异常，如网络连接错误等"""


class ElongAPIError(ElongException):
    """如果返回值的 `code` 不为 `0`，则 API 调用发生异常"""

    def __init__(self, code, message):
        self.code = utf8(code)
        self.message = utf8(message)

        super(ElongAPIError, self).__init__(message)

    def __str__(self):
        return '<ElongAPIError ("%s", "%s")>' % (self.code, self.message)


class RetryableAPIError(ElongAPIError):
    """可以重试的 API 错误"""
