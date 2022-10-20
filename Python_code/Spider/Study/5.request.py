import requests

url = " https://movie.douban.com/j/chart/top_list"
# 重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}   # 伪装成浏览器

resp = requests.get(url=url, params=param, headers=header)

print(resp.json())
resp.close()   # 关掉resp，若不关闭访问次数过多会报错

