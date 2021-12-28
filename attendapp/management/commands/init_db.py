# !/usr/bin/env python
# -*- coding=utf-8 -*-
"""
author: Hu lin
This script is used to init sql
"""
from django.core.management.base import BaseCommand
from django.db import connection
import logging
from django.conf import settings as conf

from attendapp.management.system_sql_data import data


class Command(BaseCommand):
    help = '初始化数据'

    def handle(self, *args, **options):
        run()


def run():
    logging.info('开始初始化数据,请稍等......')
    excute_init(data)
    logging.info('初始化数据库结束......')


def excute_init(data):
    column_char = '"'
    if use_db_type() == 'mysql':
        column_char = "`"
    for table in data:
        table_name = table['table_name']
        init_data = table['init_data']
        for init_row in init_data:
            keys = []
            values = []
            for key in init_row:
                keys.append(column_char + str(key) + column_char)
                values.append("'" + str(init_row[key]) + "'")
            keys_str = ",".join(keys)
            values_str = ",".join(values)
            sql = "insert into " + table_name + "(" + keys_str + ") values(" + values_str + ")"
            excute_sql(sql)

        #  初始设置数据库索引的序列值，  避免有数据，但新增的时候仍然从第一个值开始
        if use_db_type() != 'mysql':
            if table_name != 'usermanage_permission':  # id是permission的编码值，id非自增的
                seq_sql = "SELECT setval('" + table_name + "_id_seq', COALESCE((SELECT MAX(id)+1 FROM " + table_name + "), 1), false)"
                print("seq_sql:", seq_sql)
                excute_sql(seq_sql)

        print("init " + table_name + " success")


def use_db_type():
    if str(conf.DATABASES['default']['ENGINE']).__contains__('mysql'):
        return "mysql"
    return "pgsql"


def excute_sql(str_sql):
    try:
        cur = connection.cursor()
        cur.execute(str_sql)
    except Exception as e:
        print(e)
        print("sql:执行失败：{}".format(str_sql))
