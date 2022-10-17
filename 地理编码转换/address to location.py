# 需在联网情况下运行
import sys
import pandas as pd
import requests
import os.path
import time
import math
import winreg
# ===========================================================================================
# 定义自动获取桌面路径函数
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
    return winreg.QueryValueEx(key, "Desktop")[0]  # 返回的是Unicode类型数据


Desktop_path = str(get_desktop())  # Unicode转化为str,获取桌面路径

# ============================================================================================
# 坐标转换
x_pi = float(3.14159265358979324 * 3000.0 / 180.0)
# //pai
pi = float(3.1415926535897932384626)
# //离心率
ee = float(0.00669342162296594323)
# //长半轴
a = float(6378245.0)


# //百度转国测局
def bd09togcj02(bd_lon, bd_lat):
    x = (bd_lon - 0.0065)
    y = (bd_lat - 0.006)
    z = (math.sqrt(x * x + y * y)) - (0.00002 * math.sin(y * x_pi))
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return gg_lng, gg_lat


# //国测局转百度
def gcj02tobd09(lng, lat):
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return bd_lng, bd_lat


# //国测局转84
def gcj02towgs84(lng, lat):
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


# //经度转换
def transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + 0.1 * lng * lat + 0.2 * math.sqrt(abs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 * math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 * math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 * math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


# //纬度转换
def transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + 0.1 * lng * lat + 0.1 * math.sqrt(abs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 * math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 * math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 * math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def getWgs84xy(x, y):
    # //先转 国测局坐标
    doubles_gcj = bd09togcj02(x, y)
    # //（x 117.   y 36. ）
    # //国测局坐标转wgs84
    doubles_wgs84 = gcj02towgs84(doubles_gcj[0], doubles_gcj[1])
    # //返回 纠偏后 坐标
    return doubles_wgs84


#  =============================================================================================

AK = "47fnvrEVHmsG0SVIuwYPkbWEOPq1BARz"  # 将刚刚获取到的AK复制到这里


# =============================================================================================
# 定义获取经纬度函数
# 百度地理编码服务文档详细请查看网址：https://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding
# 默认返回百度经纬度坐标(bd09II)，WGS1984需要进一步转换
def get_position(name, AK):
    url = f'http://api.map.baidu.com/geocoding/v3/?address={name}&output=json&ak={AK}'
    while True:
        try:
            res = requests.get(url)
            print(f'{name}finished!')
            break
        except:
            print('sleep for 1 seconds')
            time.sleep(1)
            continue
    val = res.json()
    print(val)
    retval = {'地址': name,
              '经度': val['result']['location']['lng'],
              '维度': val['result']['location']['lat'],
              '地区标签': val['result']['level'],
              '是否精确查找': val['result']['precise']}
    longitude = retval['经度']
    latitude = retval['维度']
    level_1 = retval['地区标签']
    select_type = retval['是否精确查找']
    return longitude, latitude, level_1, select_type, val


# ===========================================================================================================
# 转换，文件批量转换
transform_type = input('选择转换类型：1 单个地址转换；2 通过文件特定列批量转换转换\n===>>>')
if transform_type == '2':
    file_path = input('请输入文件路径及文件名\n===>>>')
    lieming = input('请输入存放地址的列名\n===>>>')
    if os.path.splitext(file_path)[1] == '.xlsx':
        dataSet = pd.read_excel(file_path)
    elif os.path.splitext(file_path)[1] == '.csv' or os.path.splitext(file_path)[1] == '.txt':
        dataSet = pd.read_csv(file_path)
    else:
        print('本程序仅支持excel文件、csv文件或txt文件！')
        sys.exit()
    # --------------------------------------------------------------
    # 批量转换 C:\Users\xianyu\Desktop\肖\未知经纬度.xlsx  海南省文昌市迈陈村
    df = dataSet[lieming]
    print(df)
    df_location = df.apply(get_position, args=(AK,))  # 参数AK需要通过参数传入
    print(df_location)  # df_location 传回的是元组
    dataSet["经度_百度"] = df_location.map(lambda x: x[0])
    dataSet["纬度_百度"] = df_location.map(lambda x: x[1])
    dataSet["地区标签"] = df_location.map(lambda x: x[2])
    dataSet["是否精确查找"] = df_location.map(lambda x: x[3])
    df_location_wgs_x = []
    df_location_wgs_y = []
    for i in range(len(dataSet["经度_百度"])):
        xx = dataSet["经度_百度"].iloc[i]
        yy = dataSet["纬度_百度"].iloc[i]
        wgs = getWgs84xy(xx, yy)  # 返回列表
        print(wgs)
        df_location_wgs_x.append(wgs[0])
        df_location_wgs_y.append(wgs[1])
    dataSet["经度_wgs"] = df_location_wgs_x
    dataSet["纬度_wgs"] = df_location_wgs_y
    output_path = Desktop_path+'\\经纬度输出.csv'
    dataSet.to_csv(output_path, index=False)  # encoding='gbk',
    print('文件已经输出，请至桌面查看！')
# =====================================================================================================
# 单个地址转换
else:
    addr = input('请输入需要查询的地址\n===>>>')
    lo, la, le, se, val2 = get_position(addr, AK)
    print(f'{addr}的百度经度为：{lo}，百度纬度为：{la}, 地区标签：{le}')
    wgs = getWgs84xy(lo, la)
    print(f'{addr}的wgs经度为：{wgs[0]}，wgs纬度为：{wgs[1]}')

