import pandas as pd
import os
rootdir = u'D:\\Climate\\SELECT-month-FIX'  # 存放文件的根目录
os.chdir(rootdir)
out_fold = 'D:\\Climate\\Interpolation-csv-fix\\'   # 输出文件目录
for parent, dirnames, filenames in os.walk(rootdir):   # 此时filenames 是一个存放了所有文件名的列表
    print(f'文件夹中共有{len(filenames)}个文件！')
#        filedir = os.path.join(parent, fn)  # os.path.join是路径拼接函数

for file in filenames:
    print(f'正在读取--{file}。。。')
    read = pd.read_csv(file)
    num_list = ['01', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for field_num in range(1, 13):
        month = read[(read['月'] == field_num)]
        month.reset_index()
        month.to_csv(f'{out_fold}{file[len(file)-14:len(file)-4]}-{num_list[field_num]}.csv', index=False)

    print(f'文件-{file}已经完成！')


