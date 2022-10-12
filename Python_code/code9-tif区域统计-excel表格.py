# coding=utf-8
# Name: ZonalStatisticsAsTable_Ex_02.py
# Description: Summarizes values of a raster within the zones of
#              another dataset and reports the results to a table.
# Requirements: Spatial Analyst Extension
# Import system modules

import arcpy
from arcpy import env
from arcpy.sa import *
import sys, string, os
import arcgisscripting

file_path_dbf = "G:\\Zonal_Statistic\\Anhui_Zonal_year_dbf"  # dbf文件存放路径
# ========================================================================================================
# Set environment settings
# 第一步：完成zonal statistic,并生成dbf文件
env.workspace = "G:\\tif\\Anhui_tif_year_mean_Albers"
rasters = arcpy.ListRasters("*", "tif")  # 获取所有以tif结尾的文件
print rasters
# Set local variables
inZoneData = "G:\\Artical-1\\Map\\安徽县级.shp"  # 底图
zoneField = "CNTY_COD_1"             # zoneField字段不支持中文，字段里不要出现中文，不然那一列全为空值
for inValueRaster in rasters:
    outTable = file_path_dbf +"\\{}.dbf".format(inValueRaster[:-4].encode('utf-8'))
    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    # Execute ZonalStatisticsAsTable
    outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, inValueRaster,
                                     outTable, "DATA", "MEAN")      # 其无法覆盖已经存在的同名文件
    print "{} has been finished!".format(inValueRaster.encode('utf-8'))

# ============================================================================================================
# 第二步，在第一步的基础上将dbf文件转为excel表格形式
arcpy.env.workspace = file_path_dbf
files = os.listdir(file_path_dbf)
file_path_excel = "G:\\Zonal_Statistic\\Anhui_Zonal_year_excel"
for in_table in files:
    if os.path.splitext(in_table)[1] == '.dbf':  # 判断文件扩展名是不是为.dbf  os.path.splitext(“文件路径”)
        #        print in_table
        #                                                           # 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作
        #Set local variable
        out_xls = file_path_excel+"\\{}.xls".format(in_table[:-4])
        # Execute TableToExcel
        arcpy.TableToExcel_conversion(in_table, out_xls)
        print "The excel of {} had done".format(in_table)
