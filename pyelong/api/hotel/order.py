# -*- coding: utf-8 -*-

from ..base import ApiBase


class Order(ApiBase):
    _category = 'hotel'

    def create(self, **kwargs):
        """创建订单，方法名：hotel.order.create，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.create
        """
        return self._request('create', https=True, **kwargs)

    def list(self, **kwargs):
        """订单列表，方法名：hotel.order.list，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.list
        """
        return self._request('list', https=True, **kwargs)

    def detail(self, **kwargs):
        """订单详情，方法名：hotel.order.create，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.create
        """
        return self._request('detail', https=True, **kwargs)

    def checkguest(self, **kwargs):
        """客人姓名验证，方法名：hotel.order.checkguest

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.checkguest
        """
        return self._request('checkguest', https=True, **kwargs)

    def update(self, **kwargs):
        """修改订单，方法名：hotel.order.update，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.update
        """
        return self._request('update', https=True, **kwargs)

    def cancel(self, **kwargs):
        """取消订单，方法名：hotel.order.cancel，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.cancel
        """
        return self._request('cancel', https=True, **kwargs)

    def instant(self, **kwargs):
        """即时确认，方法名：hotel.order.instant，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.instant
        """
        return self._request('instant', https=True, **kwargs)

    def related(self, **kwargs):
        """ 关联订单，方法名：hotel.order.related，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.related
        """
        return self._request('related', https=True, **kwargs)

    def recent(self, **kwargs):
        """最近预订，方法名：hotel.order.recent，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.recent
        """
        return self._request('recent', https=True, **kwargs)

    def feedback(self, **kwargs):
        """入住反馈，方法名：hotel.order.feedback，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.feedback
        """
        return self._request('feedback', https=True, **kwargs)

    def promote(self, **kwargs):
        """订单催确认，方法名：hotel.order.promote，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.order.promote
        """
        return self._request('promote', https=True, **kwargs)
