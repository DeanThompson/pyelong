# -*- coding: utf-8 -*-

from ..base import ApiBase
from .order import Order
from .data import Data
from .incr import Incr

__all__ = 'Hotel'


class Hotel(ApiBase):
    _category = ''

    def list(self, **kwargs):
        """酒店列表搜索，方法名：hotel.list

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.list
        """
        return self._request('list', **kwargs)

    def detail(self, **kwargs):
        """酒店详情搜索，方法名：hotel.detail

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.detail
        """
        return self._request('detail', **kwargs)

    @property
    def order(self):
        return Order(self._client)

    @property
    def data(self):
        return Data(self._client)

    @property
    def incr(self):
        return Incr(self._client)

    @property
    def id(self):
        return ID(self._client)

    @property
    def inv(self):
        return Inv(self._client)


class ID(ApiBase):
    _category = 'hotel'

    def list(self, **kwargs):
        """酒店Id列表搜索，方法名： hotel.id.list

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.id.list
        """
        return self._request('list', **kwargs)


class Inv(ApiBase):
    _category = 'hotel'

    def validate(self, **kwargs):
        """库存验证，方法名：hotel.inv.validate

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.inv.validate
        """
        return self._request('validate', **kwargs)
