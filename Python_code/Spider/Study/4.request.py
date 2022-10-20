import requests

url = " https://fanyi.baidu.com/sug"
s = input("请输入您想查询的单词\n===>>>")
dat = {
    "kw": s
}
# 发送post请求,发送的数据必须放在字典中，通过data参数进行传递
resp = requests.post(url, data=dat)
print(resp.json())  # 将服务器返回的内容直接处理成json()    =>dict


