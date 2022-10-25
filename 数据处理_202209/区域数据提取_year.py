import pandas as pd
# import numpy as np
# import win32com.client as win32
import os
# =====================================================================================================
workpath =r'G:\A_Hainan_20220321\Stata\excel'  #存放excel的文件夹
os.chdir(workpath)   # 设定工作目录
filenames = os.listdir(workpath)  # 获取工作路径下所以文件名
file_list_evp_max = []
file_list_evp_min = []
file_list_gst_max = []
file_list_gst_avg = []
file_list_gst_min = []
file_list_pre_day = []
file_list_pre_nig = []
file_list_pre_all = []
file_list_prs_max = []
file_list_prs_avg = []
file_list_prs_min = []
file_list_rhu_avg = []
file_list_rhu_min = []
file_list_ssd = []
file_list_tem_max = []
file_list_tem_avg = []
file_list_tem_min = []
file_list_win_max = []
file_list_win_avg = []
file_list_win_mmax = []
# ==================================================================================================
for file in filenames:
    if os.path.splitext(file)[1] == '.xls':  # 判断文件扩展名是不是为.xls  os.path.splitext(“文件路径”)
        file_name = os.path.splitext(file)[0]   # 文件名，不含后缀
        print(os.path.splitext(file)[1])        # 后缀，拓展名
        print(f'正在读取文件{os.path.splitext(file)[0]}')
        print(file_name[-3:])
# ======================================================================================================
# 大型蒸发
        if file_name[:3] =='EVP' and file_name[-3:] =='大型蒸':                   # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            #print(re_file)
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 更改列名
            #print(re_file)
            file_list_evp_max.append(re_file)
# =======================================================================================================
# 小型蒸发
        elif file_name[:3] == 'EVP' and file_name[-3:] == '小型蒸':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 更改列名
            file_list_evp_min.append(re_file)
#  ========================================================================================================
# 地温日最高
        elif file_name[:3] == 'GST' and file_name[-3:] == '日最高':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)
            file_list_gst_max.append(re_file)
# ============================================================================================================
# 地温日最低
        elif file_name[:3] == 'GST' and file_name[-3:] == '日最低':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)
            file_list_gst_min.append(re_file)
# ==============================================================================================================
# 平均地温
        elif file_name[:3] == 'GST' and file_name[-3:] == '平均地':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)
            file_list_gst_avg.append(re_file)
# ===============================================================================================================
# # 降水8-20时
#         elif file_name[:3] == 'PRE' and file_name[-4:] == '8_20':  # 获取文件名（不包含后缀，后3位）
#             col_name = file_name[:-4]
#             re_file = pd.read_excel(file)
#             re_file = re_file[['CNTY_COD_1', 'SUM']]  # 选择特定列
#             re_file.rename(columns={'SUM': col_name}, inplace=True)  # 重命名列
#             file_list_pre_day.append(re_file)
# # ===============================================================================================================
# # 降水20-8时
#         elif file_name[:3] == 'PRE' and file_name[-4:] == '20_8':  # 获取文件名（不包含后缀，后3位）
#             col_name = file_name[:-4]
#             re_file = pd.read_excel(file)
#             re_file = re_file[['CNTY_COD_1', 'SUM']]  # 选择特定列
#             re_file.rename(columns={'SUM': col_name}, inplace=True)  # 重命名列
#             file_list_pre_nig.append(re_file)
# # ===============================================================================================================
# # 降水20_20时
#         elif file_name[:3] == 'PRE' and file_name[-4:] == '20_2':  # 获取文件名（不包含后缀，后3位）
#             col_name = file_name[:-4]
#             re_file = pd.read_excel(file)
#             re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
#             re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
#             file_list_pre_all.append(re_file)
# ===============================================================================================================
# 气压日最高
        elif file_name[:3] == 'PRS' and file_name[-3:] == '日最高':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_prs_max.append(re_file)
# ===============================================================================================================
# 气压日最低
        elif file_name[:3] == 'PRS' and file_name[-3:] == '日最低':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_prs_min.append(re_file)
# ===============================================================================================================
# 平均气压
        elif file_name[:3] == 'PRS' and file_name[-3:] == '平均本':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_prs_avg.append(re_file)
