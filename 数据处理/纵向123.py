import pandas as pd
import xlwt
data = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2006.xlsx", sheet_name='2006')
data1 = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2007.xlsx", sheet_name='2007')
data2 = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2008.xlsx", sheet_name='2008')
data3 = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2009.xlsx", sheet_name='2009')
data4 = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2010.xlsx", sheet_name='2010')
data5 = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2011.xlsx", sheet_name='2011')
data6 = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2012.xlsx", sheet_name='2012')
data7 = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2013.xlsx", sheet_name='2013')
data8 = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2014年1-6月.xlsx", sheet_name='1-6')
data9 = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2014年7-9月.xlsx", sheet_name='7-9')
data10 = pd.read_excel(r"C:\Users\xianyu\Desktop\需要字段\2014年10-12月.xlsx", sheet_name='10-12')

c = pd.concat([data, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10], ignore_index=True)
c.to_excel(r"C:\Users\xianyu\Desktop\个案数据合成06-14.xlsx", index=False)
