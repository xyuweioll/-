import os
import os.path
import win32com.client as win32
# 根目录
a = input("是否保留原格式文件？不保留请输入 1/保留 2\n--->>")
b = int(a)
rootdir = u'C:\\Users\\xianyu\\Desktop\\河北分年龄性别 - 副本'  #存放文件的根目录
# 三个参数：父目录；所有文件夹名（不含路径）；所有文件名
for parent, dirnames, filenames in os.walk(rootdir):
    for fn in filenames:
        filedir = os.path.join(parent, fn)  # os.path.join是路径拼接函数，
        print(filedir)

        # excel = win32.gencache.EnsureDispatch('Excel.Application')   # 若报错则用下一条语句
        excel = win32.DispatchEx('Excel.Application')
        wb = excel.Workbooks.Open(filedir)  # 打开文件
        # xlsx: FileFormat=51
        # xls:  FileFormat=56,
        # 后缀名的大小写不通配，需按实际修改：xls，或XLS
        wb.SaveAs(filedir.replace('xls', 'xlsx'), FileFormat=51)  # 我这里原文件是小写的xls
        wb.Close()
        excel.Application.Quit()
    if b == 1:
        for fn in filenames:
            filedir = os.path.join(parent, fn)  # os.path.join是路径拼接函数，
            os.remove(filedir)
            print(filedir)









# for parent, dirnames, filenames in os.walk('C:\\Users\\xianyu\\Desktop\\调试数据'):
#     print(parent)  # C:\Users\xianyu\Desktop\调试数据  即返回父目录
#     print(dirnames)  # 返回文件夹名，因为不包含文件夹，所以返回一个空列表[]
#     print(filenames)  # 返回所有的文件名在一个列表中['1.csv', '上海201001.csv', '上海201001.xls', '上海201001.xlsx',
#     # '上海201002.csv', '上海201002.xls', '上海201003.xls', '上海201004.xls', '上海201005.xls', '上海201006.xls',
#     # '上海201007.xls', '上海201008.xls', '上海201009.xls']