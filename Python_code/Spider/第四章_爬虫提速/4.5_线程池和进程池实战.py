# 1.如何提取单个页面的数据
# 2.上线程池，多个页面同时抓取
# 页面数据是动态加载出来的，通过携带参数current=n去拿第n页的数据
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import csv
f = open(r"C:\Users\xianyu\Desktop\data.csv", "w", encoding='gbk')
f.write('prodName,avgPrice,highPrice,lowPrice,place,prodCat')
csvwriter = csv.writer(f)


def download_one_page(url):
    # 拿到页面源代码
    resp = requests.get(url)
    list_data = resp.json()['list']  # 在这里可以将json理解为python中的字典
    # print(list_data)
    for i in list_data:
        ls = [str(i['prodName']), str(i['avgPrice']), str(i['highPrice']), str(i['lowPrice']), str(i['place']),
              str(i['prodCat'])]
        # print(ls)
        # f.write(",".join(ls) + "\n")
        csvwriter.writerow(ls)


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 500):
            # 把任务提交给线程池
            t.submit(download_one_page, f'http://www.xinfadi.com.cn/getPriceData.html?current={i}')
            print(f"第{i}个页下载成功！")
    print('程序结束！')



