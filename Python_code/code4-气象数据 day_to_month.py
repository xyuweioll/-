import pandas as pd
import os
# 处理的思想就是将每一个月的平均值/累计值计算出来后赋值给对应月份的1日，然后再将每个月1日的数据提取出来即可得到月数据
rootdir = u'D:\\Climate\\SELECT-FIX'  # 存放文件的根目录
out_fold = 'D:\\Climate\\SELECT-month-FIX\\'   # 输出文件目录
read_list = []
for parent, dirnames, filenames in os.walk(rootdir):   # 此时filenames 是一个存放了所有文件名的列表
    for fn in filenames:
        filedir = os.path.join(parent, fn)  # os.path.join是路径拼接函数，
        read_list.append(filedir)
        print(filedir)
# =================================================================================================================
# 地温-求月平均
for num in range(len(filenames)):
    if filenames[num][:2] == '地温':
        read_1 = pd.read_csv(read_list[num])  # 读取文件
        print(f'{filenames[num]}已经成功读取！')
        code_list = read_1['区站号'].drop_duplicates()    # 获取站点号并去除重复值
        for field in ['平均地表气温', '日最高地表气温', '日最低地表气温']:
            for month in range(1, 13):
                for site_code in code_list:
                    try:
                        avg = sum(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)][field])/\
                              len(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)])  # 计算一个站点一个月的平均地表温度，浮点型数据
                        read_1.loc[(read_1['月'] == month) & (read_1['区站号'] == site_code) & (read_1['日'] == 1), [field]] = avg
                    except:
                        print(f'{filenames[num]}文件中{month}没有{site_code}的数据！')
            print(f'字段{field}已计算完成！')

        select = read_1[(read_1['日'] == 1)][['省份', '站名', '区站号', '维度', '经度', '观测场海拔高度', '年', '月', '平均地表气温', '日最高地表气温', '日最低地表气温']]
        select.reset_index(inplace=True)
        select.drop(columns=['index'], inplace=True)
        print('程序段1-1已执行结束！')
        # ==================================================================================================================================================
        # 经纬度转换
        # 维度转换
        number_index = len(select)  # 计算行数
        for i in range(number_index):
            last_2 = float(str(select['维度'][i])[2:4])/60  # 维度后两位 分转度
            first_2 = float(str(select['维度'][i])[:2])     # 取维度前两位
            lat = first_2+last_2
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
        OUT = out_fold+filenames[num]
        select.to_csv(OUT, index=False)
        print(f'{filenames[num]}已输出！')
# ==============================================================================================
# ===============================================================================================
# #降水-求和
    elif filenames[num][:2] == '降水':
        print(f'{filenames[num]}读取成功！')
        read_1 = pd.read_csv(read_list[num])  # 读取文件
        code_list = read_1['区站号'].drop_duplicates()  # 获取站点号并去除重复值
        for field in ['20-8时降水量', '8-20时降水量', '20-20时累计降水量']:
            for month in range(1, 13):
                for site_code in code_list:
                    try:
                        avg = sum(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)][field])  # 浮点型数据
                        read_1.loc[
                            (read_1['月'] == month) & (read_1['区站号'] == site_code) & (read_1['日'] == 1), [field]] = avg
                    except:
                        print(f'{filenames[num]}文件中{month}没有{site_code}的数据！')
            print(f'字段{field}已计算完成！')

        select = read_1[(read_1['日'] == 1)][['省份', '站名', '区站号', '维度', '经度', '观测场海拔高度', '年', '月', '20-8时降水量', '8-20时降水量', '20-20时累计降水量']]
        select.reset_index(inplace=True)
        select.drop(columns=['index'], inplace=True)
        print('程序段1已执行结束！')
        # ==================================================================================================================================================
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
        OUT = out_fold + filenames[num]
        select.to_csv(OUT, index=False)
        print(f'{filenames[num]}已输出！')
