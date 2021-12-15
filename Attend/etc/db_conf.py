# !/usr/bin/env python
# -*- coding=utf-8 -*-

from Attend.common.yml_read_util import get_config_from_file

# 使用dj_db_conn_pool任务池配置
dj_db_conn_pool_conf = get_config_from_file("database.yml", "dj_db_conn_pool", {"is_use_pool": False,
                                                                                "pool_options": {"max_overflow": 10,
                                                                                                 "pool_size": 10}})

db_conf = get_config_from_file("database.yml", "database",
                               {'type': 'mysql',
                                'host': '127.0.0.1',
                                'username': 'root',
                                'password': 'root',
                                'db-name': 'attend',
                                'port': 3306
                                })
db_engine = 'django.db.backends.mysql'

if db_conf['type'] == 'pgsql':
    db_engine = 'django.db.backends.postgresql_psycopg2'
elif db_conf['type'] == 'mysql':
    db_engine = 'django.db.backends.mysql'
elif db_conf['type'] == 'kingbase':
    db_engine = 'qa.src.extend.backends.kingbase'

if dj_db_conn_pool_conf["is_use_pool"]:
    if db_conf['type'] == 'pgsql':
        db_engine = 'dj_db_conn_pool.backends.postgresql'
    elif db_conf['type'] == 'mysql':
        db_engine = 'dj_db_conn_pool.backends.mysql'
    elif db_conf['type'] == 'oracle':
        db_engine = 'dj_db_conn_pool.backends.oracle'
    elif db_conf['type'] == 'kingbase':
        db_engine = 'qa.src.extend.backends.kingbase'

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'USER': db_conf['username'],# root
        'PASSWORD': db_conf['password'],  # root
        'NAME': db_conf['db-name'],  # mysql
        'HOST': db_conf['host'],  # 127.0.0.1
        'PORT': str(db_conf['port']),
    }
}
