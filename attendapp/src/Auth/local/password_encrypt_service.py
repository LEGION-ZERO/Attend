# !/usr/bin/env python
# -*- coding=utf-8 -*-

from attendapp.src.Utils.sm2_crypt_utils import SM2Encrypt
from django.conf import settings as conf
from attendapp.src.Utils import LongRsaUtils

private_key = ""
public_key = ""
if hasattr(conf, "SM2_KEY"):
    private_key = conf.SM2_KEY['privateKey']
    public_key = conf.SM2_KEY['publicKey']
sm2_client = SM2Encrypt(private_key=private_key,
                        public_key=public_key)


class PasswordDecryptService(object):

    def decrypt(self, password):
        if self.is_sm2_encrypt():
            return sm2_client.decrypt(bytes.fromhex(password))
        return LongRsaUtils.decrypt_pass(password)

    def get_encrypt_method(self):
        if hasattr(conf, 'PASSWORD_ENCRYPT_METHOD'):
            return conf.PASSWORD_ENCRYPT_METHOD
        return "RSA"

    def is_sm2_encrypt(self):
        return hasattr(conf, 'PASSWORD_ENCRYPT_METHOD') and conf.PASSWORD_ENCRYPT_METHOD == 'SM2'

    def readPublicKey(self):
        if self.is_sm2_encrypt():
            return public_key
        return LongRsaUtils.read_publicKey()
