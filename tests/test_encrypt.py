# -*- coding: utf-8 -*-

__author__ = 'leon'

import unittest

from testconf import fake_client
from pyelong.util import des_decrypt


class CreditCardNoEncryptTestCase(unittest.TestCase):
    def test_encrypt(self):
        card_no = '4336660000000000'
        timestamp = '1437756898'
        encrypted = fake_client.encrypt_credit_card_no(card_no, timestamp)
        assert encrypted == '6bce37879e7dbbc7122b51851f9dd46bdf7aab4fe6bac513cf054a210fb265e5'

        key = fake_client.request.app_key[-8:]
        plain = des_decrypt(encrypted, key, key)
        assert plain == '%s#%s' % (timestamp, card_no)


if __name__ == '__main__':
    unittest.main()