# ===============================================================================================================
# 平均相对湿度
        elif file_name[:3] == 'RHU' and file_name[-3:] == '平均相':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_rhu_avg.append(re_file)
# ===============================================================================================================
# 最小相对湿度
        elif file_name[:3] == 'RHU' and file_name[-3:] == '最小相':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_rhu_min.append(re_file)
# ===============================================================================================================
# 日照时长
        elif file_name[:3] == 'SSD' and file_name[-3:] == '日照时':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_ssd.append(re_file)
# ===============================================================================================================
# 日最高温度
        elif file_name[:3] == 'TEM' and file_name[-3:] == '日最高':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_tem_max.append(re_file)
# ================================================================================================================
# 日最低温度
        elif file_name[:3] == 'TEM' and file_name[-3:] == '日最低':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_tem_min.append(re_file)
# =================================================================================================================
# 日平均温度
        elif file_name[:3] == 'TEM' and file_name[-3:] == '平均气':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_tem_avg.append(re_file)
# =================================================================================================================
# 最大风
        elif file_name[:3] == 'WIN' and file_name[-3:] == '最大风':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_win_max.append(re_file)
# ==================================================================================================================
# 极大风
        elif file_name[:3] == 'WIN' and file_name[-3:] == '极大风':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_win_mmax.append(re_file)
# ==================================================================================================================
# 平均风
        elif file_name[:3] == 'WIN' and file_name[-3:] == '平均风':  # 获取文件名（不包含后缀，后3位）
            col_name = file_name[:-3]
            re_file = pd.read_excel(file)
            re_file = re_file[['CNTY_COD_1', 'MEAN']]  # 选择特定列
            re_file.rename(columns={'MEAN': col_name}, inplace=True)  # 重命名列
            file_list_win_avg.append(re_file)
# ==================================================================================================================
# 定义横向连接函数
def con_list(list_con, out_path, file_name):   # 第一个参数是输入列表，第二个参数是输出文件路径,第三文件名
    out_file = out_path+file_name+'.xlsx'
    fist_table = list_con[0]
    for i in range(1, len(list_con)):
        fist_table = pd.merge(fist_table, list_con[i], left_on='CNTY_COD_1', right_on='CNTY_COD_1', how="outer")
    fist_table.to_excel(out_file, index=False)
# ==================================================================================================================
# 文件输出
out_path = 'G:\\A_Hainan_20220321\\Stata\\panel_1\\'       #指定输出文件路径
con_list(file_list_evp_max, out_path, 'EVP_MAX')
con_list(file_list_evp_min, out_path, 'EVP_MIN')
print('EVP已输出')
con_list(file_list_gst_max, out_path, 'GST_MAX')
con_list(file_list_gst_min, out_path, 'GST_MIN')
con_list(file_list_gst_avg, out_path, 'GST_AVG')
print('GST已输出')
# con_list(file_list_pre_day, out_path, 'PRE_8_20时')
# con_list(file_list_pre_nig, out_path, 'PRE_20_8时')
# con_list(file_list_pre_all, out_path, 'PRE_20_20时')
# print('PRE已输出')
con_list(file_list_prs_max, out_path, 'PRS_MAX')
con_list(file_list_prs_min, out_path, 'PRS_MIN')
con_list(file_list_prs_avg, out_path, 'PRS_AVG')
print('PRS已输出')
con_list(file_list_rhu_min, out_path, 'RHU_MIN')
con_list(file_list_rhu_avg, out_path, 'RHU_AVG')
print('RHU已输出')
con_list(file_list_ssd, out_path, 'SSD')
print('SSD已输出')
con_list(file_list_tem_max, out_path, 'TEM_MAX')
con_list(file_list_tem_min, out_path, 'TEM_MIN')
con_list(file_list_tem_avg, out_path, 'TEM_AVG')
print('TEM已输出')
con_list(file_list_win_mmax, out_path, 'WIN_MMAX')
con_list(file_list_win_max, out_path, 'WIN_MAX')
con_list(file_list_win_avg, out_path, 'WIN_AVG')
print('WIN已输出')





