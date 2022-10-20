# 原理：通过第三方的机器去发送请求
import requests

# 110.81.107.181:7311
proxies = {
    "https": "https://165.225.196.94:10605"
}
resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)


# 找可以做中间代理的IP
