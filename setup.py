from setuptools import setup

setup(
    name='pyelong',
    version='0.0.1',
    packages=['pyelong', 'pyelong.api', 'pyelong.api.hotel'],
    url='',
    license='MIT',
    author='Yangliang Li',
    author_email='yanglianglee@gmail.com',
    description='Python SDK fro Elong (http://elong.com/) rest API',
    install_requires=[
        'requests>=2.7.0'
    ]
)
