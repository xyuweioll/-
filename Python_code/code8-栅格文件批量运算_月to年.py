# coding=utf-8
import arcpy
from arcpy.sa import *
import os
import shutil

arcpy.CheckOutExtension("spatial")  # 查看ArcGIS Spatial Analyst扩展模块许可
arcpy.gp.overwriteOutput = True
inputpath = 'G:\\tif\\Dongbei-tif_1'  # tif文件存放路径   G:\tif\Anhui_tif
# =====================================================================================================
# 第一步\将1年的气象tif放入一个文件夹
arcpy.env.workspace = inputpath           # 设定工作空间
rasters = arcpy.ListRasters("*", "tif")  # 获取所有以tif结尾的文件名
for raster in rasters:                   # 遍历文件名列表，每一年每一类气象tif建立一个文件夹，并将文件移进去
    move_path = inputpath+"\\"+raster    # tif文件完整路径加名称
    if raster[:3] =='PRE':
        outpath = inputpath + "\\" +raster[:5]+raster[-9:-5]   # tif文件要移入的完整路径
        if not os.path.exists(outpath):  # 如果输入文件夹不存在则创建文件夹
            os.makedirs(outpath)         # 建立文件夹
            print 'ok!'
        shutil.move(move_path, outpath)             # 移动文件到相应目录
    else:
        outpath = inputpath + "\\" + raster[:5] + raster[-7:-4]
        if not os.path.exists(outpath):     # 如果输入文件夹不存在则创建文件夹
            os.makedirs(outpath)            # 建立文件夹
            print raster[-7:-4]
        shutil.move(move_path, outpath)     # 移动文件到相应目录
print ('............................Step one is finished........................')
# =============================================================================================
# 第二步\求平均值或求和
aa = 0
for parent, dirnames, filenames in os.walk(inputpath):
    print 'dirnames have gotten!'
    print dirnames
    if aa == 0:
        foldlist = dirnames  # 获取文件夹名
    aa += 1
    print aa
print foldlist
for workpath in foldlist:
    #print 'ok'
    #print workpath
    if workpath[:3] == "PRE":
        env_path = inputpath + '\\' + workpath.encode('utf-8')
        print "workpath is "+env_path
        arcpy.env.workspace = env_path   # tif文件存放路径   G:\tif\Anhui_tif
        rasters = arcpy.ListRasters("*", "tif")  # 获取所有以tif结尾的文件名
        print rasters
        for raster in rasters:
            print raster
        try:
            outCellStatistics = CellStatistics(rasters, "SUM", "DATA")  # MEAN(均值)\MAJORITY(众数)\MAXIMUM(最大值)\MEDIAN(中值)\
                                                             # MINIMUM(最小值)\MINORITY(少数)\RANGE(范围：最大值-最小值)\
                                                            # STD(标准差)\SUM(总和)\VARIETY(变异度:唯一值的数量).
        except:
            print workpath +"is something wrong"

        outCellStatistics.save('G:\\tif\\result\\' + workpath + '.tif')  # 运算结果存放目录加文件名
    else:
        arcpy.env.workspace = inputpath + "\\" + workpath  # tif文件存放路径   G:\tif\Anhui_tif
        rasters = arcpy.ListRasters("*", "tif")  # 获取所有以tif结尾的文件名
        outCellStatistics = CellStatistics(rasters, "MEAN", "DATA")  # MEAN(均值)\MAJORITY(众数)\MAXIMUM(最大值)\MEDIAN(中值)\
        print workpath                                                                # MINIMUM(最小值)\MINORITY(少数)\RANGE(范围：最大值-最小值)\
                                                                         # STD(标准差)\SUM(总和)\VARIETY(变异度:唯一值的数量).
        outCellStatistics.save('G:\\tif\\result\\' + workpath + '.tif')  # 运算结果存放目录加文件名

print ('Finished!')





# arcpy.env.workspace = r'G:\tif\test'           # tif文件存放路径
# rasters = arcpy.ListRasters("*", "tif")  # 获取所有以tif结尾的文件
# outpath='C:\\Users\\xianyu\\Desktop\\批量运算\\'
# outCellStatistics = CellStatistics(rasters, "MAXIMUM", "DATA")
# # sum1 = 0
# # for raster in rasters:
# #     print raster[:5].encode('utf-8')
# #     print raster[-7:-4].encode('utf-8')
# #     sum1 += Raster(raster)
# # sum1 = sum1/len(rasters)
# # sum1.save(outpath+'sum6.tif')
# outCellStatistics.save(outpath+'sum4.tif')
#
#
# # for type_cl in ['EVP','GST','PRE','PRS','RHU','SSD','TEM','WIN']:
# #     for yea
