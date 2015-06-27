# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.basename('..'))

from tornado.web import RequestHandler, Application
from tornado import gen, ioloop, options

from pyelong import Client

env = lambda x: os.environ.get(x)

client = Client(
    user=env('elong_user'),
    app_key=env('elong_app_key'),
    secret_key=env('elong_secret_key'),
    host='api.test.lohoo.com/rest',  # 测试环境
    use_tornado=True   # AsyncHTTPClient
)

sync_client = Client(
    user=env('elong_user'),
    app_key=env('elong_app_key'),
    secret_key=env('elong_secret_key'),
    host='api.test.lohoo.com/rest',  # 测试环境
    use_tornado=False  # requests
)


class HelloHandler(RequestHandler):
    def get(self, name):
        self.write('Hello, ' + name)


class HotelListHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        print '+++++' * 10
        resp = yield client.hotel.list(ArrivalDate='06/24/2015',
                                       DepartureDate='06/25/2015',
                                       CityId='0101')
        print '-----' * 10
        self.write(resp.to_json())


class SyncHotelListHandler(RequestHandler):
    def get(self):
        print '*****' * 10
        resp = sync_client.hotel.list(ArrivalDate='06/24/2015',
                                      DepartureDate='06/25/2015',
                                      CityId='0101')
        print '#####' * 10
        self.write(resp.to_json())


options.parse_command_line()

settings = {
    'debug': True
}

application = Application([
    (r'/hello/(.*)', HelloHandler),
    (r'/hotel/list', HotelListHandler),
    (r'/sync/hotel/list', SyncHotelListHandler),
], **settings)

application.listen(port=9999)
ioloop.IOLoop().instance().start()

# $ ab -n 10 -c 5 http://127.0.0.1:9999/hotel/list
# Concurrency Level:      5
# Time taken for tests:   0.269 seconds
# Complete requests:      10
# Failed requests:        0
# Total transferred:      7960 bytes
# HTML transferred:       5950 bytes
# Requests per second:    37.12 [#/sec] (mean)
#     Time per request:       134.713 [ms] (mean)
# Time per request:       26.943 [ms] (mean, across all concurrent requests)
# Transfer rate:          28.85 [Kbytes/sec] received
#
# Connection Times (ms)
# min  mean[+/-sd] median   max
# Connect:        0    0   0.1      0       0
# Processing:   102  128  18.2    139     151
# Waiting:      102  128  18.2    139     151
# Total:        102  128  18.2    139     151


# $ ab -n 10 -c 5 http://127.0.0.1:9999/sync/hotel/list
# Concurrency Level:      5
# Time taken for tests:   1.078 seconds
# Complete requests:      10
# Failed requests:        5
# (Connect: 0, Receive: 0, Length: 5, Exceptions: 0)
# Total transferred:      7955 bytes
# HTML transferred:       5945 bytes
# Requests per second:    9.28 [#/sec] (mean)
#     Time per request:       539.034 [ms] (mean)
# Time per request:       107.807 [ms] (mean, across all concurrent requests)
# Transfer rate:          7.21 [Kbytes/sec] received
#
# Connection Times (ms)
# min  mean[+/-sd] median   max
# Connect:        0    0   0.1      0       0
# Processing:   132  436 149.9    529     562
# Waiting:      131  436 149.8    529     562
# Total:        132  436 149.8    529     563
