import pandas as pd
# 该模块的功能是一次性将多张表读入存到一个列表中去
a = []
for i in range(12, 13):       # 年份范围，左闭右开
    for j in range(1, 5):     # 月份范围，左闭右开
        k = i*100+j
        l = str(k)
        n = str(i)
        p = str(j)
        m = 'qt'+l
        q = n+'年'+p+'月'
        m = pd.read_excel(r"D:\A数据 - 处理文件夹\去头数据 - 副本\人口数据.xlsx", sheet_name=q)
        a.append(m)

# 该模块实现追加
b = pd.read_excel(r"D:\A数据 - 处理文件夹\去头数据 - 副本\人口数据汇总.xlsx", sheet_name='Sheet1')
for d in a:
    b = pd.merge(b, d, left_on='ID', right_on='ID', how='left')
print(b.head(2))
b.to_excel(r"D:\A数据 - 处理文件夹\去头数据 - 副本\人口数据汇总2.xlsx", index=False)