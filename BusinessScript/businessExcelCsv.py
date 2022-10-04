# -*- codeing = utf-8 -*-
# @Time: 2022/9/17 11:10
# @Author: xiaowo
# @File：businessExcelCsv.py
# @Software：PyCharm
import csv
import os

from Base.basePath import BasePath
from Base.baseExcel import BaseExcel

"""
该文件存放处理excel文件业务需求的步骤
下边举了一个例子，get_data_from_excels + insert_data_to_csv：将excel获取的数据存入csv中
"""
class BusinessExcelCsv(object):

    def __init__(self):
        self.Excel = BaseExcel()
        self.ExcelFiles = BasePath.EXCELFILES
        self.CsvFiles = BasePath.CSVFILES
        self.Header = ["testdata"]

    """
    读取Excel数据到
    :param path: 文件夹路径
    :return: 读取到的数据-tables
    """
    def get_data_from_excels(self, path):
        tables = []
        filelist = os.listdir(path)
        if(len(filelist) > 0):
            for file in filelist:#针对不止一个xlsx文件情况
                list = []  # CSV文件内容
                data = self.Excel.read_key_value_Excel(os.path.join(path,file),0)
                list.append(data[0].get("testdata"))
                tables.append(list)
                print("【{}】文件数据已载入tables".format(file))
        return tables


    """
    将Excel读取到的数据,写入到CSV文件
    :param filepath: 文件路径
    :param tables: 插入的数据
    :return:
    """
    def insert_data_to_csv(self, filename, tables):
        #指定文件对象
        f = open(os.path.join(BasePath.CSVFILES,filename),"w",encoding="utf-8",newline="")
        csv_writer = csv.writer(f) #基于稳健对象构建csv写入对象
        # 构建列表头
        f.truncate()
        csv_writer.writerow(self.Header)
        # 写入csv文件内容
        for data in tables:
            csv_writer.writerow(data)
            print("csv文件写入tables数据{}成功".format(data))
        f.close()
        return True

    """
    清除csv文件全部数据
    :param filepath: CSV文件路径
    :return:
    """
    def delete_data_csv(self, filename):
        #指定文件对象
        f = open(os.path.join(BasePath.CSVFILES,filename),"w",encoding="utf-8",newline="")
        #删除文件所有数据
        f.truncate()
        f.close()
        print("【{}】文件数据全部清除成功".format(filename))



if __name__ == '__main__':
    xx = BusinessExcelCsv()
    tables = xx.get_data_from_excels(BasePath.EXCELFILES)
    xx.insert_data_to_csv("test.csv",tables)
    # xx.delete_data_csv("auto-confirm-test-latest.csv")