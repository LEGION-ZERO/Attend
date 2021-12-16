# !/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.http import HttpResponse

from attendapp.src.Auth.local.password_encrypt_service import PasswordDecryptService


def loginview(request):
    """
    登陆页面
    """
    password_service = PasswordDecryptService()
    # 加密公钥
    publicKey = password_service.readPublicKey()
    # 加密方法
    encrypt_method = password_service.get_encrypt_method()
    return render(request, 'attendapp/login.html',
                  {"publicKey": publicKey, 'encryptMethod': encrypt_method})


def index(request):
    return HttpResponse("跳转ok")
