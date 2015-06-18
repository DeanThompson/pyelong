# -*- coding: utf-8 -*-

from pyelong.api.base import ApiBase
from pyelong.api.hotel.order import Order

__all__ = 'Hotel'


class Hotel(ApiBase):
    _category = ''

    def list(self, **kwargs):
        """
        酒店列表搜索，方法名：hotel.list
        http://open.elong.com/wiki/Hotel.list
        """
        return self._request('list', kwargs)

    def detail(self, **kwargs):
        """
        酒店详情搜索，方法名：hotel.detail
        http://open.elong.com/wiki/Hotel.detail
        """
        return self._request('detail', kwargs)

    @property
    def order(self):
        return Order(self._client)
