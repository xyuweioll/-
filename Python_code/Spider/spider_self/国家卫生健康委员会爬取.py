import random
import re
import time
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
day_num = (datetime.datetime.now() - select_date_1).days + 1  # 计算所查询日期距离今天的天数，加一即为查询的总天数
print(f"总计查询的天数/查询日期距离今天的天数为：{day_num}天")
if day_num % 18 == 0:
    page_number = day_num // 18  # 计算需要查询的页面的页数
else:
    page_number = day_num // 18 + 1
print(f'需要查询的页面数为：{page_number}页')
## ==================================
# 生成url列表
url_list = ["http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml"]
for i in range(2, page_number + 1):
    url_list.append("http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_" + str(i) + ".shtml")
print(f"url_list:{url_list}")
# ====================
# 以下均是经过验证可用的user_agent
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11']
user_agent1 = random.choice(user_agent_list)  # 随机从user_agent中选取一个
user_agent2 = random.choice(user_agent_list)  # 随机从user_agent中选取一个
header1 = {
    "User-Agent": user_agent1,
    'Referer': 'http://www.nhc.gov.cn/xcs/xxgzbd/gzbd_index.shtml'
}

header2 = {
    "User-Agent": user_agent2,
    'Referer': 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'
}

adress_dic = {}  # 用于存放一个页面的所有日期和地址，日期为键，地址为值
for url in url_list:
    time.sleep(0.05)  # 程序休眠50毫秒
    resp = requests.get(url, headers=header1, verify=False)
    page_cotent = resp.text  # 拿到页面源代码
    resp.close()  # 关闭请求
    print(page_cotent)
    obj = re.compile(
        f'''<li>  <a href="(?P<adress>.*?)" target="_blank" title.*?<span class="ml">(?P<date_today>.*?)</span>''',
        re.S)
    result = obj.finditer(page_cotent)
    for it in result:
        adress_dic[it.group('date_today')] = "http://www.nhc.gov.cn" + it.group('adress')
    try:
        print(f'child_herf:{adress_dic[select_date]}')
    except:
        print(f'遭遇反爬！请稍后再次尝试！')
        print(f"user_agent1为:{user_agent1}")
        print(f"user_agent2为:{user_agent2}")
        sys.exit()  # 若没有获取的内容，无法匹配则给出提示并终止程序
# ================================================================================
# 获取到需要查询那一天的页面
child_herf = adress_dic[select_date]  # 根据日期获取链接，即根据字典的键获取值
resp2 = requests.get(child_herf, headers=header2, verify=False)
page_content2 = resp2.text
print(page_content2)
resp2.close()  # 关闭请求
#  ====
page_content2 = page_content2.replace('<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">', '')
page_content2 = page_content2.replace('</span>', '')
#  ===
# 解析境外确诊病例
data0 = pd.DataFrame({"省份": [], "境外输入确诊": []})  # 创建空数据框
try:
    obj_jingwai = re.compile(
        f"31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例.*?例。其中境外输入病例(?P<Total_confirm>.*?)例（(?P<comfirm_jinwai>.*?)）")
    jingwai = obj_jingwai.finditer(page_content2)
    Total = []  # 存放境外无症状转确诊总数
    Province = []  # 存放省份名
    cases = []  # 存放病例数
    for i_jinwai in jingwai:
        print(f"境外输入确诊情况：{i_jinwai.group('comfirm_jinwai')}")
        Total.append(i_jinwai.group('Total_confirm'))
        jingwai = ',' + i_jinwai.group('comfirm_jinwai')  # 各个省份境外输入病例的情况,加个逗号未来方便正则表达式匹配
    print(jingwai)
    judge_jingwai = re.search('均在', jingwai)  # 搜索不到则返回None
    if judge_jingwai == None:
        obj_jingwai_1 = re.compile(".?(?P<Province>\D{1,})(?P<cases>\d{1,})例")
        jingwai_1 = obj_jingwai_1.finditer(jingwai)
        for i_jinwai_1 in jingwai_1:
            Province.append(i_jinwai_1.group("Province"))
            cases.append(i_jinwai_1.group("cases"))
        data0['省份'] = Province
        data0['境外输入确诊'] = cases
    else:
        data0['省份'] = [jingwai[3:]]
        data0['境外输入确诊'] = Total
except:
    print(f"user_agent1为:{user_agent1}")
    print(f"user_agent2为:{user_agent2}")
    print('可能遭遇反扒，请稍后重新尝试')
    sys.exit()  # 若没有获取的内容，无法匹配则给出提示并终止程序
