# 爬虫：通过编写程序获取互联网上的资源
# 需求：用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容
from urllib.request import urlopen  # 打开一个网址

url = "http://www.baidu.com"
resp = urlopen(url)
# windows默认encoding为gbk
with open("mybaidu.html", mode="w", encoding='utf-8') as f:  # 将结果写入一个文件
    f.write(resp.read().decode("utf-8"))    # 读取到网页的页面源代码
print("over!")
