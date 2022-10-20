# 1.拿到主页面的源代码，然后提取子页面的链接地址，herf
# 2.通过herf拿到子页面的内容，从子页面中找到图片的下载地址  img->src
# 3.下载图片
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = "utf-8"  # 处理乱码
# print(resp.text)
# 源代码交给Beautifulsoup
main_page = BeautifulSoup(resp.text, "html.parser")  # "html.parser" 告诉它按照HTML解析
alist = main_page.find("div", class_="swiper mySwiper").find_all("a")  # 找所有的a标签，把范围第一次缩小
print(alist)
for a in alist:
    print(a.get("href"))  # 直接通过get就可以拿到属性的值
    href = "https://www.umei.cc" + a.get("href")
    print(href)
    # 拿到子页面源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    p = child_page.find("section", class_="img-content")
    img = p.find("img")  # 找到img标签
    src = img.get("src")  # 获取某个标签里的某个属性的值
    print(src)
    # 3.下载图片
    img_resp = requests.get(src)
    img_name = src.split("/")[-1]  # 通过/切割路径，并且取到最后一个作为图片的名字
    with open(f"C:\\Users\\xianyu\\Desktop\\图\\{img_name}", mode="wb") as f:  # 写入文件
        f.write(img_resp.content)
    print(f"{img_name}over")
    time.sleep(0.5)  # 休眠0.5秒
print("finished")

