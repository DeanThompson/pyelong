# -*- coding: utf-8 -*-

__version__ = '0.5.0'

__all__ = ('Client', 'Request', 'Response')

from .client import Client
from .request import Request
from .response import Response

# Set default logging handler to avoid "No handler found" warnings.
import logging

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
