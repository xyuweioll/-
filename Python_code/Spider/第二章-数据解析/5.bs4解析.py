'''
# BeautifulSoup解析
bs4解析-HTML语法
HTML(Hyper Text Markup Language) 超文本标记语言，是我们编写网页的最基本也是最核心的一种语言，其语法规则就是用不同的标签
对网页上的内容进行标记，从而使网页显示出不同的展示效果
'''

# 安装
import requests
from bs4 import BeautifulSoup
url = "http://www.szhigreen.com/"
resp = requests.get(url)
print(resp.text)
# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
# 2.从bs对象中查找数据
# find(标签,属性=值)   find只找第一个值
# find_all(标签,属性=值)    find_all找同一类标签的所有值
# page.find("table", class_="hq_table")  # class是python的关键字，用下划线进行区分
table = page.find("table", attrs={"class": "hq_table"})  # 和上一行是一个意思，此时可以避免class
print(table)
# 拿到所以数据行
trs = table.find_all("tr")
for tr in trs:    # 每一行
    tds = tr.find_all("td")  # 拿到每一行中的所以td
    name = tds[0].text    # .text 表示拿到被标签标记的内容






