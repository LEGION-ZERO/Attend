# !/usr/bin/env python
# -*- coding=utf-8 -*-
import json
from rest_framework import serializers
from .models import *


# 权限表的序列化器
class PemissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name')


# 角色表的序列化器
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


# 部门表的序列化器
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


# 用户表的序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'name', 'password', 'roles', 'department', 'status', 'is_superuser', 'email', 'wechat_id',
            'phone')
