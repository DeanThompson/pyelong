# -*- coding: utf-8 -*-

from pyelong.request import Request
from pyelong.api.hotel import Hotel


class Client(object):
    def __init__(self, user, app_key, secret_key, **kwargs):
        self.request = Request(user, app_key, secret_key, **kwargs)

    @property
    def hotel(self):
        return Hotel(self)

    @property
    def ihotel(self):
        return None
