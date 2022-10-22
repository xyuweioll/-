import pandas as pd
data = pd.read_csv(r'G:\全国肺结核_20220526\肺结核_1\分地区_总发病.csv', encoding='gbk')
print(data.head(5))
year_list = set(data['年份'])  # 提取年份信息
print(year_list)
data_frame_list = []  # 根据年份逐年筛选
for year in year_list:
    frame = data[data['年份'] == year]
    frame.rename(columns={'年份': f'{year}', '肺结核发病数': f'{year}发病数', '肺结核死亡数': f'{year}死亡数', '肺结核发病率': f'{year}发病率', '肺结核死亡率': f'{year}死亡率'}, inplace=True)
    data_frame_list.append(frame)

first_file = data_frame_list[0]
for i in range(1, len(data_frame_list)):
    print(i)
    first_file = pd.merge(first_file, data_frame_list[i], left_on='地区', right_on='地区', how='outer')
first_file.to_csv('C:\\Users\\xianyu\\Desktop\\肺结核.csv', index=False)
print('文件已输出')


# 逐年纵向合并


