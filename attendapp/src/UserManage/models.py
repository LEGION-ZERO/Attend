# !/usr/bin/env python
# -*- coding=utf-8 -*-

from django.db import models
from django.conf import settings as conf
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _


# 操作权限类
class Permission(models.Model):
    id = models.CharField('权限编码', max_length=56, primary_key=True, unique=True)
    name = models.CharField('权限名称', max_length=56)

    class Meta:
        db_table = 'usermanage_permission'


# 角色
class Role(models.Model):
    name = models.CharField('角色名称', max_length=56)
    code = models.IntegerField('对应码')
    # 和权限为多对多关系
    permissions = models.ManyToManyField(Permission, related_name='permissions')

    class Meta:
        db_table = 'usermanage_role'


# 部门
class Department(models.Model):
    name = models.CharField('部门名称', max_length=56)
    id_delete = models.BooleanField('是否被删除', default=False)

    class Meta:
        db_table = 'department'


# 自定义用户
class User(AbstractBaseUser):
    username = models.CharField('登陆账号', max_length=30, unique=True,
                                help_text=('Required. 30 characters or fewer. Letters, digits and '
                                           '@/./+/-/_ only.'),
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]+$',  # ^[\w.@+-]+$  ^[\S.@+-]+$
                                                              ('Enter a valid username. '
                                                               'This value may contain only letters, numbers '
                                                               'and @/./+/-/_ characters.'), 'invalid'),
                                ],
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                }
                                )
    password = models.CharField(_('password'), max_length=256)
    name = models.CharField('用户姓名', max_length=64, blank=True, null=True)
    roles = models.ManyToManyField(Role, verbose_name='角色', related_name='roles')
    department = models.ForeignKey(Department, verbose_name='部门', on_delete=models.CASCADE)
    status = models.CharField('在职状态', max_length=256, blank=True, null=True)
    is_superuser = models.IntegerField('是否超级用户', default=0)
    email = models.CharField('邮箱', validators=[
        validators.RegexValidator(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$',
                                  # ^[\w.@+-]+$  ^[\S.@+-]+$
                                  ('Enter a valid email. '
                                   'This value may contain only letters, numbers '
                                   'and @/./+/-/_ characters.'), 'invalid'),
    ], max_length=256, blank=True, null=True)
    wechat_id = models.CharField('微信号', max_length=32, null=True, blank=True)
    phone = models.CharField('电话', max_length=56, null=True, blank=True)
    # 限制登录次数,自动锁定账号
    error_password_count = models.IntegerField("密码输错次数", null=True)
    forbidden_time = models.DateTimeField("禁止登录时间", null=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'usermanage_user'
