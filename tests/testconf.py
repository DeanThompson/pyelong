# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

import logging

from pyelong import Client
from api_settings import ELONG_API_SETTINGS

logging.basicConfig(level=logging.DEBUG)

client = Client(**ELONG_API_SETTINGS)

fake_client = Client(
    user='test_user',
    app_key='84ac5067a15058e86eceffde1b903a89',
    secret_key='6e06826ce933d8b8a35279c966a2da64'
)
