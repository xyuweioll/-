import re
import time
import numpy as np
import pandas as pd
import requests
import datetime  # 用于获取系统当前时间
import winreg
import sys
# ===========================================================================================
# 定义自动获取桌面路径函数
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
    return winreg.QueryValueEx(key, "Desktop")[0]  # 返回的是Unicode类型数据


Desktop_path = str(get_desktop())  # Unicode转化为str,获取桌面路径

# ============================================================================================
select_date = input('请输入你要查询的日期,若查询最近一天的日报请输入1，日期输入格式：2022-08-02\n=======>>>')
if select_date == '1':
    select_date = datetime.datetime.now().strftime('%Y-%m-%d')
else:
    pass
print(f"查询的日期/起始日期为：{select_date}")
select_date_1 = datetime.datetime.strptime(select_date, "%Y-%m-%d")
day_num = (datetime.datetime.now()-select_date_1).days+1   # 计算所查询日期距离今天的天数，加一即为查询的总天数
print(f"总计查询的天数/查询日期距离今天的天数为：{day_num}天")
if day_num%18==0:
    page_number = day_num//18   # 计算需要查询的页面的页数
else:
    page_number = day_num//18+1
print(f'需要查询的页面数为：{page_number}页')
# ======================================================================
# today = datetime.datetime.now()  # 获取当前系统时间
# yesterday = today - datetime.timedelta(days=2)  # 减1天,得到昨天的日期
# after_yesterday = yesterday+datetime.timedelta(days=1)  # 加1天
# after_yesterday = after_yesterday.strftime('%Y-%m-%d')  # 将时间格式化为字符串
# print(yesterday)
# yesterday = yesterday.strftime('%Y-%m-%d')  # 将时间格式化为字符串
# print(yesterday)
# yesterday = yesterday.split('-')
# year = yesterday[0]
# month = str(int(yesterday[1]))  # 先转数字再转字符是未来去除前面的0，如8月为08
# day = str(int(yesterday[2]))
# print(year, month, day)
##  =======================================================================
# 日期运算操作
# datetime1 = today - datetime.timedelta(seconds=10)  # 减10秒
# datetime2 = today - datetime.timedelta(minutes=10)  # 减10分钟
# datetime3 = today - datetime.timedelta(hours=1)  # 减1小时
# datetime4 = today - datetime.timedelta(days=1)  # 减1天
# datetime5 = today - datetime.timedelta(weeks=1)  # 减1周
# datetime6 = today.strftime('%Y-%m-%d')  # 将时间格式化为字符串
## ==================================
# 生成url列表
url_list =["http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml"]
for i in range(2, page_number+1):
    url_list.append("http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_"+str(i)+".shtml")
print(f"url_list:{url_list}")
# ====================
header1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    'Referer': 'http://www.nhc.gov.cn/xcs/xxgzbd/gzbd_index.shtml'
}

header2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    'Referer': 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'
}

adress_dic = {}   # 用于存放一个页面的所有日期和地址，日期为键，地址为值
for url in url_list:
    time.sleep(0.05)  # 程序休眠50毫秒
    resp = requests.get(url, headers=header1, verify=False)
    page_cotent = resp.text  # 拿到页面源代码
    resp.close()  # 关闭请求
    print(page_cotent)
    obj = re.compile(f'''<li>  <a href="(?P<adress>.*?)" target="_blank" title.*?<span class="ml">(?P<date_today>.*?)</span>''',
                      re.S)
    result = obj.finditer(page_cotent)
    for it in result:
        adress_dic[it.group('date_today')] = "http://www.nhc.gov.cn" + it.group('adress')
    try:
        print(f'child_herf:{adress_dic[select_date]}')
    except:
        print(f'遭遇反爬！请稍后再次尝试！')
# ================================================================================
# 获取到需要查询那一天的页面
child_herf = adress_dic[select_date]  # 根据日期获取链接，即根据字典的键获取值
resp2 = requests.get(child_herf, headers=header2, verify=False)
page_cotent2 = resp2.text
print(page_cotent2)
resp2.close()  # 关闭请求
# +++++++++++++++++++++++++++++++++++++
# 解析境外输入确诊病例
# obj_jingwai = re.compile(f"31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例.*?例。其中境外输入病例.*?例（(?P<comfirm_jinwai>.*?)）")
# try:
#     jingwai = obj_jingwai.finditer(page_cotent2)
# except:
#     print('获取内容失败，可能遭遇反爬！')
#     sys.exit()      # 若没有获取的内容，无法匹配则给出提示并终止程序
# for i_jinwai in jingwai:
#     print(f"境外输入确诊情况：{i_jinwai.group('comfirm_jinwai')}")
#     jingwai = ',' + i_jinwai.group('comfirm_jinwai')  # 各个省份境外输入病例的情况,加个逗号未来方便正则表达式匹配
# obj_jingwai_1 = re.compile(".?(?P<Province>\D{1,})(?P<cases>\d{1,})例")
# jingwai_1 = obj_jingwai_1.finditer(jingwai)
#
# Province = []  # 存放省份名
# cases = []    # 存放病例数
# for i_jinwai_1 in jingwai_1:
#     # print(i_jinwai_1.group("Province"))
#     Province.append(i_jinwai_1.group("Province"))
#     # print(i_jinwai_1.group("cases"))
#     cases.append(i_jinwai_1.group("cases"))
# data = pd.DataFrame()  # 创建空数据框
# data['省份'] = Province
# data['境外输入确诊'] = cases
# data.to_csv(f"{Desktop_path}\\data.csv", index=False)
# +++++++++++++++++++++++++++++++++++++
# 解析境外无症状转确诊
obj_jingwai_zhuan = re.compile(f"31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例.*?例。.*?，含.*?例由无症状感染者转为确诊病例（(?P<jingwai_zhuan>.*?)）")
jingwai_zhuan = obj_jingwai_zhuan.finditer(page_cotent2)
for i_jinwai_zhuan in jingwai_zhuan:
    print(f"境外无症状转确诊情况：{i_jinwai_zhuan.group('jingwai_zhuan')}")
    jingwai_zhuan = ',' + i_jinwai_zhuan.group('jingwai_zhuan')  # 各个省份境外输入病例的情况,加个逗号未来方便正则表达式匹配
print(jingwai_zhuan)
obj_jingwai_zhuan_1 = re.compile(".?(?P<Province>\D{1,})(?P<cases>\d{1,})例")
jingwai_zhuan_1 = obj_jingwai_zhuan_1.finditer(jingwai_zhuan)
# for i_jinwai_zhuan_1 in jinwai_zhuan_1:


# http://www.nhc.gov.cn/xcs/yqtb/202208/8802f7342e2c4bd7ac2d123930f3aedc.shtml

