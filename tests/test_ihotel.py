# -*- coding: utf-8 -*-

__author__ = 'leon'

import datetime

from testconf import client

ci_date = datetime.date.today() + datetime.timedelta(days=1)
co_date = ci_date + datetime.timedelta(days=2)

ci_date = ci_date.isoformat()
co_date = co_date.isoformat()

detail_args = {
    u'checkInDate': ci_date,
    u'checkOutDate': co_date,
    u'iHotelId': 331690,
    u'options': u'1',
    u'roomGroup': [
        {
            u'childAges': u'', u'numberOfAdults': 2
        }
    ]
}

detail_auto_detect_args = {
    u'checkInDate': ci_date,
    u'checkOutDate': co_date,
    u'iHotelId': 331690,
    u'options': u'1',
    u'roomGroup': [
        {
            u'childAges': u'', u'numberOfAdults': 2
        },
        {
            u'childAges': u'', u'numberOfAdults': 2
        }
    ]
}

detail_avail_args = {
    u'checkInDate': ci_date,
    u'checkOutDate': co_date,
    u'iHotelId': 331690,
    u'options': u'1',
    u'roomGroup': [
        {
            u'childAges': u'1', u'numberOfAdults': 2
        }
    ]
}

client.ihotel.detail(**detail_args)

client.ihotel.detail(**detail_auto_detect_args)

client.ihotel.detail.avail(**detail_avail_args)

price_args = {
    'checkInDate': ci_date,
    'checkOutDate': co_date,
    'iHotelIds': [331690, 324763, 324748],
    'roomGroup': [
        {'numberOfAdults': 2, 'childAges': None}
    ],
    'options': '1'
}

client.ihotel.lowest.price(**price_args)
