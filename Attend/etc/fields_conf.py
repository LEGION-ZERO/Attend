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