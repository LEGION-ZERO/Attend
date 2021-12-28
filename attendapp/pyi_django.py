# -*- coding=utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2005-2019, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
# -----------------------------------------------------------------------------


# This Django rthook was tested with Django 1.8.3.


import django.core.management
import django.utils.autoreload
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from pathlib import Path
import django.contrib.auth.password_validation as password_validation


# 这是pyinstaller打包后，django 运行前 执行的脚本
# 在这里可以修改django的代码,相当于修改了django的源码

def _get_commands():
    # Django groupss commands by app.
    # This returns static dict() as it is for django 1.8 and the default project.
    commands = {
        'changepassword': 'django.contrib.auth',
        'check': 'django.core',
        'clearsessions': 'django.contrib.sessions',
        'collectstatic': 'django.contrib.staticfiles',
        'compilemessages': 'django.core',
        'createcachetable': 'django.core',
        'createsuperuser': 'django.contrib.auth',
        'dbshell': 'django.core',
        'diffsettings': 'django.core',
        'dumpdata': 'django.core',
        'findstatic': 'django.contrib.staticfiles',
        'flush': 'django.core',
        'inspectdb': 'django.core',
        'loaddata': 'django.core',
        'makemessages': 'django.core',
        'makemigrations': 'django.core',
        'migrate': 'django.core',
        'runfcgi': 'django.core',
        'runserver': 'django.core',
        'shell': 'django.core',
        'showmigrations': 'django.core',
        'sql': 'django.core',
        'sqlall': 'django.core',
        'sqlclear': 'django.core',
        'sqlcustom': 'django.core',
        'sqldropindexes': 'django.core',
        'sqlflush': 'django.core',
        'sqlindexes': 'django.core',
        'sqlmigrate': 'django.core',
        'sqlsequencereset': 'django.core',
        'squashmigrations': 'django.core',
        'startapp': 'django.core',
        'startproject': 'django.core',
        'syncdb': 'django.core',
        'test': 'django.core',
        'testserver': 'django.core',
        'validate': 'django.core',
        'init_db': 'hulin',
        'make_data': 'hulin',
    }
    return commands


def get_child_arguments():
    """
    Return the executable. This contains a workaround for Windows if the
    executable is reported to not have the .exe extension which can cause bugs
    on reloading.
    """
    import django.__main__
    from pathlib import Path
    import sys
    django_main_path = Path(django.__main__.__file__)
    py_script = Path(sys.argv[0])

    args = [sys.executable] + ['-W%s' % o for o in sys.warnoptions]
    if py_script == django_main_path:
        # The server was started with `python -m django runserver`.
        args += ['-m', 'django']
        args += sys.argv[1:]
    else:
        args += sys.argv
    return args


# 修改django启动类的方法
# django3.1 新增了elif not py_script.exists() 导致runserver 启动不了
# get_child_arguments修改为django 2.2 中的方式
django.utils.autoreload.get_child_arguments = get_child_arguments

# django3.1 中 DEFAULT_PASSWORD_LIST_PATH 使用 Path.resolve(strict=True)
# 导致打包后指定的路径不存在文件报错.
# 去掉strict=True后不会再校验路径是否存在文件
# 这个在django 3.1.2已经修改了
# password_validation.CommonPasswordValidator.DEFAULT_PASSWORD_LIST_PATH = Path(
#    password_validation.__file__).resolve().parent / 'common-passwords.txt.gz'

_old_restart_with_reloader = django.utils.autoreload.restart_with_reloader


def _restart_with_reloader(*args):
    import sys
    a0 = sys.argv.pop(0)
    try:
        return _old_restart_with_reloader(*args)
    finally:
        sys.argv.insert(0, a0)


# Override get_commands() function otherwise the app will complain that
# there are no commands.
django.core.management.get_commands = _get_commands
# Override restart_with_reloader() function otherwise the app might
# complain that some commands do not exist. e.g. runserver.
django.utils.autoreload.restart_with_reloader = _restart_with_reloader
