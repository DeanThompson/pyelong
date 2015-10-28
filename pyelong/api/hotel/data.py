# -*- coding: utf-8 -*-

from ..base import ApiBase


class Data(ApiBase):
    _category = 'hotel'

    def rp(self, **kwargs):
        """产品详情，方法名：hotel.data.rp

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.data.rp

        NOTE
        ~~~~
            - 本接口属于高级功能接口，通常开发使用不到，不建议使用。
        """
        return self._request('rp', **kwargs)

    def inventory(self, **kwargs):
        """房态库存，方法名：hotel.data.inventory

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.data.inventory

        NOTE
        ~~~~
            - 本接口属于高级功能接口，通常开发使用不到，不建议使用。
            - 本接口不能获取万豪集团酒店的库存数据；万豪集团酒店的报价请使用hotel.detail接口。
        """
        return self._request('inventory', **kwargs)

    def rate(self, **kwargs):
        """产品详情，方法名：hotel.data.rate

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.data.rate

        NOTE
        ~~~~
            - 本接口属于高级功能接口，通常开发使用不到，不建议使用。
            - 本接口不能获取直连酒店(目前是万豪集团的酒店)的价格数据；其报价请使用hotel.detail接口。
        """
        return self._request('rate', **kwargs)

    def validate(self, **kwargs):
        """房态库存，方法名：hotel.data.validate

        文档
        ~~~~
            - http://open.elong.com/wiki/Hotel.data.validate
        """
        return self._request('validate', **kwargs)
