# -*- coding: utf-8 -*-

__author__ = 'leon'

import unittest

from testconf import fake_client


class CreditCardEncryptTestCase(unittest.TestCase):
    def test_encrypt(self):
        timestamp = '1438229745'
        card_info = {
            'card_no': '4336660000000000',
            'cvv': 123,
            'expiration_year': 2018,
            'expiration_month': 10,
            'holder_name': '张三',
            'identification_type': '1',
            'identification_no': '123456198910232415'
        }

        encrypted = fake_client.encrypt_credit_card_fields(card_info, timestamp)

        expected_values = {
            'card_no': '5296efb22a20bd7115cbd9791d6944b7799180c0d30d78acf5f65fee9c5d121e',
            'cvv': '5296efb22a20bd718676c97935b92751',
            'expiration_year': '5296efb22a20bd7189c0e4e63add66b7',
            'expiration_month': '5296efb22a20bd71e066e44fcff5b25e',
            'holder_name': '5296efb22a20bd71ba9a0b813b783b6095d9a4c46b2b0e9b',
            'identification_type': '5296efb22a20bd711080d90abb03d4e5',
            'identification_no': '5296efb22a20bd71970ff9714c04123a929ab771c6c5dac0e427079601eab828'
        }

        for k, v in encrypted.iteritems():
            assert v == expected_values[k]


if __name__ == '__main__':
    unittest.main()
