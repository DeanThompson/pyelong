# -*- coding: utf-8 -*-

from ..base import ApiBase


class Detail(ApiBase):
    _category = 'ihotel'

    def avail(self, **kwargs):
        """国际酒店详情，方法名：ihotel.detail.avail

        文档
        ~~~~
            - http://open.elong.com/wiki/Ihotel.detail

        NOTE
        ~~~~
            - 请求的入出参数和ihotel.detail一样
            - 属于实时数据接口，将不使用缓存
            - 实时接口访问控制频次更严格(每秒5次)
        """
        return self._request('avail', raw=True, **kwargs)

    def __call__(self, **kwargs):
        """国际酒店详情，方法名：ihotel.detail

        文档
        ~~~~
            - http://open.elong.com/wiki/Ihotel.detail

        NOTE
        ~~~~

        本接口是基于缓存的响应速度快，适用于本地缓存数据或快速展示一个粗略的价格，入参有限制：
            - 只能一个房间
            - 房间大人个数是1或者2，不能带小孩
            - 传入 productId 参数，将不受上面的限制并且结果不使用缓存
        """
        use_detail_avail = False
        room_group = kwargs.get('roomGroup', [])
        if room_group:
            if len(room_group) > 1:
                use_detail_avail = True
            else:
                room = room_group[0]
                if room['childAges'] or room['numberOfAdults'] > 2:
                    use_detail_avail = True

        if use_detail_avail:
            return self._request('avail', raw=True, **kwargs)

        return self._request('', raw=True, **kwargs)
