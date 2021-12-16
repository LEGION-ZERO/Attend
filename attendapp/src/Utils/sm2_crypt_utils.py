# !/usr/bin/env python
# -*- coding:utf-8 -*-
from gmssl import sm2, func


class SM2Encrypt(object):

    def __init__(self, private_key, public_key):
        self.public_key = public_key
        self.private_key = private_key
        self.sm2_func = sm2.CryptSM2(public_key=self.public_key, private_key=self.private_key)

    def encrypt(self, data: bytes):
        return self.sm2_func.encrypt(data)

    def decrypt(self, data: bytes):
        return self.sm2_func.decrypt(data)

    def sign(self, data: bytes):
        random_hex_str = func.random_hex(self.sm2_func.para_len)
        return self.sm2_func.sign(data, random_hex_str)

    def verify(self, sign, data):
        return self.sm2_func.verify(sign, data)


if __name__ == '__main__':
    private_key = '6C5B1CC156AE465EF26973E0E01C466157B81521D448D4F6DE6671A697FCB1B6'
    public_key = '27AE9564D854B5585BF1662225B9AF566A3877F389AB64B085D52ABE02D988593912F8185ED47FC41574FB6BDB5EE118643CA11FCF655E3336B3E6C36A8F1645'
    s = SM2Encrypt(private_key=private_key, public_key=public_key)
    src_message = s.decrypt(bytes.fromhex(
        "9438661a0127505806ccc7a46c5006731deb3791a5f1ffa7b84762d803c91c201ad4746585b0358c20d2606d96b09a8fa2e3ddfc001587e82721c35ba7bb4f7ebb3770aba5624446ffe89b3f38d9df8f91f72cc6cc1eb7fe2186ca9d835f203bd9a5dd6dcd"))
    print(src_message)

    print(bytes.fromhex(
        "9438661a0127505806ccc7a46c5006731deb3791a5f1ffa7b84762d803c91c201ad4746585b0358c20d2606d96b09a8fa2e3ddfc001587e82721c35ba7bb4f7ebb3770aba5624446ffe89b3f38d9df8f91f72cc6cc1eb7fe2186ca9d835f203bd9a5dd6dcd"))

