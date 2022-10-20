import re
import pandas as pd
import winreg
import datetime
# 定义自动获取桌面路径函数
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
    return winreg.QueryValueEx(key, "Desktop")[0]  # 返回的是Unicode类型数据


Desktop_path = str(get_desktop())  # Unicode转化为str,获取桌面路径

# ============================================================================================
f = open(rf'{Desktop_path}\网页.txt', mode='r', encoding='utf-8')
page_content2 = f.read()
f.close()

# ==========================================================================================
print(page_content2)
page_content2 = page_content2.replace('<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">', '')
page_content2 = page_content2.replace('</span>', '')
print(page_content2)
# 解析境外确诊病例
data0 = pd.DataFrame({"省份": [], "境外输入确诊": []})  # 创建空数据框
try:
    obj_jingwai = re.compile(f"31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例.*?例。其中境外输入病例(?P<Total_confirm>.*?)例（(?P<comfirm_jinwai>.*?)）")
    jingwai = obj_jingwai.finditer(page_content2)
    Total = []  # 存放境外无症状转确诊总数
    Province = []  # 存放省份名
    cases = []    # 存放病例数
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
    print(data0)
except:
    print('无境外输入确诊病例')
# ==========================================================================================
# 境外无症状转确诊数据解析
data1 = pd.DataFrame({"省份": [], "境外输入无症状转确诊": []})  # 创建空数据框
try:
    obj_jingwai_zhuan = re.compile(f"31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例.*?例。.*?，含(?P<Total_zhuan>.*?)例由无症状感染者转为确诊病例（(?P<jingwai_zhuan>.*?)）")
    jingwai_zhuan = obj_jingwai_zhuan.finditer(page_content2)
    Total = []  # 存放境外无症状转确诊总数
    Province = []  # 存放省份名
    cases = []    # 存放病例数
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
    cases = []    # 存放病例数
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
    obj_quezheng_zhuan = re.compile(f'31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例.*?例。.*?本土病例.*?例（.*?），含(?P<Total_ben_zhuan>.*?)例由无症状感染者转为确诊病例（(?P<bentu_zhuan>.*?)）')
    quezheng_zhuan = obj_quezheng_zhuan.finditer(page_content2)
    Total = []  # 存本土确诊总数
    Province = []  # 存放省份名
    cases = []    # 存放病例数
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
    cases = []    # 存放病例数
    for i_wu_jinwai in wu_jinwai:
        print(f"境外输入无症状感染者情况：{i_wu_jinwai.group('wu_jinwai')}")
        cases.append(i_wu_jinwai.group('wu_jinwai'))
    data4['省份'] = Province
    data4["境外输入无症状感染者"] =cases
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
    cases = []    # 存放病例数
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
# 横向合并
data_list = [data1, data4, data2, data5, data3]
for i in data_list:
    data0 = pd.merge(data0, i, how='outer', on='省份')
data0.fillna(0, inplace=True)  # 替换空值为0
number_lie = data0.shape[0]  # 获取行数
date_file = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取当天日期
Year = [date_file.split('-')[0]]*number_lie
Month = [date_file.split('-')[1]]*number_lie
Day = [date_file.split('-')[2]]*number_lie
data0['年'] = Year
data0['月'] = Month
data0['日'] = Day
print(data0)
# ========================================================================================
data0.to_csv(rf"{Desktop_path}\{date_file}.csv", encoding='gbk', index=False)

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
data2.to_csv(rf"{Desktop_path}\{date_file}_国内.csv", encoding='gbk', index=False)

