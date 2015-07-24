# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from pyelong import Client

client = Client(
    user=os.environ.get('elong_user'),
    app_key=os.environ.get('elong_app_key'),
    secret_key=os.environ.get('elong_secret_key'),
    host='api.test.lohoo.com/rest'  # 测试环境
)

fake_client = Client(
    user='test_user',
    app_key='84ac5067a15058e86eceffde1b903a89',
    secret_key='6e06826ce933d8b8a35279c966a2da64'
)
