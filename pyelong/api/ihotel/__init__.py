# -*- coding: utf-8 -*-

from pyelong.api.base import ApiBase
from pyelong.api.ihotel.order import Order
from pyelong.api.ihotel.detail import Detail

__all__ = 'Ihotel'


class Ihotel(ApiBase):
    _category = ''

    def list(self, **kwargs):
        """国际酒店列表，方法名：ihotel.list

        文档
        ~~~~
            - http://open.elong.com/wiki/Ihotel.list
        """
        return self._request('list', raw=True, **kwargs)

    @property
    def detail(self):
        return Detail(self._client)

    @property
    def order(self):
        return Order(self._client)
