# -*- coding: utf-8 -*-

from pyelong.api.base import ApiBase
from pyelong.api.ihotel.order import Order

__all__ = ('Ihotel')


class Ihotel(ApiBase):
    _category = ''

    def list(self, **kwargs):
        """
        国际酒店列表，方法名：ihotel.list
        http://open.elong.com/wiki/Ihotel.list
        """
        return self._request('list', raw=True, **kwargs)

    def detail(self, **kwargs):
        """
        国际酒店详情，方法名：ihotel.detail
        http://open.elong.com/wiki/Ihotel.detail
        """
        return self._request('detail', raw=True, **kwargs)

    @property
    def order(self):
        return Order(self._client)
