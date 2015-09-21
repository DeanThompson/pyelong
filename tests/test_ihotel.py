# -*- coding: utf-8 -*-

__author__ = 'leon'

from testconf import client

detail_args = {
    u'checkInDate': u'2015-09-23',
    u'checkOutDate': u'2015-09-24',
    u'iHotelId': 331690,
    u'options': u'1',
    u'roomGroup': [
        {
            u'childAges': u'', u'numberOfAdults': 2
        }
    ]
}

detail_avail_args = {
    u'checkInDate': u'2015-09-23',
    u'checkOutDate': u'2015-09-24',
    u'iHotelId': 331690,
    u'options': u'1',
    u'roomGroup': [
        {
            u'childAges': u'1', u'numberOfAdults': 2
        }
    ]
}

client.ihotel.detail(**detail_args)

client.ihotel.detail.avail(**detail_avail_args)
