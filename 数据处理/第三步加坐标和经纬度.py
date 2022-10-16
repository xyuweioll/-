import pandas as pd

a = pd.read_excel(r'C:\Users\xianyu\Desktop\黑龙江省ID.xlsx', sheet_name='Sheet1')
c = pd.read_excel(r'C:\Users\xianyu\Desktop\人口.xlsx', sheet_name='Sheet1')
b = pd.merge(a, c, left_on='CITY_CODE', right_on='CITY_CODE', how='left')
b.to_excel(r'C:\Users\xianyu\Desktop\黑龙江省人口数据.xlsx', index=False)

# import pandas as pd
# a = pd.read_excel(r"C:\Users\xianyu\Desktop\吉林省ID.xlsx", sheet_name="Sheet1")
# b = pd.read_excel(r"C:\Users\xianyu\Desktop\人口.xlsx", sheet_name="Sheet1")
# c = pd.merge(a, b, left_on='CITY_CODE', right_on='CITY_CODE', how='left')
# c.to_excel(r"C:\Users\xianyu\Desktop\吉林省人口数据.xlsx", index=False)