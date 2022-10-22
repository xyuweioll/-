import pandas as pd
import os.path
import win32com.client as win32
import openpyxl
from openpyxl.utils import get_column_letter
import re
# ===============================================================
# 格式转换
a = input("是否保留原格式文件？不保留请输入 1/保留 2\n--->>")
b = int(a)
os.chdir(r'G:\全国肺结核_20220526\报告数据')
rootdir = r'G:\全国肺结核_20220526\报告数据'  # 存放文件的根目录
#三个参数：父目录；所有文件夹名（不含路径）；所有文件名
for parent, dirnames, filenames in os.walk(rootdir):
    for fn in filenames:
        if os.path.splitext(fn)[1] == '.xls':  # 判断文件扩展名是不是为.xlsx  os.path.splitext(“文件路径”)
            print(fn)
            filedir = os.path.join(parent, fn)  # os.path.join是路径拼接函数，
            print(filedir)
            # excel = win32.gencache.EnsureDispatch('Excel.Application')   # 若报错则用下一条语句
            excel = win32.DispatchEx('Excel.Application')   # 若上一条报错则使用本条语句
            wb = excel.Workbooks.Open(filedir)  # 打开文件
            # xlsx: FileFormat=51
            # xls:  FileFormat=56,
            # 后缀名的大小写不通配，需按实际修改：xls，或XLS
            wb.SaveAs(filedir.replace('xls', 'xlsx'), FileFormat=51)  # 我这里原文件是小写的xls
            wb.Close()
            excel.Application.Quit()
    if b == 1:
        for fn in filenames:
            if os.path.splitext(fn)[1] == '.xls':  # 判断文件扩展名是不是为.xlsx  os.path.splitext(“文件路径”)
                filedir = os.path.join(parent, fn)  # os.path.join是路径拼接函数，
                os.remove(filedir)
                print(filedir)
print('格式转换完成！')

# ==========================================================================
for parent, dirnames, filenames in os.walk(rootdir):
    for fn in filenames:
        print(fn)
        if os.path.splitext(fn)[1] == '.xlsx':  # 判断文件扩展名是不是为.xlsx  os.path.splitext(“文件路径”)
            file_op = pd.read_excel(fn)
            file_op.drop([0, 1], axis=0, inplace=True)  # 删除前两行
            file_op.rename(columns={'Unnamed: 0': '无名列', 'Unnamed: 1': '地区',
                                    'Unnamed: 2': '仅阳培发病数', 'Unnamed: 3': '仅阳培死亡数', 'Unnamed: 4': '仅阳培发病率', 'Unnamed: 5': '仅阳培死亡率',
                                    'Unnamed: 6': '未痰检发病数', 'Unnamed: 7': '未痰检死亡数', 'Unnamed: 8': '未痰检发病率', 'Unnamed: 9': '未痰检死亡率',
                                    'Unnamed: 10': '涂（+）发病数', 'Unnamed: 11': '涂（+）死亡数', 'Unnamed: 12': '涂（+）发病率', 'Unnamed: 13': '涂（+）死亡率',
                                    'Unnamed: 14': '肺结核发病数', 'Unnamed: 15': '肺结核死亡数', 'Unnamed: 16': '肺结核发病率', 'Unnamed: 17': '肺结核死亡率',
                                    'Unnamed: 18': '菌（-）发病数', 'Unnamed: 19': '菌（-）死亡数', 'Unnamed: 20': '菌（-）发病率', 'Unnamed: 21': '菌（-）死亡率',}, inplace=True)
            lie_num = file_op.shape[1]  # 获取列数
            hang_num = file_op.shape[0]  # 获取行数
            # file_op.drop([hang_num-1, hang_num-2], axis=0, inplace=True)  # 删除最后一行
            time_lable = [str(os.path.splitext(fn)[0][0:4])] * (hang_num)  # 添加时间标签
            file_op['年份'] = time_lable
            file_op.to_excel(fn, index=False)






