# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from pyelong import Client

client = Client(
    user='user',
    app_key='app_key',
    secret_key='secret_key',
    host='api.test.lohoo.com/rest'  # 测试环境
)
