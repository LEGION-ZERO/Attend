# !/usr/bin/env python
# -*- coding=utf-8 -*-
from Attend.common.yml_read_util import get_config_from_file



# 限制登录
LIMIT_ERROR_LOGIN = {
    'is-use': get_config_from_file("module-config.yml", "login.limit-error-login.is-use", False),
    'max-error-login-times': get_config_from_file("module-config.yml",
                                                  "login.limit-error-login.max-error-login-times", 10),

    'auto-unlock-duration': get_config_from_file("module-config.yml",
                                                 "login.limit-error-login.auto-unlock-duration", 30),
    'force-change-password': get_config_from_file("module-config.yml",
                                                  "login.limit-error-login.force-change-password", False),
    'force-change-password-days': get_config_from_file("module-config.yml",
                                                       "login.limit-error-login.force-change-password-days", 90),

}

# 密码加密传输设置
PASSWORD_ENCRYPT_METHOD = get_config_from_file("module-config.yml", "login.encrypt-password.encrypt-method", "RSA")
if PASSWORD_ENCRYPT_METHOD == 'SM2':
    # django 密码加密方式
    PASSWORD_HASHERS = (
        'attendapp.src.Auth.localAuth.password_encrypt_service.SM2PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
        'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.CryptPasswordHasher',
    )
    SM2_KEY = {
        'publicKey': get_config_from_file("module-config.yml", "login.encrypt-password.sm2-public-key", ""),
        'privateKey': get_config_from_file("module-config.yml", "login.encrypt-password.sm2-private-key", "")
    }