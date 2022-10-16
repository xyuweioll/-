# import pandas as pd
# import os.path
# import win32com.client as win32
# import openpyxl
# from openpyxl.utils import get_column_letter
# import re
#
# a = input("是否保留原格式文件？不保留请输入 1/保留 2\n--->>")
# b = int(a)
# rootdir = r'C:\Users\xianyu\Desktop\全部'  # 存放文件的根目录
# # 三个参数：父目录；所有文件夹名（不含路径）；所有文件名
# for parent, dirnames, filenames in os.walk(rootdir):
#     for fn in filenames:
#         if os.path.splitext(fn)[1] == '.xls':  # 判断文件扩展名是不是为.xlsx  os.path.splitext(“文件路径”)
#             print(fn)
#             filedir = os.path.join(parent, fn)  # os.path.join是路径拼接函数，
#             print(filedir)
#             # excel = win32.gencache.EnsureDispatch('Excel.Application')   # 若报错则用下一条语句
#             excel = win32.DispatchEx('Excel.Application')   # 若上一条报错则使用本条语句
#             wb = excel.Workbooks.Open(filedir)  # 打开文件
#             # xlsx: FileFormat=51
#             # xls:  FileFormat=56,
#             # 后缀名的大小写不通配，需按实际修改：xls，或XLS
#             wb.SaveAs(filedir.replace('xls', 'xlsx'), FileFormat=51)  # 我这里原文件是小写的xls
#             wb.Close()
#             excel.Application.Quit()
#     if b == 1:
#         for fn in filenames:
#             if os.path.splitext(fn)[1] == '.xls':  # 判断文件扩展名是不是为.xlsx  os.path.splitext(“文件路径”)
#                 filedir = os.path.join(parent, fn)  # os.path.join是路径拼接函数，
#                 os.remove(filedir)
#                 print(filedir)
# print('格式转换完成！')
# #  ====================================================================================================================
# # # ----
# a = []
# for parent, dirnames, filenames in os.walk(rootdir):
#     for i in filenames:
#         if os.path.splitext(i)[1] == '.xlsx':  # 判断文件扩展名是不是为.xlsx  os.path.splitext(“文件路径”)
#             b = len(i)-5
#             a.append(i[:b])  # 这个循环的作用是去除后缀.xlsx（即去除后五个字符）
#         print(a)
#     # 这一部分实现单元格拆分
#     for i in filenames:
#         if os.path.splitext(i)[1] == '.xlsx':  # 判断文件扩展名是不是为.xlsx  os.path.splitext(“文件路径”)
#             filedir = os.path.join(parent, i)
#             data = pd.read_excel(filedir)
#             data.fillna(method='ffill', inplace=True)
#             data.to_excel(filedir, index=False)
#             print(f'{i}单元格拆分已完成！')
# # ====================================================================================================
#
#     for i in range(len(filenames)):
#         if os.path.splitext(filenames[i])[1] == '.xlsx':  # 判断文件扩展名是不是为.xlsx  os.path.splitext(“文件路径”)
#             filedir = os.path.join(parent, filenames[i])  # os.path.join是路径拼接函数
#             print(filedir)
#             wb = openpyxl.load_workbook(filedir)
#             #ws = wb[a[i]]
#             ws = wb['Sheet1']
#             ws.delete_rows(1)  # 删除第一行
#             wb.save(filedir)
# import re
# def date_number(date_list):  # 传入字符串，如：2001,01:2020,12  返回值为时间间隔列表
#     date_list = re.split(r'[,:]\s*', date)
#     date_list = [int(i) for i in date_list]
#     month_number = (date_list[2] - date_list[0]) * 12 + (date_list[3] - date_list[1]) + 1  # d的数值是两个日期之间包含的月数
#     e = []
#     if date_list[0] == date_list[2]:
#         for i in range(date_list[1], date_list[3] + 1):
#             if i < 10:
#                 e.append(str(date_list[0]) + '0' + str(i))
#             else:
#                 e.append(str(date_list[0]) + str(i))
#     else:
#         for i in range(date_list[1], 13):
#             if i < 10:
#                 e.append(str(date_list[0]) + '0' + str(i))
#             else:
#                 e.append(str(date_list[0]) + str(i))
#     for i in range(date_list[0] + 1, date_list[2]):
#         for j in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
#             e.append(str(i) + j)
#     if date_list[0] != date_list[2]:
#         for i in range(1, date_list[3] + 1):
#             if i < 10:
#                 e.append(str(date_list[2]) + '0' + str(i))
#             else:
#                 e.append(str(date_list[2]) + str(i))
#     return e
# date = input("请输入日期\n（输入示例：如2001年6月至2020年4月：2001,06:2020,04）===>>>")
#
# date_number_list = date_number(date)
# print(date_number_list)
# pyecharts 共有四种地理图标，
# Map：地图
# Geo：地理坐标系
# Bmap：百度地图
# Map3D：三维地图
from pyecharts.charts import Map
from pyecharts import options as opts

