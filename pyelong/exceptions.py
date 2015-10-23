# -*- coding: utf-8 -*-

__author__ = 'leon'


class ElongException(Exception):
    """Base exception class used by :mod:`~pyelong`"""


class ElongAPIError(ElongException):
    """如果返回值的 `code` 不为 `0`，则 API 调用发生异常"""

    def __init__(self, resp):
        self.resp = resp
        self._code = self.resp.code
        self._msg = self.resp.error

    def __str__(self):
        klass = self.__class__.__name__
        return '<%s ("%s", "%s")>' % (klass, self._code, self._msg)