# ==========================================================================================
# 境外无症状转确诊数据解析
data1 = pd.DataFrame({"省份": [], "境外输入无症状转确诊": []})  # 创建空数据框
try:
    obj_jingwai_zhuan = re.compile(
        f"31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例.*?例。.*?，含(?P<Total_zhuan>.*?)例由无症状感染者转为确诊病例（(?P<jingwai_zhuan>.*?)）")
    jingwai_zhuan = obj_jingwai_zhuan.finditer(page_content2)
    Total = []  # 存放境外无症状转确诊总数
    Province = []  # 存放省份名
    cases = []  # 存放病例数
    for i_jinwai_zhuan in jingwai_zhuan:
        print(f"境外无症状转确诊情况：{i_jinwai_zhuan.group('jingwai_zhuan')}")
        Total.append(i_jinwai_zhuan.group('Total_zhuan'))
        jingwai_zhuan = ',' + i_jinwai_zhuan.group('jingwai_zhuan')  # 各个省份境外输入病例的情况,加个逗号未来方便正则表达式匹配
    print(jingwai_zhuan)
    judge_jingwai_zhuan = re.search('均在', jingwai_zhuan)  # 搜索不到则返回None
    if judge_jingwai_zhuan == None:
        obj_jingwai_zhuan_1 = re.compile(".?(?P<Province>\D{1,})(?P<cases>\d{1,})例")
        jingwai_zhuan_1 = obj_jingwai_zhuan_1.finditer(jingwai_zhuan)
        for i_jinwai_zhuan_1 in jingwai_zhuan_1:
            Province.append(i_jinwai_zhuan_1.group("Province"))
            cases.append(i_jinwai_zhuan_1.group("cases"))
        data1['省份'] = Province
        data1['境外输入无症状转确诊'] = cases
    else:
        data1['省份'] = [jingwai_zhuan[3:]]
        data1['境外输入无症状转确诊'] = Total
    print(data1)
except:
    print('无境外无症状转确诊')
# ===========================================================================================
# 解析本土确诊
data2 = pd.DataFrame({"省份": [], "本土确诊": []})  # 创建空数据框
try:
    obj_quezheng = re.compile(f'31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例.*?例。.*?；本土病例(?P<Total_ben>.*?)例（(?P<bentu>.*?)）')
    quezheng = obj_quezheng.finditer(page_content2)
    Total = []  # 存本土确诊总数
    Province = []  # 存放省份名
    cases = []  # 存放病例数
    for i_quezhen in quezheng:
        print(f"本土确诊情况：{i_quezhen.group('bentu')}")
        Total.append(i_quezhen.group('Total_ben'))
        quezheng = ',' + i_quezhen.group('bentu')  # 各个省份境外输入病例的情况,加个逗号未来方便正则表达式匹配
    print(quezheng)
    judge_quezheng = re.search('均在', quezheng)  # 搜索不到则返回None
    print(judge_quezheng)
    if judge_quezheng == None:
        obj_quezheng_1 = re.compile(".?(?P<Province>\D{1,})(?P<cases>\d{1,})例")
        quezheng_1 = obj_quezheng_1.finditer(quezheng)
        for i_quezhen_1 in quezheng_1:
            print(i_quezhen_1.group("Province"), i_quezhen_1.group("cases"))
            Province.append(i_quezhen_1.group("Province"))
            cases.append(i_quezhen_1.group("cases"))
        data2['省份'] = Province
        data2['本土确诊'] = cases
    else:
        data2['省份'] = [quezheng[3:]]
        data2['本土确诊'] = Total
    print(data2)
except:
    print("无本土确诊病例")
# ===============================================================================================
# 本土无症状转确诊解析
data3 = pd.DataFrame({"省份": [], "本土无症状转确诊": []})  # 创建空数据框
try:
    obj_quezheng_zhuan = re.compile(
        f'31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例.*?例。.*?本土病例.*?例（.*?），含(?P<Total_ben_zhuan>.*?)例由无症状感染者转为确诊病例（(?P<bentu_zhuan>.*?)）')
    quezheng_zhuan = obj_quezheng_zhuan.finditer(page_content2)
    Total = []  # 存本土确诊总数
    Province = []  # 存放省份名
    cases = []  # 存放病例数
    for i_quezhen_zhuan in quezheng_zhuan:
        print(f"本土无症状情况：{i_quezhen_zhuan.group('bentu_zhuan')}")
        Total.append(i_quezhen_zhuan.group('Total_ben_zhuan'))
        quezheng_zhuan = ',' + i_quezhen_zhuan.group('bentu_zhuan')  # 各个省份境外输入病例的情况,加个逗号未来方便正则表达式匹配
    print(quezheng_zhuan)
    judge_quezheng_zhuan = re.search('均在', quezheng_zhuan)  # 搜索不到则返回None
    print(judge_quezheng_zhuan)
    if judge_quezheng_zhuan == None:
        obj_quezheng_zhuan_1 = re.compile(".?(?P<Province>\D{1,})(?P<cases>\d{1,})例")
        quezheng_zhuan_1 = obj_quezheng_zhuan_1.finditer(quezheng_zhuan)
        for i_quezhen_zhuan_1 in quezheng_zhuan_1:
            print(i_quezhen_zhuan_1.group("Province"), i_quezhen_zhuan_1.group("cases"))
            Province.append(i_quezhen_zhuan_1.group("Province"))
            cases.append(i_quezhen_zhuan_1.group("cases"))
        data3['省份'] = Province
        data3['本土无症状转确诊'] = cases
    else:
        data3['省份'] = [quezheng_zhuan[3:]]
        data3['本土无症状转确诊'] = Total
    print(data3)
