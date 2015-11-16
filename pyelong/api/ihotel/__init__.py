# -*- coding: utf-8 -*-

from ..base import ApiBase
from .order import Order
from .detail import Detail
from .lowest import Lowest

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
    def lowest(self):
        return Lowest(self._client)

    @property
    def detail(self):
        return Detail(self._client)

    @property
    def order(self):
        return Order(self._client)
