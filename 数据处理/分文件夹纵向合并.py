import pandas as pd
import os
import xlrd
input_path = 'C:\\Users\\xianyu\\Desktop\\ICD10-OUT'
os.chdir(input_path)
file_list = []
for parent, dirnames, filenames in os.walk(input_path):
    print(filenames)
for filename in filenames:
    print(f'{filename}正在读取！')
    file_i = pd.read_excel(filename, sheet_name='Sheet1')
    print(f'{filename}读取完成！')
    file_list.append(file_i)
out_file = pd.concat(file_list, ignore_index=True)
out_file.to_csv('C:\\Users\\xianyu\\Desktop\\ICD10完全.csv', index=False)







# for work_path in foldlist:      # 循环文件夹
#     open_path = input_path + '\\' + work_path
#     os.chdir(open_path)  # 设定工作目录
#     print(open_path)
#     file_list = []
#     for parent, dirnames, filenames in os.walk(open_path):  # 获取每个文件夹中的文件名
#         for i in filenames:    # 循环读取文件
#             print(i)
#             data = pd.read_excel(i, sheet_name=0)  # 读取表
#             file_list.append(data)  # 将读取出来的表放入列表
#         outfile = pd.concat(foldlist, ignore_index=True)  # 纵向连接
#         outfile.to_csv(output_path+work_path+'.csv', index=False)   # 输出连接表
#         print(f'{work_path}已经输出!')