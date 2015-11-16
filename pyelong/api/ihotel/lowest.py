# -*- coding: utf-8 -*-

__author__ = 'leon'

from ..base import ApiBase


class Lowest(ApiBase):
    _category = 'ihotel'

    def price(self, **kwargs):
        """国际酒店最低价列表

        文档
        ~~~~
            - http://open.elong.com/wiki/Ihotel.lowest.price

        NOTE:
        ~~~~
            - 获取API中缓存的酒店的最低价
        """

        return self._request('price', raw=True, **kwargs)
