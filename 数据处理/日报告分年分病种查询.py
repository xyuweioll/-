import pandas as pd
import os
import openpyxl
pname = input("请输入需要查询的省份名\n====>>>>")
dname = input("请输入需要查询的病名\n =====>>>>")
date = input("请输入你要查询的日期范围\n（输入示例：如2001年至2020：2001:2020）"
          "注意！间隔符为英文形式\n====>>>>")
a = date.split(':')  # 此时a的格式为['2001','2020']
print(a)
# ==============================================================
# 代码段1：生成文件中的年份段存放在列表 year_n[]中
stat_y = int(a[0])
over_y = int(a[1])
year_n = []
for i in range(stat_y, over_y+1):
    year_n.append(i)
print(f'已生成年份列表{year_n}')
print('代码段1已执行完毕！')
# ===============================================================
# 代码段2：生成完整的文件名列表
file_name = []  # 用于存放生成的文件名
for i in year_n:
    a = pname+str(i)+'日报'+'.xlsx'
    file_name.append(a)
print(f'文件名列表已生成:{file_name}')
print('代码段2已执行完毕！')
# ===============================================================
# 代码段3：查找操作
os.chdir('C:\\Users\\xianyu\\Desktop\\调试数据')   # 确定操作路径，也就是文件存放文件夹路径，根据实际情况更改
feature_name = ['时间', dname, dname+'death']     # 需要查询的属性列表
sheet = []                                       # 用于存放每一张表
exception = []                                   # 用于存放表中没有所查询疾病的表
for i in range(len(file_name)):
    try:
        d_case = pd.read_excel(file_name[i])
        sheet.append(d_case[feature_name])
        print(f'{file_name[i]}已查询完毕！')
    except Exception as oll:
        exception.append(file_name[i])
        print(f'{file_name[i]}中不存在{dname}！')
    continue
print('代码段3执行完毕！')
print(sheet)
# ===============================================================
# 代码段4
# 这段程序将刚在出现异常的年份表在file_name列表里删除
if len(exception) != 0:
    for i in exception:
        print(f'{i}已在查询列表中删除！')
        file_name.remove(i)
print('代码段4执行完毕！')
# ===============================================================
# 代码段5：写出每一张表操作，将每一年写一张表
writer = pd.ExcelWriter('C:\\Users\\xianyu\\Desktop\\输出数据.xlsx')
for i in range(len(file_name)):
    sheet[i].to_excel(writer, sheet_name=file_name[i], index=False)
writer.save()
print('代码段5执行完毕！')
# ===============================================================
# 代码段6：进行横向连接

for i in range(len(sheet)):
    sheet[i].to_excel(writer, sheet_name='横向合并表', index=False, startcol=len(feature_name)*i)
writer.save()
print('代码段6执行完毕')
# =================================================================
# 代码段7：进行纵向追加
zong = sheet[0]
for i in range(len(sheet)):
    zong = pd.concat([zong, sheet[i]], ignore_index=True)
zong.to_excel(writer, sheet_name='纵向合并表', index=False)
writer.save()
writer.close()
print('程序已执行完毕，在桌面查看输出文件')
# ==================================================================

















