# -*- codeing = utf-8 -*-
# @Time: 2022/9/8 21:59
# @Author: xiaowo
# @File：demandScript.py
# @Software：PyCharm
import os
import time

from BusinessScript.businessS3 import BusinessS3
from BusinessScript.businessExcelCsv import BusinessExcelCsv
from Base.basePath import BasePath

class DemandScript(object):

    def __init__(self):
        self.s3 = BusinessS3()
        self.excelcsv = BusinessExcelCsv()
        self.path = BasePath()

    """
    具体需求1：
    S3文件下载进行修改，然后上传
    :param download_path: 下载文件的目录路径(注：该目录下即是文件)
    :param upload_path: 上传文件至S3的目录路径(注：该目录下即是文件)
    :return: 打印输出
    """
    def auto_download_ammend_upload(self,download_path,upload_path):
        self.s3.delete_all_S3Files()
        self.s3.download_file_to_S3FILES(download_path)
        self.s3.add_prefix_suffix(".word")
        self.s3.ammend_suffix("test","hello")
        time.sleep(1)#暂停1秒
        self.s3.upload_file_to_s3(upload_path)


    """
    具体需求2：
    将excel文件信息提取到csv文件并上传
    :param upload_path: 上传文件至S3的目录路径(注：该目录下即是文件)
    :return: 打印输出
    """
    def excel_demand_upload(self,csvname,upload_path):
        self.excelcsv.delete_data_csv(csvname)#先清空csv
        tables = self.excelcsv.get_data_from_excels(self.path.EXCELFILES)
        self.excelcsv.insert_data_to_csv(csvname,tables)
        self.s3.upload_file_to_s3(upload_path)



if __name__ == '__main__':
    pass
