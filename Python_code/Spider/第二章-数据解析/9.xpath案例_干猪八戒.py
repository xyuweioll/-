# ctrl+f 键可调出在源码界面搜索
# 拿到页面源代码
# 提取和解析数据
import requests
from lxml import etree

url = "https://www.zbj.com/search/service/?kw=saas&r=1"
resp = requests.get(url)
# print(resp.text)
# 解析
html = etree.HTML(resp.text)
# 拿到每一个服务商的div
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
print(divs)
for div in divs:  # 每一个服务商信息
    price = div.xpath("./div[3]/div[1]/span/text()")[0]
    name = div.xpath('./a/div[2]/div[1]/div/text()')[0]
    print(name, ':', price)