# # ==============================================================================================================
# # ==============================================================================================================
#  气压
    elif filenames[num][:2] == '气压':
        print(f'{filenames[num]}读取成功！')
        read_1 = pd.read_csv(read_list[num])  # 读取文件
        code_list = read_1['区站号'].drop_duplicates()  # 获取站点号并去除重复值
        for field in ['平均本站气压', '日最高本站气压', '日最低本站气压']:
            for month in range(1, 13):
                for site_code in code_list:
                    try:
                        avg = sum(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)][field]) / \
                              len(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)])  # 浮点型数据
                        read_1.loc[
                            (read_1['月'] == month) & (read_1['区站号'] == site_code) & (read_1['日'] == 1), [field]] = avg
                    except:
                        print(f'{filenames[num]}文件中{month}没有{site_code}的数据！')
            print(f'字段{field}已计算完成！')

        select = read_1[(read_1['日'] == 1)][['省份', '站名', '区站号', '维度', '经度', '观测场海拔高度', '年', '月', '平均本站气压', '日最高本站气压', '日最低本站气压']]
        select.reset_index(inplace=True)
        select.drop(columns=['index'], inplace=True)
        print('程序段1已执行结束！')
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
        OUT = out_fold + filenames[num]
        select.to_csv(OUT, index=False)
        print(f'{filenames[num]}已输出！')

# =================================================================================================================
# =================================================================================================================
#  日照
    elif filenames[num][:2] == '日照':
        print(f'{filenames[num]}读取成功！')
        read_1 = pd.read_csv(read_list[num])  # 读取文件
        code_list = read_1['区站号'].drop_duplicates()  # 获取站点号并去除重复值
        for field in ['日照时数']:
            for month in range(1, 13):
                for site_code in code_list:
                    try:
                        avg = sum(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)][field]) / \
                              len(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)])  # 浮点型数据
                        read_1.loc[
                            (read_1['月'] == month) & (read_1['区站号'] == site_code) & (read_1['日'] == 1), [field]] = avg
                    except:
                        print(f'{filenames[num]}文件中{month}没有{site_code}的数据！')
            print(f'字段{field}已计算完成！')

        select = read_1[(read_1['日'] == 1)][['省份', '站名', '区站号', '维度', '经度', '观测场海拔高度', '年', '月', '日照时数']]
        select.reset_index(inplace=True)
        select.drop(columns=['index'], inplace=True)
        print('程序段1已执行结束！')
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
        OUT = out_fold + filenames[num]
        select.to_csv(OUT, index=False)
        print(f'{filenames[num]}已输出！')
# =================================================================================================================
# =================================================================================================================
#  温度
    elif filenames[num][:2] == '温度':
        print(f'{filenames[num]}读取成功！')
        read_1 = pd.read_csv(read_list[num])  # 读取文件
        code_list = read_1['区站号'].drop_duplicates()  # 获取站点号并去除重复值
        for field in ['平均气温', '日最高气温', '日最低气温']:
            for month in range(1, 13):
                for site_code in code_list:
                    try:
                        avg = sum(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)][field]) / \
                              len(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)])  # 浮点型数据
                        read_1.loc[
                            (read_1['月'] == month) & (read_1['区站号'] == site_code) & (read_1['日'] == 1), [field]] = avg
                    except:
                        print(f'{filenames[num]}文件中{month}没有{site_code}的数据！')
            print(f'字段{field}已计算完成！')

        select = read_1[(read_1['日'] == 1)][['省份', '站名', '区站号', '维度', '经度', '观测场海拔高度', '年', '月', '平均气温', '日最高气温', '日最低气温']]
        select.reset_index(inplace=True)
        select.drop(columns=['index'], inplace=True)
        print('程序段1已执行结束！')
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
        OUT = out_fold + filenames[num]
        select.to_csv(OUT, index=False)
        print(f'{filenames[num]}已输出！')
