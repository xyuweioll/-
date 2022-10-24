import pandas as pd
import os.path
rootdir = input('请输入存放文件的文件夹路径\n ===>>>')
for parent, dirnames, filenames in os.walk(rootdir):
    for i in filenames:
        if os.path.splitext(i)[1] == '.xls':  # 判断文件扩展名是不是为.xlsx  os.path.splitext(“文件路径”)
            filedir = os.path.join(parent, i)
            print(filedir)
            df = pd.read_excel(filedir)
            print(df)
            colName = df.columns.tolist()  # 获取所有列名并强转为列表
            print(colName)
            print(colName[2:])
            df['Total'] = df[colName[2:]].sum(axis=1)  # 每一行进行求和后加一列
            # print(df[colName[2:]].sum(axis=1))  # 每一行进行求和
            # print(df[colName[2:]].sum(axis=0))  # 每一列进行求和
            for j in colName[2:]:
                df[f"{j}_{i[9:-4]}"] = df[f"{j}"]/df['Total']*100
            df.to_excel(filedir, index=False)  # 输出并覆盖源文件

