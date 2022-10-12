# coding=utf-8
import arcpy
arcpy.env.workspace = str(raw_input('please input the path you store your tif files\n===>>>'))    # 输入tif文件存放路径            # tif文件存放路径
rasters = arcpy.ListRasters("*", "tif")  # 获取所有以tif结尾的文件
print rasters
mask = str(raw_input('please input the path you store your coordinates reference files\n===>>>'))   # 参考文件路径    # 裁切地图存放路径(即底图)
for raster in rasters:
    print raster.encode('utf-8')
    out_path = r'G:\fujian_20220530\Maxent\tif\NDVI_2\{}'.format(raster.encode('utf-8'))                   # 裁切后的tif文件存放路径加名称
    arcpy.gp.ExtractByMask_sa(raster, mask, out_path)
    print ('{}裁剪已完成'.format(raster.encode('utf-8')))
