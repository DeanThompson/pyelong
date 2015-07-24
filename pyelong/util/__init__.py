# -*- coding: utf-8 -*-

__author__ = 'leon'

from Crypto.Cipher import DES

try:
    from Crypto.Util.Padding import pad, unpad
except ImportError:
    from .padding import pad, unpad


def des_encrypt(data, key, iv, mode=DES.MODE_CBC):
    cihper = DES.new(key, mode=mode, IV=iv)
    padded_text = pad(data, cihper.block_size)
    return cihper.encrypt(padded_text).encode('hex')


def des_decrypt(data, key, iv, mode=DES.MODE_CBC):
    cipher = DES.new(key, mode=mode, IV=iv)
    decrypted = cipher.decrypt(data.decode('hex'))
    return unpad(decrypted, cipher.block_size)
