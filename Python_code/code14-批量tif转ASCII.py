# coding=utf-8
# 注：输出路径中若有中文则可能会报错，输入路径中可含有中文
import arcpy
from arcpy import env
import os
env_path = str(raw_input('please input the path you store your tif files\n===>>>'))
out_path = str(raw_input('please input the path you store your output ascii files\n===>>> '))
# python 2 与 python3在输入函数的使用上存在区别，
# Python 2.7  raw_input()  input() 都存在 可使用    raw_input()接收字符串string  input()接收数字int /flot.
# Python 3  raw_input()不存在  仅存在input()   两者合并  接收任意格式 返回string
print '工作空间已设定为: {}'.format(env_path)
print '正在读取文件......'
arcpy.env.workspace = env_path          # 设定工作空间
rasters = arcpy.ListRasters("*", "tif")  # 获取所有以tif结尾的文件名
for inRaster in rasters:
    print inRaster[:-4]
    outASCII = out_path+'\\'+inRaster[:-4].encode("utf-8")+'.asc'
    print outASCII
# # Execute RasterToASCII
    arcpy.RasterToASCII_conversion(inRaster, outASCII)
    # print '{} has been done,please check!'.format(outASCII.encode('utf-8'))
    print '{} has been done,please check!'.format(outASCII)

print 'finished!'
