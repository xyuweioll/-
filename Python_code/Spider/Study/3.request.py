# requests模块
# 国内源
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
import requests
url = "https://www.sogou.com/web?query=周杰伦"
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
# 浏览器地址栏里面输入的网址统一用get
resp = requests.get(url, headers=header)   # 处理一个小小的反爬
print(resp)
print(resp.text)   # 查看页面源代码
