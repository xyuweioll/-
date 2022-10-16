import pandas as pd
import numpy as np
import os
pro_name = input('请输入您要查询的省份名：')
year = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
        '2019', '2020']
path = 'C:\\Users\\xianyu\\Desktop\\'+pro_name  # 指定创建文件夹的路径，更具实际情况更改

os.mkdir(path)     # 在指定路径创建相应省份的文件夹用于存放筛选后的文件
# ____________________________________________________________________________
# GST模块
os.chdir('D:\\Climate\\SELECT-month')   # 指定SELECT文件夹存放的路径，根据实际情况更改
GST_N = '地温(GST)-'
for i in year:
        GST_N_S = GST_N+i+'.csv'      # 循环生成读取文件的路径加名称
        file = pd.read_csv(GST_N_S)   # 读取文件
        file_out = file[file['省份'] == pro_name]  # 根据字段’省份‘进行筛选
        path_out = path + '\\'+pro_name+GST_N+i+'.csv'
        file_out.to_csv(path_out, index=False)      # 将筛选文件输出到之前创建的文件夹中
print('模块1执行完毕')
# -----------------------------------------------------------------------------
# WIN模块
WIN_N = '风向风速(WIN)-'
for i in year:
        WIN_N_S = WIN_N+i+'.csv'
        file = pd.read_csv(WIN_N_S)
        file_out = file[file['省份'] == pro_name]
        path_out = path + '\\'+pro_name+WIN_N+i+'.csv'
        file_out.to_csv(path_out, index=False)
print('模块2执行完毕')
# -----------------------------------------------------------------------------
# PRE模块
PRE_N = '降水(PRE)-'
for i in year:
        PRE_N_S = PRE_N+i+'.csv'
        file = pd.read_csv(PRE_N_S)
        file_out = file[file['省份'] == pro_name]
        path_out = path + '\\'+pro_name+PRE_N+i+'.csv'
        file_out.to_csv(path_out, index=False)
print('模块3执行完毕')
# ------------------------------------------------------------------------------
# PRS模块
PRS_N = '气压(PRS)-'
for i in year:
        PRS_N_S = PRS_N+i+'.csv'
        file = pd.read_csv(PRS_N_S)
        file_out = file[file['省份'] == pro_name]
        path_out = path + '\\'+pro_name+PRS_N+i+'.csv'
        file_out.to_csv(path_out, index=False)
print('模块4执行完毕')
# ------------------------------------------------------------------------------
# SSD模块
SSD_N = '日照(SSD)-'
for i in year:
        SSD_N_S = SSD_N+i+'.csv'
        file = pd.read_csv(SSD_N_S)
        file_out = file[file['省份'] == pro_name]
        path_out = path + '\\'+pro_name+SSD_N+i+'.csv'
        file_out.to_csv(path_out, index=False)
print('模块5执行完毕')
# ------------------------------------------------------------------------------
# TEM模块
TEM_N = '温度(TEM)-'
for i in year:
        TEM_N_S = TEM_N+i+'.csv'
        file = pd.read_csv(TEM_N_S)
        file_out = file[file['省份'] == pro_name]
        path_out = path + '\\'+pro_name+TEM_N+i+'.csv'
        file_out.to_csv(path_out, index=False)
print('模块6执行完毕')
# ------------------------------------------------------------------------------
# RHU模块
RHU_N = '相对湿度(RHU)-'
for i in year:
        RHU_N_S = RHU_N+i+'.csv'
        file = pd.read_csv(RHU_N_S)
        file_out = file[file['省份'] == pro_name]
        path_out = path + '\\'+pro_name+RHU_N+i+'.csv'
        file_out.to_csv(path_out, index=False)
print('模块7执行完毕')
# ------------------------------------------------------------------------------
# EVP模块
EVP_N = '蒸发(EVP)-'
for i in year:
        EVP_N_S = EVP_N+i+'.csv'
        file = pd.read_csv(EVP_N_S)
        file_out = file[file['省份'] == pro_name]
        path_out = path + '\\'+pro_name+EVP_N+i+'.csv'
        file_out.to_csv(path_out, index=False)
print('模块8执行完毕')
print('程序执行完毕')