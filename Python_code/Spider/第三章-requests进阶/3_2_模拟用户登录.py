# 处理 cookie
# 登录->得到cookie
# 带着cookie去请求url -> 得到内容
# 必须把上面的两个操作连起来
# 我们可以使用session进行请求 -> session可以认为是一连串的请求。在这个过程中的cookie不会丢失
import requests

# 会话,session可以保存上下文会话的内容
session = requests.session()

# 1. 登录
url ="https://passport.17k.com/ck/user/login"
data = {
    "loginName": "18256233572",
    "password": "Wei@163.com"
}
resp = session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)  # 看cookie
# 2.拿数据
# 刚才的那个会话中是有cookies的，
resp2 = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(resp2.json())
