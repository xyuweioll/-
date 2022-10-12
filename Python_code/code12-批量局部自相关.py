# coding=utf-8
# 使用的是工具箱里的Spatial Statistics Tools -> Mapping Clusters -> Cluster and Outlier Anselin(Anseline Local Morans I)
import arcpy
arcpy.env.overwriteOutput = True   # 若指定路径存在同名文件则覆盖之
env_path = str(raw_input('please input the path you store your shp files\n===>>>'))
file_name = str(raw_input('please input the file name of shp file\n===>>>'))
arcpy.env.workspace = env_path          # 设定工作空间
out_path = str(raw_input('please input the path you store your output shp files\n===>>> '))
strat_field = int(input('please enter the sequence number for the start field\n===>>>'))
end_field = int(input('please enter the sequence number for the ended field\n===>>>'))  # 直到最后一个字段则输入-1
# python 2 与 python3在输入函数的使用上存在区别，
# Python 2.7  raw_input()  input() 都存在 可使用    raw_input()接收字符串string  input()接收数字int /flot.
# Python 3  raw_input()不存在  仅存在input()   两者合并  接收任意格式 返回string
fields = arcpy.ListFields(file_name)  # 获取所有列名
for i in fields[strat_field-1:end_field]:
    print i.name+'  is doing'
    out_shp = out_path+'\\'+i.name.encode('utf-8')+'病数局部自相关.shp'  # 输出路径及文件名
    arcpy.ClustersOutliers_stats(file_name, i.name, out_shp,
                                 "CONTIGUITY_EDGES_CORNERS", "#",
                                 "NONE", "#", "#", "NO_FDR", 999)
    print '{} has been done,please check!'.format(i.name.encode('utf-8'))  # 字段名字包含中文时才需要utf-8编码

print 'finished!'

