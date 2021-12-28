# !/usr/bin/env python
# -*- coding=utf-8 -*-
"""
The script is used to init database
"""

from django.conf import settings as conf

data = [
    {
        "descripe": "操作权限",
        "table_name": "usermanage_permission",
        "init_data": [
            {"id": 000, "name": "系统管理"},
            {"id": 100, "name": "查看"},
            {"id": 101, "name": "修改"},
            {"id": 102, "name": "增加"},
            {"id": 103, "name": "删除"},
        ]
    },
    {
        "descripe": "用户角色",
        "table_name": "usermanage_role",
        "init_data": [
            {"id": 1, "name": "系统管理员", "code": "110"},
            {"id": 2, "name": "部门经理", "code": "111"},
            {"id": 3, "name": "部门主管", "code": "112"},
            {"id": 4, "name": "员工", "code": "113"},
        ]
    },
    {
        "descripe": "角色权限",
        "table_name": "usermanage_role_permissions",
        "init_data": [
            # 系统管理员
            {"role_id": 1, "permission_id": 000},

            # 部门经理
            {"role_id": 2, "permission_id": 100},
            {"role_id": 2, "permission_id": 101},
            {"role_id": 2, "permission_id": 102},
            {"role_id": 2, "permission_id": 103},

            # 部门主管
            {"role_id": 3, "permission_id": 100},
            {"role_id": 3, "permission_id": 101},
            {"role_id": 3, "permission_id": 102},

            # 员工
            {"role_id": 4, "permission_id": 100},
        ]
    },
    {
        "descripe": "部门",
        "table_name": "department",
        "init_data": [
            {"id": 1, "name": "研发部", "is_delete": 0},
            {"id": 2, "name": "测试部", "is_delete": 0},
            {"id": 3, "name": "运维部", "is_delete": 0},
        ]
    },
    {
        "descripe": "用户",
        "table_name": "usermanage_user",
        "init_data": [
            {"id": 1, "last_login": "2018-01-01", "username": "emp1", "password": "123456", "name": "员工1",
             "status": "在职", "is_superuser": 0, "email": "12345671@qq.com", "wechat_id": "wx123456781",
             "department_id": 1},
            {"id": 2, "last_login": "2018-01-01", "username": "emp2", "password": "123456", "name": "员工2",
             "status": "在职", "is_superuser": 0, "email": "12345672@qq.com", "wechat_id": "wx123456782",
             "department_id": 1},
            {"id": 3, "last_login": "2018-01-01", "username": "charge", "password": "123456", "name": "部门主管",
             "status": "在职", "is_superuser": 0, "email": "12345673@qq.com", "wechat_id": "wx123456783",
             "department_id": 1},
            {"id": 4, "last_login": "2018-01-01", "username": "manage", "password": "123456", "name": "部门经理",
             "status": "在职", "is_superuser": 0, "email": "12345674@qq.com", "wechat_id": "wx123456784",
             "department_id": 1},
            {"id": 5, "last_login": "2018-01-01", "username": "admin", "password": "123456", "name": "系统管理员",
             "status": "在职", "is_superuser": 1, "email": "12345675@qq.com", "wechat_id": "wx123456785",
             "department_id": 1},
        ]
    },
    {
        "descripe": "用户角色",
        "table_name": "usermanage_user_roles",
        "init_data": [
            {"user_id": 1, "role_id": 4},
            {"user_id": 2, "role_id": 4},
            {"user_id": 3, "role_id": 3},
            {"user_id": 4, "role_id": 2},
            {"user_id": 5, "role_id": 1},
        ]
    },
]
