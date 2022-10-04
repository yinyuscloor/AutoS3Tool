# -*- codeing = utf-8 -*-
# @Time: 2022/9/8 19:44
# @Author: jiadong
# @File：utils.py
# @Software：PyCharm

import os
from configparser import RawConfigParser
from Base.basePath import BasePath

def read_config_ini(configpath):
    '''读取ini文件'''
    config = RawConfigParser() #内置读取config配置文件方法
    config.read(configpath,encoding='utf-8')
    return config

def delete_all_in_folder(folderpath):
    '''删除目标文件夹下的所有文件'''
    filelist = os.listdir(folderpath)
    for file in filelist:
        os.remove(folderpath + file) # 该命令删除文件
        print("【{}】文件已删除".format(file))




if __name__ == "__main__":
    delete_all_in_folder(BasePath.S3FILES)