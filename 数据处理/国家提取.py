import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import xlwt

# 需要查询的国家英文名：India,Russian Federation,Thailand,Japan,Bangladesh,Viet Nam,Kazakhstan,Pakistan,Myanmar,Nepal,
# South Korea,Mongolia,Lebanon,Uzbekistan,Kyrgyzstan,Lao People's Democratic Republic,Afghanistan,Congo

data = pd.read_excel(r"C:\Users\xianyu\Desktop\WHO-COVID-19-global-data.xlsx", sheet_name=
"WHO-COVID-19-global-data")
a = input('请输入你要查询的国家名，用英文逗号作为分割符\n-------->') # 此时国家名还是一个字符串
b = a.split(',')  # split函数的作用是将字符串按照特定字符分割后存进列表里,这里就是按照英文逗号分割
# b = [s.capitalize() for s in b]  #这一步的作用是将列表b里的每一个字符串进行首字母大写，其他字母小写化处理
c = []   # 此处定义一个空列表，空列表用于存储
for i in b:
    data1 = data['Country'] == i  # 用于判断'Country'这一列的值是否等于特定值i，其返回值为布尔值；
    d = data[data1]  # 再将布尔值作为筛选条件进行筛选，其只返回布尔值等于True的行；
    # e = d['New_cases']  #取表格中的特定列，即选择单列
    e = d[['Date_reported', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']]
    c.append(e)

# e的数据格式是dataframe,所以下面的模块是将一个dataframe写进入
writer = pd.ExcelWriter('C:\\Users\\xianyu\\Desktop\\查询国家数据.xlsx')
for i in range(len(c)):
    c[i].to_excel(writer, sheet_name=b[i], index=False)
writer.save()
writer.close()



# print(e)
# print(len(e))
# print(type(e))

# 创建工作簿
# f = xlwt.Workbook()


# # 以国家为各个sheet的名字创建sheet，查了几个国家就创建了几个sheet
# for i in range(len(b)):
#     name = b[i]
#     sheet1 = f.add_sheet(name, cell_overwrite_ok=True)

# writer = pd.ExcelWriter(f)
# for i in range(len(c)):
#      eval(c[i]).to_excel(excel_writer=writer, sheet_name=b[i], index=False)
# writer.save()
# writer.close()
# f.save("C:\\Users\\xianyu\\Desktop\\查询国家数据.xlsx")

# 中国周边国家有：
# 俄罗斯、哈萨克斯坦、吉尔吉斯斯坦、塔吉克斯坦、蒙古、越南、老挝、缅甸、印度、不丹、尼泊尔、巴基斯坦、阿富汗、朝鲜
#  Russian Federation,Kazakhstan,Kyrgyzstan,Tajikistan,Mongolia,Viet Nam,Lao People's Democratic Republic,Myanmar,India,Bhutan,Nepal,Pakistan,Afghanistan,Democratic People's Republic of Korea
# 日本、韩国、马来西亚、印度尼西亚、文莱、菲律宾
#  Japan,Republic of Korea,Malaysia,Indonesia,Brunei Darussalam,Philippines