except:
    print('无本土无症状转确诊病例')
# ==================================================================================================
# 境外输入无症状感染者解析
data4 = pd.DataFrame({"省份": [], "境外输入无症状感染者": []})  # 创建空数据框
try:
    obj_wu_jinwai = re.compile(f'31个省（自治区、直辖市）和新疆生产建设兵团报告新增无症状感染者.*?例，其中境外输入(?P<wu_jinwai>.*?)例')
    wu_jinwai = obj_wu_jinwai.finditer(page_content2)
    Province = ['境外输入无症状总计数']  # 存放省份名
    cases = []  # 存放病例数
    for i_wu_jinwai in wu_jinwai:
        print(f"境外输入无症状感染者情况：{i_wu_jinwai.group('wu_jinwai')}")
        cases.append(i_wu_jinwai.group('wu_jinwai'))
    data4['省份'] = Province
    data4["境外输入无症状感染者"] = cases
    print(data4)
except:
    print('无境外输入无症状感染者！')
# ====================================================================================================
# 本土无症状解析
data5 = pd.DataFrame({"省份": [], "本土新增无症状": []})  # 创建空数据框
try:
    # obj_wu_bentu = re.compile(f'31个省（自治区、直辖市）和新疆生产建设兵团报告新增无症状感染者.*?例，其中境外输入.*?例，本土(?P<Total_wu>.*?)例（(?P<bentu_wu>.*?)）')
    obj_wu_bentu = re.compile(
        f'31个省（自治区、直辖市）和新疆生产建设兵团报告新增无症状感染者.*?例，.*?本土(?P<Total_wu>.*?)例（(?P<bentu_wu>.*?)）')
    wu_bentu = obj_wu_bentu.finditer(page_content2)
    Total = []  # 存本土无症状总数
    Province = []  # 存放省份名
    cases = []  # 存放病例数
    for i_wu_bentu in wu_bentu:
        print(f"本土无症状情况：{i_wu_bentu.group('bentu_wu')}")
        Total.append(i_wu_bentu.group('bentu_wu'))
        wu_bentu = ',' + i_wu_bentu.group('bentu_wu')  # 各个省份境外输入病例的情况,加个逗号未来方便正则表达式匹配
    print(wu_bentu)
    judge_wu_bentu = re.search('均在', wu_bentu)  # 搜索不到则返回None
    print(judge_wu_bentu)
    if judge_wu_bentu == None:
        obj_wu_bentu_1 = re.compile(".?(?P<Province>\D{1,})(?P<cases>\d{1,})例")
        wu_bentu_1 = obj_wu_bentu_1.finditer(wu_bentu)
        for i_wu_bentu_1 in wu_bentu_1:
            print(i_wu_bentu_1.group("Province"), i_wu_bentu_1.group("cases"))
            Province.append(i_wu_bentu_1.group("Province"))
            cases.append(i_wu_bentu_1.group("cases"))
        data5['省份'] = Province
        data5['本土新增无症状'] = cases
    else:
        data5['省份'] = [wu_bentu[3:]]
        data5['本土新增无症状'] = Total
    print(data5)
except:
    print("无本土新增无症状感染者！")
# ============================================================================================================
# 横向合并全部
data_list = [data1, data4, data2, data5, data3]
for i in data_list:
    data0 = pd.merge(data0, i, how='outer', on='省份')
data0.fillna(0, inplace=True)  # 替换空值为0
number_lie = data0.shape[0]  # 获取行数
date_file = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取当天日期
Year = [date_file.split('-')[0]] * number_lie
Month = [date_file.split('-')[1]] * number_lie
Day = [date_file.split('-')[2]] * number_lie
data0['年'] = Year
data0['月'] = Month
data0['日'] = Day
print(data0)
# ========================================================================================
data0.to_csv(rf"{Desktop_path}\{select_date}.csv", encoding='gbk', index=False)


# =========================================================================================
data_list2 = [data5, data3]
for i in data_list2:
    data2 = pd.merge(data2, i, how='outer', on='省份')
data2.fillna(0, inplace=True)  # 替换空值为0
print(data2)
number_lie2 = data2.shape[0]  # 获取行数
data2['本土确诊'] = data2['本土确诊'].astype(int)  # 转换该列的数据类型
data2['本土新增无症状'] = data2['本土新增无症状'].astype(int)  # 转换该列的数据类型
data2['本土无症状转确诊'] = data2['本土无症状转确诊'].astype(int)  # 转换该列的数据类型
data2['合计'] = data2['本土确诊']+data2['本土新增无症状']-data2['本土无症状转确诊']
Year2 = [date_file.split('-')[0]]*number_lie2
Month2 = [date_file.split('-')[1]]*number_lie2
Day2 = [date_file.split('-')[2]]*number_lie2
data2['年'] = Year2
data2['月'] = Month2
data2['日'] = Day2
print(data2)
data2.to_csv(rf"{Desktop_path}\{select_date}_国内.csv", encoding='gbk', index=False)
print(f'文件已输出至桌面，文件名为：{select_date}.csv')
