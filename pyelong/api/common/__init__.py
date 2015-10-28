# -*- coding: utf-8 -*-

from ..base import ApiBase
from .creditcard import CreditCard

__all__ = 'Common'


class Common(ApiBase):
    _category = ''

    def exchangerate(self, **kwargs):
        """获取外币对应人民币的汇率，方法名：common.exchangerate

        文档
        ~~~~
            - http://open.elong.com/wiki/Common.exchangerate
        """
        return self._request('exchangerate', **kwargs)

    @property
    def creditcard(self):
        return CreditCard(self._client)
