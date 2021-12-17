# !/usr/bin/env python
# -*- coding=utf-8 -*-

''' 
    模块动态引入配置，由开发人员配置
    通用版配置保持不变，项目定制补充配置即可
'''

############### 通用版配置 #####################################################
# job模块配置
JOB_STD_MODEL = False  # qa_task_job表采用通用model，通用：True，定制：False
JOB_PATH = "qa.src.qaTask.ddbx.models"
JOB_SERIALIZER_PATH = "qa.src.qaTask.ddbx.serializers"
JOB_URL = "qa.src.qaTask.ddbx.urls"
JOB_SERVICE_PATH = "qa.src.qaTask.ddbx.service"
# 千寻对接接口
INTERFACE_URL = "qa.src.qaInterface.input.standard.urls"
QX_SERVICE_PATH = "qa.src.qaInterface.input.standard.qianxun"
# 定时任务路径
TIMER_PATH = "qa.src.qaTimer.ddbx.timer_service"
# 项目定制接口路径
CUSTOM_URL = 'qa.src.qaCustom.standard.urls'
# 报表接口路径
ANALYSE_URL = "qa.src.qaAnalyse.standard.urls"
# 报表定制方法路径
REPORT_SERVICE_PATH = "qa.src.qaAnalyse.standard.report_header_data_service"
# 发送邮件服务
SEND_EMAIL_PATH = "qa.src.qaEmail.standard.email_service"
