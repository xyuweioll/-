# coding=utf-8
import arcpy
arcpy.env.workspace = '\\'           # tif文件存放路径
rasters = arcpy.ListRasters("*", "tif")  # 获取所有以tif结尾的文件
print rasters
mask = 'G:\\Artical-1\\Map\\Anhui_WGS_1984.shp'   # 裁切地图存放路径(即底图)
for raster in rasters:
    out_path = '\\'                   # 裁切后的tif文件存放路径加名称
    arcpy.gp.ExtractByMask_sa(raster, mask, out_path)
    print ('{}裁剪已完成'.format()).decode('utf-8').encode('gbk')
