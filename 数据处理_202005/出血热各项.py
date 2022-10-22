import pandas as pd
data = pd.read_csv(r'G:\全国肺结核_20220526\肺结核_1\肺结核_分年横向.csv', encoding='utf-8')
print(data.head(5))
num_cases = pd.DataFrame(data['地区'])
in_cases = pd.DataFrame(data['地区'])
num_died = pd.DataFrame(data['地区'])
in_died = pd.DataFrame(data['地区'])

for i in range(2005, 2022):
    num_cases[f'{i}发病数'] = data[f'{i}发病数']
    in_cases[f'{i}发病率'] = data[f'{i}发病率']
    num_died[f'{i}死亡数'] = data[f'{i}死亡数']
    in_died[f'{i}死亡率'] = data[f'{i}死亡率']

num_cases.to_csv(r'G:\全国肺结核_20220526\肺结核_1\肺结核发病数.csv', index=False)
in_cases.to_csv(r'G:\全国肺结核_20220526\肺结核_1\肺结核发病率.csv', index=False)
num_died.to_csv(r'G:\全国肺结核_20220526\肺结核_1\肺结核死亡数.csv', index=False)
in_died.to_csv(r'G:\全国肺结核_20220526\肺结核_1\肺结核死亡率.csv', index=False)

