import pandas as pd
import xlwt
data = pd.read_excel(r"C:\Users\xianyu\Desktop\06-14.xlsx", sheet_name='Sheet1')
data2 = pd.read_excel(r"C:\Users\xianyu\Desktop\15-20.xlsx", sheet_name='Sheet1')
c = pd.concat([data, data2], ignore_index=True)
c.to_excel(r"C:\Users\xianyu\Desktop\2006-2020全国个案数据汇总.xlsx", index=False)
