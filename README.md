pyelong
=======

[艺龙 API](http://open.elong.com/wiki/API%E6%96%87%E6%A1%A3) 的 Python 封装。

参考了 @icyleaf 的这个项目：[https://github.com/icyleaf/elong/](https://github.com/icyleaf/elong/)

## 特点

- 支持国内酒店(hotel)／国际酒店(ihotel)等所有 API
- 自动选择 HTTP／HTTPS
- 计算签名、生成请求链接
- 使用简单，调用参数与文档保持一致

## 不支持

- 没有针对 API 做参数检查
- 出错时不检查 code，没有重试
- 不支持 xml 格式的请求和返回值

## 安装

```bash
git clone git@github.com:DeanThompson/pyelong.git
cd pyelong
python setup.py install
```

依赖 [requests](http://docs.python-requests.org/en/latest/) 库.

## 使用

假设已经在艺龙注册了 API 用户，得到了 `user`, `app_key`, `secret_key`，并且 IP 已经在艺龙的白名单里。

### 初始化一个客户端 `client`

```python
from pyelong import Client

client = Client(user=user, app_key=app_key, secret_key=secret_key)

# 初始化 client 时还可以传入：

- host: 指定 API 的 host，在开发时最好指定测试环境的 host
- local: 语言
- version: API 版本，默认 1.1
- debug: 设置为 True 在开发时会在标准输出看到请求的 URL 和返回值
```

### 调用

```python
response = client.hotel.list(ArrivalDate='06/24/2015', DepartureDate='06/25/2015', CityId='0101')

# HTTP 状态码
print response.status_code

# API 状态码
print response.code

# API 错误
print response.error

# API 返回结果，是一个 json 对象
print response.result

# print response
```

## LICENSE

[The MIT License](LICENSE)
