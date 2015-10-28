# -*- coding: utf-8 -*-

from ..base import ApiBase


class Incr(ApiBase):
    _category = 'hotel'

    def id(self, **kwargs):
        """增量编号，方法名：hotel.incr.id

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.incr.id

        NOTE
        ~~~~
            - 本接口属于高级功能接口，通常开发使用不到，不建议使用。可以考虑使用订单增量。
        """
        return self._request('id', **kwargs)

    def data(self, **kwargs):
        """数据变化增量，方法名：hotel.incr.data

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.incr.data

        NOTE
        ~~~~
            - 本接口属于高级功能接口，通常开发使用不到，不建议使用。
            - 本接口不能获取直连酒店(目前是万豪集团的酒店)的数据的变化；其报价请使用hotel.detail接口。
        """
        return self._request('data', **kwargs)

    def inv(self, **kwargs):
        """库存增量，方法名：hotel.incr.inv

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.incr.inv

        NOTE
        ~~~~
            - 本接口属于高级功能接口，通常开发使用不到，不建议使用。
            - 本接口不能获取直连酒店(目前是万豪集团的酒店)的数据的变化；其报价请使用hotel.detail接口。
        """
        return self._request('inv', **kwargs)

    def rate(self, **kwargs):
        """价格增量，方法名：hotel.incr.rate

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.incr.rate

        NOTE
        ~~~~
            - 本接口属于高级功能接口，通常开发使用不到，不建议使用。
            - 本接口不能获取直连酒店(目前是万豪集团的酒店)的数据的变化；其报价请使用hotel.detail接口。
        """
        return self._request('rate', **kwargs)

    def order(self, **kwargs):
        """订单增量，方法名：hotel.incr.order，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.incr.order
        """
        return self._request('order', https=True, **kwargs)

    def state(self, **kwargs):
        """状态增量，方法名：hotel.incr.state

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.incr.state
        """
        return self._request('state', **kwargs)
