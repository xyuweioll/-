import pandas as pd
import numpy as np
from pandas import DataFrame
from openpyxl import Workbook
data = pd.read_excel("C:\\Users\\xianyu\\Desktop\\东北Satscan\\12-16东北地区处理前.xlsx", sheet_name='Sheet1')
a = data['市']  # 获取地方名
b = data['市代码']  # 获取地方ID，此时a、b的数据类型为series,可以当成列表处理
c = []
for i in range(len(a)):
    xuan_hang = [i]  # 获取特定行的数据，i为行数
    d = data.iloc[xuan_hang, 243:]  # print(c)#获取特定行中的一些列,但此时d还是一个DataFrame数据类型
    d_array = np.array(d)   # 将DataFrame转换成array
    d_list = d_array.tolist()  # 将array 转换成列表
    c.extend(d_list)  # 将列表合并,此时列表中的元素还是一个列表，每一个列表是一个市的病例数
d = []
for i in c:
    d.extend(i)  # 实现将列表里的列表合并成一个大列表，元素是单个数值，此时d为人口数的列表
print(d)
e = []
for i in range(len(d)):
    if i==0 or i%20==0:
        for j in range(8):
            e.append(d[i])
    else:
        for j in range(12):
            e.append(d[i])  # 这个循环是将每一年的人口重复12遍；此时e就是所需要的人口列表
print(e)
print(len(e))


year = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
data = ['2001/05', '2001/06', '2001/07', '2001/08', '2001/09', '2001/10', '2001/11', '2001/12']

for k in year:
    for l in month:
        m = str(k) + '/' + l
        data.append(m)  # 列表data 是日期列表
data = data*36   # 36是城市个数

# #创建excel表格
wb = Workbook()  # 创建一个Workbook，表名默认为Sheet
ws = wb.active  # 激活一张表格,因为此时只有一张表格，默认为Sheet,激活表格后若不选表格则默认操作激活表格
# ws = wb["Sheet"]  #选中某一张特定表格
print("默认创建的sheet名", ws.title)
ws.append(['NAME', 'CITY_CODE', 'POP', 'DATE'])
f = 0
for i in range(len(a)):
    for j in range(236):   # 月数
        ws.append([a[i], b[i], e[f], data[f]])
        f += 1
wb.save("C:\\Users\\xianyu\\Desktop\\SaTScan1-pop.xlsx")