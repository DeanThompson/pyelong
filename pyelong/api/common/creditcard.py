# -*- coding: utf-8 -*-

from ..base import ApiBase


class CreditCard(ApiBase):
    _category = 'common'

    def validate(self, **kwargs):
        """信用卡验证，方法名：common.creditcard.validate，必须使用 https

        文档
        ~~~~
            - http://open.elong.com/wiki/Common.creditcard.validate
        """
        return self._request('validate', https=True, **kwargs)
