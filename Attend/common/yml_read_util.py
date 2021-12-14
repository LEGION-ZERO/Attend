# -*- coding: utf-8 -*-
import os
import sys

global_conf = {}


# 根据文件路径读取yml配置的方法,返回字典类型
def read_yml(file_name: str):
    import yaml
    with open(file_name, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


# 根据对应的文件名去etc目录寻找对应的配置
# 规则:1. 先从etc/项目文件夹/中去找对应的文件，找到即用那个配置文件(application.yml除外)
#      2. 未找到时读取etc下的对应的文件
#      3. application.yml只会去etc下读取
def read_base_path(file_name: str):
    # 默认文件路径: etc下
    file_path = os.path.join(app_path(), "etc", file_name)
    # 不是pyinstaller打包环境,不是application的配置时,需要从另外的文件中读取配置
    if not is_installer_env() and file_name != "application.yml":
        support_item = get_config_from_file("application.yml", "application.support-item", "system")
        curr_path = os.path.join(app_path(), "etc", support_item, file_name)
        if os.path.exists(curr_path):
            # 项目专属文件夹存在该文件时，将文件路径改到专属路径下
            file_path = curr_path
    # file_path = os.path.join(app_path(), "etc", file_name)
    if not os.path.exists(file_path):
        # logging.warning("file: [ %s ] not exist!", file_path)
        return None
    result_config = read_yml(file_path)
    return result_config


# conf_dict:配置信息的字典对象: {"parent":{"child": "value" }}
# config_key:需要读取配置的key。用 "." 号表示字典对象中的下一层: 使用parent.child读取上述child中的值
# default_vale: 没有找到对应的key时返回的默认值
def get_value_from_dict(conf_dict, config_key, default_value, root_key):
    key_list = str(config_key).split(".")
    first_key = key_list[0]
    if first_key not in conf_dict:
        # logging.warning("not found key [ %s ] in config, use default value: [ %s ] ", root_key, default_value)
        return default_value
    # 最后一个
    if key_list[-1] == first_key:
        # logging.info("found key [%s] in config.value [ %s ]", root_key, conf_dict[first_key])
        return conf_dict[first_key]
    # 不是最后一个,需要在查找
    next_find_conf = conf_dict[first_key]
    if type(next_find_conf) != dict:
        # logging.warning("found key:[ %s ] type is error!,use default value:[ %s ]", root_key, default_value)
        return default_value
    return get_value_from_dict(next_find_conf, ".".join(key_list[1:]), default_value, root_key)


# file_name: 配置信息所在的文件名
# config_key: 需要读取的key
# default_value: 未读取到时返回的默认值
def get_config_from_file(file_name, config_key, default_value):
    if not file_name in global_conf:
        # logging.info("first load file: [ %s ]", file_name)
        conf = read_base_path(file_name)
        if not conf:
            # logging.warning("file:[ %s ]  not exist! use default value:[ %s ] for key:[ %s ]", file_name, default_value,
            #                config_key)
            return default_value
        global_conf[file_name] = conf
    conf_dict = global_conf[file_name]
    return get_value_from_dict(conf_dict, config_key, default_value, config_key)


# 获取文件所在路径的方法
# 打包后返回manage二进制文件所在路径
# 未打包返回yml_read_util.py文件所在的路径
# 这样调用 os.path.join(app_path(),"etc")就打包前后都能读到配置文件
def app_path():
    """Returns the base application path."""
    import sys
    if hasattr(sys, 'frozen'):
        # 打包后,当前执行程序所在路径
        return os.path.dirname(sys.executable)
    # 未打包,该py文件所在路径
    return os.path.dirname(__file__)


# 是否是打包后的运行环境
def is_installer_env():
    # pyinstaller打包后, 会将frozen注入到sys中
    # 如果sys中没有该属性，可以认为没有进行pyinstaller打包
    return hasattr(sys, 'frozen')


if __name__ == '__main__':
    print(get_config_from_file("pqa-make-data.yml", "pqa-make-data.day-num", 123))
