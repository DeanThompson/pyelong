# -*- coding: utf-8 -*-

from pyelong.request import Request
from pyelong.api.hotel import Hotel
from pyelong.api.ihotel import Ihotel
from pyelong.api.common import Common


class Client(object):
    def __init__(self, user, app_key, secret_key, **kwargs):
        self.request = Request(user, app_key, secret_key, **kwargs)

    @property
    def hotel(self):
        return Hotel(self)

    @property
    def ihotel(self):
        return Ihotel(self)

    @property
    def common(self):
        return Common(self)
