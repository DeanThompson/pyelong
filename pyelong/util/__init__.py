# -*- coding: utf-8 -*-

__author__ = 'leon'

from Crypto.Cipher import DES

try:
    from Crypto.Util.Padding import pad, unpad
except ImportError:
    from .padding import pad, unpad


def utf8(value):
    """Converts a string argument to a byte string.

    If the argument is already a byte string or None, it is returned unchanged.
    Otherwise it must be a unicode string and is encoded as utf8.

    Taken from `tornado.escape.utf8`.
    """
    if isinstance(value, bytes):
        return value
    if not isinstance(value, unicode):
        raise TypeError('Expected bytes, unicode; got %r' % type(value))
    return value.encode('utf-8')


def des_encrypt(data, key, iv, mode=DES.MODE_CBC):
    cipher = DES.new(key, mode=mode, IV=iv)
    padded_text = pad(utf8(data), cipher.block_size)
    return cipher.encrypt(padded_text).encode('hex')


def des_decrypt(data, key, iv, mode=DES.MODE_CBC):
    cipher = DES.new(key, mode=mode, IV=iv)
    decrypted = cipher.decrypt(data.decode('hex'))
    return unpad(decrypted, cipher.block_size)
