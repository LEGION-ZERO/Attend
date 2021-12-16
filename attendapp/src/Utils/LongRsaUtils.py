#!/usr/bin/python3.7
#coding=utf-8
import os
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import datetime
import base64
from django.conf import settings as conf
import logging
from PQA.common.yml_read_util import get_config_from_file

def create_rsa_key():
    # 伪随机数生成器
    random_generator = Random.new().read # 随机数 生成器，默认方式，可不填，可接受 整数值 反回对应整数长度字节随机数
    # rsa算法生成实例
    rsa = RSA.generate(1024, random_generator)

    #--------------------------------------------生成公私钥对文件-----------------------------------------------------------
    # 秘钥对的生成
    private_pem = rsa.exportKey()
    with open(conf.BASE_DIR+r'/private.pem', 'wb') as f:
        f.write(private_pem)

    public_pem = rsa.publickey().exportKey()
    with open(conf.BASE_DIR+r'/public.pem', 'wb') as f:
        f.write(public_pem)

def rsa_long_encrypt(pub_key_str, msg, length=100):
    """
    单次加密串的长度最大为 (key_size/8)-11
    1024bit的证书用100， 2048bit的证书用 200
    """
    rsakey = RSA.importKey(pub_key_str)
    pubobj = PKCS1_v1_5.new(rsakey)
    res = []
    for i in range(0, len(msg), length):
        encrypt_txt = pubobj.encrypt(msg[i:i+length])
        res.append(encrypt_txt)
    return b"".join(res)


def rsa_long_decrypt(priv_key_str, msg, length=128):
    """
    # 1024bit的证书用128，2048bit证书用256位
    # """
    rsakey = RSA.importKey(priv_key_str)
    privobj = PKCS1_v1_5.new(rsakey)
    res = []
    for i in range(0, len(msg), length):
        res.append(privobj.decrypt(msg[i:i+length], "ERROR"))
    return b"".join(res)

def encrypt_encode(data):
    """
    base64编码 rsa加密
    :param value: 需要加密编码的数据
    :return:
    """
    try:
        encrypt_data = rsa_long_encrypt(read_publicKey(), data.encode("utf-8"))
        encode_data = base64.b64encode(encrypt_data)
        return encode_data
    except Exception:
        logging.exception("encrypt_encode:加密编码失败"+str(Exception.message))

def decrypt_decode(data):
    """
    base64解码 rsa解密
    :param value: 需要解密的数据
    :return:
    """
    try:
        # missing_padding = 4 - len(data) % 4
        # if missing_padding:
        #     data += '=' * missing_padding
        decode_data = base64.b64decode(data)
        # f= str(open(conf.BASEDIR + "/private.pem", "r").read())
        decrypt_data = rsa_long_decrypt(read_privateKey(), decode_data).decode("utf-8")
        return decrypt_data
    except Exception:
        logging.exception("decrypt_decode:解码解密失败"+str(Exception.message))


def decrypt_pass(password):
    '''
    解密前端引用jsencrypto的加密（RSA）字符串
    :param password:
    :return:
    '''
    random_generator = Random.new().read
    RSA.generate(1024, random_generator)
    privateKey = read_privateKey()
    rsakey = RSA.importKey(privateKey)
    cipher = PKCS1_v1_5.new(rsakey)
    return cipher.decrypt(base64.b64decode(password), random_generator)


def read_publicKey():
    '''
    获取公钥
    :return:
    '''
    public_key_path = os.path.join(conf.BASE_DIR, "public.pem")
    if os.path.exists(public_key_path):
        with open(conf.BASE_DIR + "/public.pem", 'r') as f:
            publicKey = f.read()
            return publicKey
    return '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCiBXfat40qZPzSjx1dJ6dbBC3Z
Lbl9zRU9qCYnakbYze/lWx350wL+e6sR/+WFfayqJPlFL/jXrQIMHAp7a75kYse8
YLiA1FGporTwILejsI6He1dXuMaSaaO6zxOXH4rsrLpn0h+b3iJOk/edwrrW/YDK
zAm9xd/LHi9EAvBSlQIDAQAB
-----END PUBLIC KEY-----'''


def read_privateKey():
    '''
    获取私钥
    :return:
    '''
    private_key_path = os.path.join(conf.BASE_DIR, "private.pem")
    if os.path.exists(private_key_path):
        with open(conf.BASE_DIR + "/private.pem", 'r') as f:
            privateKey = f.read()
            return privateKey
    return '''-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCiBXfat40qZPzSjx1dJ6dbBC3ZLbl9zRU9qCYnakbYze/lWx35
