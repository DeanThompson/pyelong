from setuptools import setup

setup(
    name='pyelong',
    version='0.0.1',
    packages=['pyelong'],
    url='',
    license='MIT',
    author='Yangliang Li',
    author_email='yanglianglee@gmail.com',
    description='Python SDK for Elong (http://elong.com/) rest APIs.',
    install_requires=[
        'requests>=2.7.0'
    ]
)
