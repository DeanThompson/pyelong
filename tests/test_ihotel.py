# -*- coding: utf-8 -*-

__author__ = 'leon'

import datetime

from testconf import client

ci_date = datetime.date.today() + datetime.timedelta(days=1)
co_date = ci_date + datetime.timedelta(days=2)

ci_date = ci_date.isoformat()
co_date = co_date.isoformat()


def test_detail():
    detail_args = {
        'checkInDate': ci_date,
        'checkOutDate': co_date,
        'iHotelId': 331690,
        'options': '1',
        'roomGroup': [{'childAges': '', 'numberOfAdults': 2}]
    }
    client.ihotel.detail(**detail_args)


def test_detail_auto_detect_avail():
    detail_auto_detect_args = {
        'checkInDate': ci_date,
        'checkOutDate': co_date,
        'iHotelId': 331690,
        'options': '1',
        'roomGroup': [
            {'childAges': '', 'numberOfAdults': 2},
            {'childAges': '', 'numberOfAdults': 2}
        ]
    }
    client.ihotel.detail(**detail_auto_detect_args)


def test_detail_avail():
    detail_avail_args = {
        'checkInDate': ci_date,
        'checkOutDate': co_date,
        'iHotelId': 331690,
        'options': '1',
        'roomGroup': [
            {
                'childAges': '1', 'numberOfAdults': 2
            }
        ]
    }

    client.ihotel.detail.avail(**detail_avail_args)


def test_lowest_price():
    price_args = {
        'checkInDate': ci_date,
        'checkOutDate': co_date,
        'iHotelIds': [331690, 324763, 324748],
        'roomGroup': [{'numberOfAdults': 2, 'childAges': None}],
        'options': '1'
    }

    client.ihotel.lowest.price(**price_args)


if __name__ == '__main__':
    test_detail()
    test_detail_avail()
    test_detail_auto_detect_avail()
    test_lowest_price()
