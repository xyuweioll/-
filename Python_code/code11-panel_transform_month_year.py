'''
本程序适用以年/月为单位的平衡面板数据的生成，平衡可以理解为每个研究因素在每一年每个研究区域都有具体的数值
研究区域，研究因素，研究年/月份可以对应上。
'''
import pandas as pd
import numpy as np
import os
file_path = input('请输入待处理文件的路径及名称：如：G:\\\\Artical-1\\\\Satscan\\\\待处理文件.xlsx\n===>>>')
if os.path.splitext(file_path)[1] =='.xlsx' or os.path.splitext(file_path)[1] =='.xls':
    sheet_name = input('请输入表名\n===>>>')
    data = pd.read_excel(file_path, sheet_name=sheet_name)
else:
    data = pd.read_csv(file_path)
start_col = int(input('请输入待处理因素开始列数，并确保各因素列间无其他无关列\n请直接输入阿拉伯数字===>>>'))
# ========================================================================================================
data_type = input('您处理的数据若是以年为单位请输入 Y  若是以月为单位请输入 M\n=====>>>')
if data_type == 'M':
    start_m = input('请输入开始年月，如2020年1月就输入: 2020/01\n=====>>>')
    stop_m = input('请输入结束年月，如2020年12月就输入: 2020/12\n=====>>>')
    rng = pd.date_range(start_m, stop_m, freq='MS')
    day_index = [str(i)[:4]+str(i)[5:7] for i in rng] # 生成日期索引的列表，数据类型为字符串
elif data_type == 'Y':
    start_y = input('请输入开始年，如2010年就输入: 2010\n=====>>>')
    stop_y = input('请输入结束年，如2020年就输入: 2020\n=====>>>')
    rng = pd.date_range(start_y, stop_y, freq='YS')
    day_index = [str(i)[:4] for i in rng]  # 生成日期索引的列表，数据类型为字符串
print(day_index)
data_num = len(day_index)
# =========================================================================================================
# 定义函数
def factor_list (para1, para2, para3 ):     # 参数1对于的数据框数据，2开始列, 3间隔
    c = []
    for i in range(len(para1)):
        xuan_hang = [i]  # 获取特定行的数据，i为行数
        d = data.iloc[xuan_hang, para2-1:para2+para3-1]   # 两个参数分别为气象数据开始的列数和结束的列数+1  print(c)#获取特定行中的一些列,但此时d还是一个DataFrame数据类型
        d_array = np.array(d)  # 将DataFrame转换成array
        d_list = d_array.tolist()  # 将array 转换成列表
        c.extend(d_list)  # 将列表合并,此时列表中的元素还是一个列表，每一个列表是一个县的气象数据值
    d = []  # 存放气象数据
    for i in c:
        d.extend(i)  # 实现将列表里的列表合并成一个大列表，元素是单个数值，此时d为气象数据分年/月、分县排列的列表
    return d     # 返回列表，列表是分地分年待处理数据的列表
# =========================================================================================================
total_col = data.shape[1]     # 获取总列数
total_row = data.shape[0]     # 获取列表总行数，行数即城市个数
factorlist = []   # 用来生成dataframe的数据列表
colname_list = ['PLACE', 'Date']  # 用来生成dataframe的列名
label_name = []   # 中间列表，只起到临时存放作用
a = np.array(data.iloc[:, 1:2].values).tolist()  # 获取第二列的值并转成列表,但此时列表元素还是列表
[label_name.extend(i) for i in a]  # 此时label_name是各地方的名字
list_name_after = [val for val in label_name for i in range(data_num)]   # 生成的名列表
print(list_name_after)
print(f"地名列表中共有{len(list_name_after)}个元素！")
factorlist.append(list_name_after)
print(factorlist)
print('地名列表已生成！')
# ================================================================================================
time_label = day_index*total_row  # 生成年份标签
factorlist.append(time_label)
print(time_label)
print(f"时间列表中共有{len(time_label)}个元素！")
print(factorlist)
print('时间列表已生成！')
# =================================================================================================
data_col_name = data.columns.tolist()   # 获取列名并生成列表
print(f"列名列表:{data_col_name}")
for ii in range(start_col, total_col+1, data_num):
    factorlist.append(factor_list(data, ii, data_num))      # 此处使用函数,将
    colname_list.append(data_col_name[ii-1])
print(f'新生成数据框的列名列表：{colname_list}')
print(f"新生成的数据框共有{len(colname_list)}列!")
print(f"factorlist中有：{len(factorlist)}个元素")
data_after = pd.DataFrame()   # 定义一个空dataframe
for i in range(len(colname_list)):
    data_after[colname_list[i]] = factorlist[i]
print(data_after)
data_after.to_csv('G:\\2010-2020安徽省面板数据1.csv', index=False)
print('程序执行完毕！')