# =================================================================================================================
# =================================================================================================================
# 相对湿度
    elif filenames[num][:2] == '相对':
        print(f'{filenames[num]}读取成功！')
        read_1 = pd.read_csv(read_list[num])  # 读取文件
        code_list = read_1['区站号'].drop_duplicates()  # 获取站点号并去除重复值
        for field in ['平均相对湿度', '最小相对湿度(仅自记)']:
            for month in range(1, 13):
                for site_code in code_list:
                    try:
                        avg = sum(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)][field]) / \
                              len(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)])  # 浮点型数据
                        read_1.loc[
                            (read_1['月'] == month) & (read_1['区站号'] == site_code) & (read_1['日'] == 1), [field]] = avg
                    except:
                        print(f'{filenames[num]}文件中{month}没有{site_code}的数据！')
            print(f'字段{field}已计算完成！')

        select = read_1[(read_1['日'] == 1)][['省份', '站名', '区站号', '维度', '经度', '观测场海拔高度', '年', '月', '平均相对湿度', '最小相对湿度(仅自记)']]
        select.reset_index(inplace=True)
        select.drop(columns=['index'], inplace=True)
        print('程序段1已执行结束！')
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
        OUT = out_fold + filenames[num]
        select.to_csv(OUT, index=False)
        print(f'{filenames[num]}已输出！')

# =================================================================================================================
# =================================================================================================================
# 蒸发
    elif filenames[num][:2] == '蒸发':
        read_1 = pd.read_csv(read_list[num])  # 读取文件
        print(f'{filenames[num]}读取成功！')
        code_list = read_1['区站号'].drop_duplicates()  # 获取站点号并去除重复值
        for field in ['小型蒸发量', '大型蒸发量']:
            for month in range(1, 13):
                for site_code in code_list:
                    try:
                        avg = sum(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)][field]) / \
                              len(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)])  # 浮点型数据
                        read_1.loc[
                            (read_1['月'] == month) & (read_1['区站号'] == site_code) & (read_1['日'] == 1), [field]] = avg
                    except:
                        print(f'{filenames[num]}文件中{month}没有{site_code}的数据！')
            print(f'字段{field}已计算完成！')

        select = read_1[(read_1['日'] == 1)][['省份', '站名', '区站号', '维度', '经度', '观测场海拔高度', '年', '月', '小型蒸发量', '大型蒸发量']]
        select.reset_index(inplace=True)
        select.drop(columns=['index'], inplace=True)
        print('程序段1已执行结束！')
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
        print('纬度转换已完成！')
        OUT = out_fold + filenames[num]
        select.to_csv(OUT, index=False)
        print(f'{filenames[num]}已输出！')

# ==================================================================================================================
# ==================================================================================================================
# 蒸发
    elif filenames[num][:2] == '风向':
        read_1 = pd.read_csv(read_list[num])  # 读取文件
        print(f'{filenames[num]}读取成功！')
        code_list = read_1['区站号'].drop_duplicates()  # 获取站点号并去除重复值
        for field in ['平均风速', '最大风速', '极大风速']:
            for month in range(1, 13):
                for site_code in code_list:
                    try:
                        avg = sum(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)][field]) / \
                              len(read_1[(read_1['月'] == month) & (read_1['区站号'] == site_code)])  # 浮点型数据
                        read_1.loc[
                            (read_1['月'] == month) & (read_1['区站号'] == site_code) & (read_1['日'] == 1), [field]] = avg
                    except:
                        print(f'{filenames[num]}文件中{month}没有{site_code}的数据！')
            print(f'字段{field}已计算完成！')

        select = read_1[(read_1['日'] == 1)][['省份', '站名', '区站号', '维度', '经度', '观测场海拔高度', '年', '月', '平均风速', '最大风速', '极大风速']]
        select.reset_index(inplace=True)
        select.drop(columns=['index'], inplace=True)
        print('程序段1已执行结束！')
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
        OUT = out_fold + filenames[num]
        select.to_csv(OUT, index=False)
        print(f'{filenames[num]}已输出！')


