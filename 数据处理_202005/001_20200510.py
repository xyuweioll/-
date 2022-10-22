import pandas as pd
import os
# 处理的思想就是将每一个月的平均值/累计值计算出来后赋值给对应月份的1日，然后再将每个月1日的数据提取出来即可得到月数据
rootdir = u'C:\\Users\\xianyu\\Desktop\\del'  # 存放文件的根目录
out_fold = 'C:\\Users\\xianyu\\Desktop\\'   # 输出文件目录
read_list = []
for parent, dirnames, filenames in os.walk(rootdir):   # 此时filenames 是一个存放了所有文件名的列表
    for fn in filenames:
        filedir = os.path.join(parent, fn)  # os.path.join是路径拼接函数，
        read_list.append(filedir)
        print(filedir)

for num in range(len(filenames)):
    read_1 = pd.read_excel(read_list[num])  # 读取文件
    print(f'{filenames[num]}已经成功读取！')
    code_list = read_1['气象站'].drop_duplicates()  # 获取站点号并去除重复值
    for field in ['降水量', '水面蒸发量']:
        for month in range(9, 11):
            for site_code in code_list:
                try:
                    avg = sum(read_1[(read_1['月'] == month) & (read_1['气象站'] == site_code)][field]) / \
                          len(read_1[(read_1['月'] == month) & (read_1['气象站'] == site_code)])  # 计算一个站点一个月的平均地表温度，浮点型数据
                    read_1.loc[
                        (read_1['月'] == month) & (read_1['气象站'] == site_code) & (read_1['日'] == 1), [field]] = avg
                except:
                    print(f'{filenames[num]}文件中{month}没有{site_code}的数据！')
        print(f'字段{field}已计算完成！')

    select = read_1[(read_1['日'] == 1)][
        ['气象站', '年', '月', '日', '降水量', '水面蒸发量', 'FID', '经度', '纬度', '高程_m_']]
    select.reset_index(inplace=True)
    select.drop(columns=['index'], inplace=True)
    print('程序段1-1已执行结束！')
    OUT = out_fold + filenames[num]
    select.to_excel(OUT, index=False)
    print(f'{filenames[num]}已输出！')