# from pyecharts.charts import Bar
#
# attr = ["{}月".format(i) for i in range(1, 13)]
# v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
# v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# bar = Bar("柱状图示例")
# bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
# bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"])
# bar.show_config()
# bar.render(path='./data/02-多标记柱形图.html')

# dct = {'Name': 'Alice', 'Age': 18, 'uid': 1001, 'id': 1001}
# print(dct['Name'])
# dct = {'安徽': 'Anhui', '澳门': 'Macao', '北京': 'Beijing', '福建': 'Fujian', '甘肃': 'Gansu', '广东': 'Guangdong',
#        '广西': 'Guangxi', '贵州': 'Guizhou', '海南': 'Hainan', '河北': 'Hebei', '河南': 'Henan', '黑龙江': 'Heilongjiang',
#        '湖北': 'Hubei', '湖南': 'Hunan', '吉林': 'Jilin', '江苏': 'Jiangsu', '江西': 'Jiangxi', '辽宁': 'Liaoning',
#        '内蒙古': 'Inner Mongolia', '宁夏': 'Ningxia', '青海': 'Qinghai', '山东': 'Shandong', '山西': 'Shanxi',
#        '陕西': 'Shaanxi', '上海': 'Shanghai', '四川': 'Sichuan', '台湾': 'Taiwan', '天津市': 'Tianjin', '西藏': 'Tibet',
#        '香港': 'Hong Kong', '新疆': 'Xinjiang', '云南': 'Yunnan', '浙江': 'Zhejiang', '重庆': 'Chongqing'}


def eng_name(chinese_name):
    province_name = {'安徽': 'Anhui', '澳门': 'Macao', '北京': 'Beijing', '福建': 'Fujian', '甘肃': 'Gansu', '广东': 'Guangdong',
                     '广西': 'Guangxi', '贵州': 'Guizhou', '海南': 'Hainan', '河北': 'Hebei', '河南': 'Henan',
                     '黑龙江': 'Heilongjiang', '湖北': 'Hubei', '湖南': 'Hunan', '吉林': 'Jilin', '江苏': 'Jiangsu',
                     '江西': 'Jiangxi', '辽宁': 'Liaoning', '内蒙古': 'Inner Mongolia', '宁夏': 'Ningxia', '青海': 'Qinghai',
                     '山东': 'Shandong', '山西': 'Shanxi', '陕西': 'Shaanxi', '上海': 'Shanghai', '四川': 'Sichuan',
                     '台湾': 'Taiwan', '天津市': 'Tianjin', '西藏': 'Tibet', '香港': 'Hong Kong', '新疆': 'Xinjiang',
                     '云南': 'Yunnan', '浙江': 'Zhejiang', '重庆': 'Chongqing'}
    return province_name[chinese_name] if chinese_name in province_name else 'None'
print(eng_name('内蒙古'))
print(type(eng_name('内蒙古')))