import pandas as pd

data = pd.read_csv(r'C:\Users\xianyu\Desktop\工作簿1.csv')

data['筛选'] = [1 if 'Viruses|p' in i else 0 for i in data['需筛选列']]  # 给数据框添加一列用于筛选的列
select_frame = data[data['筛选'] == 1]
select_frame.to_csv(r'C:\Users\xianyu\Desktop\工作簿2.csv', index=False)
