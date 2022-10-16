import os
import pandas as pd
import winreg


# 定义自动获取桌面路径函数
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
    return winreg.QueryValueEx(key, "Desktop")[0]  # 返回的是Unicode类型数据


Desktop_path = str(get_desktop())  # Unicode转化为str,获取桌面路径

# ============================================================================================
work_path = input('请输入文件路径\n===>>>')
col_name = input('请输入连接字段名\n===>>>')
os.chdir(work_path)
file_name = os.listdir(work_path)  # 取工作路径下的所有文件
file_name0 = sorted(file_name)  # 实现自然排序
print(file_name0)
first_file = pd.read_excel(file_name0[0], sheet_name=0)  # 读取第一个文件
for i in range(1, len(file_name0)):
    print(file_name0[i])
    # sheetname = file_name0[i][:-4]
    data = pd.read_excel(file_name0[i], sheet_name=0)
    print(f"{file_name0[i]}读取完成！")
    # first_file = pd.merge(first_file, data, left_on='CNTY_COD_1', right_on='CNTY_COD_1', how='left',
    # suffixes=('_' + file_name0[i-1][:5], '_' + file_name0[i][:5]))      #  suffixes用于重叠列的字符串后缀元组。 默认为（‘x’，’ y’）。
    first_file = pd.merge(first_file, data, left_on=f'{col_name}', right_on=f'{col_name}', how='outer')
first_file.to_csv(rf'{Desktop_path}\横向合并输出.csv', encoding='gbk', index=False)
print('文件已输出')

# qt1201=pd.read_excel(r"D:\A数据 - 处理文件夹\去头数据 - 副本\综合数据集.xls",sheet_name="12年1月")
# qt1202=pd.read_excel(r"D:\A数据 - 处理文件夹\去头数据 - 副本\综合数据集.xls",sheet_name="12年2月")
# print(qt1201.head(10))
# print(qt1202.head(10))
