import pandas as pd
import os
# 处理的思想就是将每一个月的平均值/累计值计算出来后赋值给对应月份的1日，然后再将每个月1日的数据提取出来即可得到月数据
rootdir = u'D:\\Climate\\SELECT-FIX'  # 存放文件的根目录
out_fold = 'D:\\Climate\\SELECT-FIX-LL_20220301\\'
read_list = []
for parent, dirnames, filenames in os.walk(rootdir):   # 此时filenames 是一个存放了所有文件名的列表
    print(filenames)
    for fn in filenames:
        filedir = os.path.join(parent, fn)  # os.path.join是路径拼接函数，
        read_list.append(filedir)
for num in range(len(filenames)):
    print(f'正在读取:{read_list[num]}')
    select = pd.read_csv(read_list[num], encoding='utf-8')  # 读取文件
    print('读取完成')
    number_index = len(select)  # 计算行数
    for i in range(number_index):
        last_2 = float(str(select['维度'][i])[2:4]) / 60  # 维度后两位 分转度
        first_2 = float(str(select['维度'][i])[:2])  # 取维度前两位
        lat = first_2 + last_2
        print(lat)
        select.loc[[i], ['维度']] = lat  # 对相应位置上的维度值进行重新赋值
    print('经度转换已完成！')
    # 经度转换：经度有大于100度的可能，需要进行一次判断
    for i in range(number_index):
        if select['经度'][i] >= 10000:  # 即经度大于100度的情况
            last_2 = float(str(select['经度'][i])[3:5]) / 60
            first_3 = float(str(select['经度'][i])[:3])
            lon = first_3 + last_2
            select.loc[[i], ['经度']] = lon  # 对相应位置上的经度值进行重新赋值
            print(lon)
        else:
            last_2 = float(str(select['经度'][i])[2:4]) / 60
            first_2 = float(str(select['经度'][i])[:2])
            lon = first_2 + last_2
            select.loc[[i], ['经度']] = lon  # 对相应位置上的经度值进行重新赋值，note:对一列数据赋值一个不同数据类型的数据会改变整列的数据类型
            print(lon)
    print('维度转换已完成！')
    OUT = out_fold + filenames[num]
    select.to_csv(OUT, index=False)
    print(f'{filenames[num]}已输出！')
