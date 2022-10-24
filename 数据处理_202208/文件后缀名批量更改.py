# python批量更换后缀名
import os
path_1 = input("请输入文件路径\n=====>>>>")
os.chdir(path_1)
files = os.listdir(path_1)  # 列出当前目录下所有的文件
for filename in files:
    portion = os.path.splitext(filename)
    # 如果后缀是.dat
    if portion[1] == ".dat":
        # 重新组合文件名和后缀名
        newname = portion[0] + ".csv"
        os.rename(filename, newname)
