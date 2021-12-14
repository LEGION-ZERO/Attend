# !/usr/bin/env python
# -*- coding=utf-8 -*-

from Attend.common.yml_read_util import get_config_from_file

dj_db_coon_pool_conf = get_config_from_file("database.yml", "dj_db_coon_pool", {"is_use_pool": False,
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
