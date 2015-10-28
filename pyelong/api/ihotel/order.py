# -*- coding: utf-8 -*-

from ..base import ApiBase


class Order(ApiBase):
    _category = 'ihotel'

    def list(self, **kwargs):
        """订单列表，方法名称：ihotel.order.list，必须使用 https

        http://open.elong.com/wiki/Ihotel.order.list
        """
        return self._request('list', https=True, raw=True, **kwargs)

    def create(self, **kwargs):
        """ 创建订单，方法名称：ihotel.order.create，必须使用 https

        http://open.elong.com/wiki/Ihotel.order.create
        """
        return self._request('create', https=True, raw=True, **kwargs)

    def detail(self, **kwargs):
        """订单详情，方法名称：ihotel.order.detail，必须使用 https

        http://open.elong.com/wiki/Ihotel.order.detail
        """
        return self._request('detail', https=True, raw=True, **kwargs)

    def canceltips(self, **kwargs):
        """订单取消提示，方法名称：ihotel.order.canceltips，必须使用 https

        http://open.elong.com/wiki/Ihotel.order.canceltips
        """
        return self._request('canceltips', https=True, raw=True, **kwargs)

    def cancel(self, **kwargs):
        """订单取消，方法名称：ihotel.order.cancel，必须使用 https

        http://open.elong.com/wiki/Ihotel.order.cancel
        """
        return self._request('cancel', https=True, raw=True, **kwargs)
