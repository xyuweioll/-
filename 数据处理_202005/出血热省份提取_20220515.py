import pandas as pd
data = pd.read_csv(r'G:\全国肺结核_20220526\肺结核_1\分地区_总发病.csv', encoding='gbk')
print(data.head(5))
zone_list = set(data['地区'])  # 提取地区信息
print(zone_list)
data_frame_list = []  # 根据年份逐年筛选
for zone in zone_list:
    frame = data[data['地区'] == zone]
    frame.rename(columns={'地区': f'{zone}', '肺结核发病数': f'{zone}发病数', '肺结核死亡数': f'{zone}死亡数', '肺结核发病率': f'{zone}发病率', '肺结核死亡率': f'{zone}死亡率'}, inplace=True)
    data_frame_list.append(frame)

first_file = data_frame_list[0]
for i in range(1, len(data_frame_list)):
    print(data_frame_list[i])
    first_file = pd.merge(first_file, data_frame_list[i], left_on='年份', right_on='年份', how='outer')
first_file.to_csv('C:\\Users\\xianyu\\Desktop\\肺结核分省_横向.csv', index=False)
print('文件已输出')


# 逐年纵向合并