0wL+e6sR/+WFfayqJPlFL/jXrQIMHAp7a75kYse8YLiA1FGporTwILejsI6He1dX
uMaSaaO6zxOXH4rsrLpn0h+b3iJOk/edwrrW/YDKzAm9xd/LHi9EAvBSlQIDAQAB
AoGAAKXQ8tjlAZRhxl24GlU8QArmPAYIxc36FcMEVAgCvH8mRF524jbLvkS0TGAf
hMcZ15xKOtKURhh096NtD01A95gjZWVwZcy/Ehy9FWU/m1eV50inpqiS35N8kR3d
hkopwzyQlagPO73s3T60BgNb2KRIk1V3PYwr9E5GkZOBWokCQQC8jp2lOje70kTM
2biB0iAFISM/6MrLA8VSqx36hvoi58AkqleC2NztLbEq4sBsQRf/4PO6BqKfosSP
hdj3oJLPAkEA2/kWGX8HfUPt0MeLU6hba60H1tqzywr1xrWUl1eyycbvoaRd2Ses
OKsqiRBBmwKKGb97LsOU4lQCbJYFWoZtWwJBALmzO08epwUzcM7PHge9CgwDNtQa
UJ7gd9WS8VNq267Ez1dM7CLRscNk3Ld/2kLDWP+IbIEpR8AwbaVsDOLUIcECQDoK
QvZ/Oe6nWbxYqj5skZKbmRHrqrzMK4U+q/IyxY3P27J+t/RwL1TUdOitTWIlDWM1
zr7MBCCjofActVTpWzkCQFbWab14Pa3OsaI0DscxhUX9m9IWbt4fC0tl6IG2lTSx
0tCSb9o+obkjKQVIswLwd3fHEpFDwWkroQo6eC0ok24=
-----END RSA PRIVATE KEY-----'''


if __name__ == "__main__":
    create_rsa_key()
    # BASE_DIR = "D:\\Work\\PQA\\"
    # create_rsa_key()
    # msg = "52222222222222222211111111"
    # print(len(msg))
    # starttime1 = datetime.datetime.now()
    # enres = rsa_long_encrypt(open(BASE_DIR+"/public.pem","r").read(), msg.encode("utf-8"))
    # starttime2 = datetime.datetime.now()
    # print("encrypt cost time",(starttime2 - starttime1).seconds)
    # print(len(enres))
    # deres = rsa_long_decrypt(open(BASE_DIR+"/private.pem","r").read(), enres).decode('utf-8')
    # starttime3 = datetime.datetime.now()
    # print("decrypt cost time",(starttime3 - starttime2).seconds)
    # print(msg == deres)

    # phone = "13366218336"
    # bank_account = "6228480010999521718"
    # id_card = "522627199711112222"
    # en_phone = base64.b64encode(rsa_long_encrypt(open(BASE_DIR+"\public.pem","r").read(), phone.encode("utf-8")))
    # en_bank_account = base64.b64encode(rsa_long_encrypt(open(BASE_DIR+"/public.pem","r").read(), bank_account.encode("utf-8")))
    # en_id_card = base64.b64encode(rsa_long_encrypt(open(BASE_DIR+"/public.pem","r").read(), id_card.encode("utf-8")))
    # print("en_phone:"+str(en_phone))
    # print("="*10)
    # print("en_bank_account:"+str(en_bank_account))
    # print("=" * 10)
    # print("en_id_card:"+str(en_id_card))
    #
    # print("=" * 10)
    # decode_data = base64.b64decode(en_phone)
    # decode = rsa_long_decrypt(open(BASE_DIR + "\private.pem", "r").read(), decode_data).decode("utf-8")
    # print(decode)

    # f = 'D:\Work\PQA/qa/static/qa/download/质检系统_明细报表_20191220-180101.xlsx'.encode('utf-8')+"1111"
    # print(str(f))
