import pandas as pd
import os
read_1 = pd.read_csv(r'D:\Climate\SELECT\地温(GST)-2017.csv')
code_list = read_1['区站号'].drop_duplicates()  # 获取站点号并去除重复值
for field in ['平均地表气温', '日最高地表气温', '日最低地表气温']:
    for month in range(1, 13):
        for site_code in code_list:
            try:
                avg = sum(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)][field]) / \
                      len(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)])  # 计算一个站点一个月的平均地表温度，浮点型数据
                read_1.loc[(read_1['月'] == month) & (read_1['区站号'] == site_code) & (read_1['日'] == 1), [field]] = avg
            except:
                print(f'文件中{month}没有{site_code}的数据！')
    print(f'字段{field}已计算完成！')

select = read_1[(read_1['日'] == 1)][
    ['省份', '站名', '区站号', '维度', '经度', '观测场海拔高度', '年', '月', '平均地表气温', '日最高地表气温', '日最低地表气温']]
select.reset_index(inplace=True)
select.drop(columns=['index'], inplace=True)
print('程序段1-1已执行结束！')
# ==================================================================================================================================================
# 经纬度转换
# 维度转换
number_index = len(select)  # 计算行数
for i in range(number_index):
    last_2 = float(str(select['维度'][i])[2:4]) / 60  # 维度后两位 分转度
    first_2 = float(str(select['维度'][i])[:2])  # 取维度前两位
    lat = first_2 + last_2
    select.loc[[i], ['维度']] = lat  # 对相应位置上的维度值进行重新赋值
print('经度转换已完成！')
# 经度转换：经度有大于100度的可能，需要进行一次判断
for i in range(number_index):
    if select['经度'][i] >= 10000:  # 即经度大于100度的情况
        last_2 = float(str(select['经度'][i])[3:5]) / 60
        first_3 = float(str(select['经度'][i])[:3])
        lon = first_3 + last_2
        select.loc[[i], ['经度']] = lon  # 对相应位置上的经度值进行重新赋值
        # print(lon)
    else:
        last_2 = float(str(select['经度'][i])[2:4]) / 60
        first_2 = float(str(select['经度'][i])[:2])
        lon = first_2 + last_2
        select.loc[[i], ['经度']] = lon  # 对相应位置上的经度值进行重新赋值，note:对一列数据赋值一个不同数据类型的数据会改变整列的数据类型
        # print(lon)
print('维度转换已完成！')
select.to_csv('D:\Climate\SELECT-month\地温(GST)-2017.csv', index=False)
print(f'已输出！')
