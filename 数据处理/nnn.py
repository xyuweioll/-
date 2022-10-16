import pandas as pd
a = pd.read_excel(r"C:\Users\xianyu\Desktop\东北Satscan\SaTScan1.xlsx", sheet_name='Sheet')
b = pd.read_excel(r"C:\Users\xianyu\Desktop\东北Satscan\东北经纬度.xlsx", sheet_name="Sheet1")
c = pd.merge(a, b, left_on='CITY_CODE', right_on='市代码', how='left')
#c = pd.merge(a, b, on=['现住地址国标', '性别', '发病日期'], how='left')
c.to_excel(r"C:\Users\xianyu\Desktop\东北.xlsx", index=False)
#a = pd.read_csv(r'C:\Users\xianyu\Desktop\2011.csv')
#a.to_csv(r'G:\Artical-1\Satscan\SaTScan-cases.txt', header=None, index=False, sep=" ")