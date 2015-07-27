#!/usr/bin/env python

import re
from setuptools import setup

with open('pyelong/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

setup(
    name='pyelong',
    version=version,
    packages=[
        'pyelong',
        'pyelong.api',
        'pyelong.api.hotel',
        'pyelong.api.ihotel',
        'pyelong.api.common',
        'pyelong.util'
    ],
    url='https://github.com/DeanThompson/pyelong',
    license='MIT',
    author='Yangliang Li',
    author_email='yanglianglee@gmail.com',
    description='Python SDK for Elong (http://elong.com/) rest APIs.',
    zip_safe=False,
    install_requires=[
        'requests>=2.7.0',
        'tornado>=4.2',
        'pycrypto>=2.6.1'
    ]
)
