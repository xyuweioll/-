# 拿到页面源代码   requests
# 通过re来提取想要的有效信息  re模块
import re
import requests
import csv    # 为了将数据存为csv格式， 注意此模块的使用
for start in range(0, 251, 25):   # 爬取前10页
    print(start)
    url = f"https://movie.douban.com/top250?start={start}&filter="
    header ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=header)
    page_cotent = resp.text      # 拿到页面源代码

    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>\s*(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span>(?P<num>.*?)</span>', re.S)

    # 开始匹配
    result = obj.finditer(page_cotent)
    if start == 0:
        mod = "w"   # 写文件
    else:
        mod = "a"   # 追加数据
    f = open("C:\\Users\\xianyu\\Desktop\\data.csv", mode=mod, newline='')  # 打开文件 没有则创建,a表示追加//
    csvwriter = csv.writer(f)                                               # newline='': 这个限定插入新数据不会空行，如果没有这个，每次插入数据都会隔行填数据
    for it in result:
        # print(it.group("name"))
        # print(it.group("year"))
        # print(it.group("score"))
        # print(it.group("num"))
        dic = it.groupdict()
        print(dic)
        csvwriter.writerow(dic.values())   # 按行写入数据
    f.close()
    print("over")


