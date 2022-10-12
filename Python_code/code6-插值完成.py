# coding=utf-8
import arcpy
import os
import arcpy
from arcpy.sa import *
from arcpy import env
rootdir = u'C:\\Users\\xianyu\\Desktop\\csv'  # 存放文件的根目录
for parent, dirnames, filenames in os.walk(rootdir):   # 此时filenames 是一个存放了所有文件名的列表
    print('文件夹中共有{}个文件！'.format(len(filenames)))
arcpy.env.workspace ="C:\\Users\\xianyu\\Desktop\\csv"
env.extent = arcpy.Extent(-1684578.182212, -2462883.694315, 2651995.683691, 3113931.942137)  # 确定环境范围，分别为
                                                                                    # #（Left, Bottom, Right, Top  ）
# 这里的地图使用的是以 'Asia North Albers Equal Area Conic' 即 阿尔波斯投影的中国地图作为底图的范围
env.mask = r'D:\Climate\base_map\base_map.shp'    # 研磨地图存放路径
out_coordinate_system = arcpy.SpatialReference('Asia North Albers Equal Area Conic')  # 阿尔波斯投影
for name in filenames:
    print (name)
    select_name = name[1:4]    # 筛选的结果是：GST\PRE\RHU等，用于后面判断其属于哪一种气象数据文件，以对不同位置的字段进行插值
    print select_name
    if select_name == 'SSD':
        field_num = 1
    elif select_name == 'RHU':
        field_num = 2
    elif select_name == 'EVP':
        field_num = 2
    else:
        field_num = 3
    print ('{}类型的文件有{}个字段需要插值！'.format(select_name, field_num))
    out_Layer = name[1:4]+name[8:10]+name[11:13]  # 输出shp类型文件的文件名

    print (out_Layer)
    in_Table = name
    x_coords = "经度"
    y_coords = "维度"
    # z_coords = "平均气温"
    # out_Layer = "firestations_layer"
    spRef = r"Coordinate Systems\Geographic Coordinate Systems\World\WGS 1984.prj"     # 设定参考坐标为WGS 1984
    arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef)  # 创建事件图层
    out_feature_class = 'C:\\Users\\xianyu\\Desktop\\shp\\{}.shp'.format(out_Layer)    # shp文件存放处加文件名
    arcpy.Project_management(out_Layer, out_feature_class, out_coordinate_system)      # 投影
    print ('{} shp文件已经输出!'.format(name))
# 以上部分是实现气象csv文件生成shp文件
# ======================================================================================================================
# 插值
    fields = arcpy.ListFields(out_feature_class)   # 获取shp属性表里的字段
    print field_num
    for fields_order in range(10, 10+field_num):   # 依次对各个字段进行插值
        print fields_order
        print ('现在正在对字段{}进行插值！'.format(fields[fields_order].name.encode('utf-8')))
# ===============================================================================================
        # 解决PRE文件字段长度超出13的问题
        if select_name == 'PRE':
            fields_length = 5
        else:
            fields_length = len(fields[fields_order].name)
# ===============================================================================================
        # long_fields = len(fields)
        out_Kriging = arcpy.gp.Kriging_sa(out_feature_class, fields[fields_order].name, 'C:\\Users\\xianyu\\Desktop\\result\\{}{}'.format(out_Layer, fields[fields_order].name[:fields_length].encode('utf-8')), "Spherical", "1000", "VARIABLE 12", "C:\\Users\\xianyu\\Desktop\\variance\\{}{}".format(out_Layer, fields[fields_order].name[:fields_length].encode('utf-8')))
        out_kringing = Kriging(out_feature_class, fields[fields_order].name, "Spherical",  "1000", "VARIABLE 12")  # 输出tif文件
        out_kringing.save('C:\\Users\\xianyu\\Desktop\\tif\\{}{}.tif'.format(out_Layer, fields[fields_order].name[:fields_length].encode('utf-8')))  # 保存tif文件



# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "(EVP)-2001-2"
#arcpy.gp.Kriging_sa("(EVP)-2001-2", "小型蒸", "C:/Users/xianyu/Documents/ArcGIS/Default3.gdb/Kriging_shp3", "Exponential 16765.455726", "1000", "VARIABLE 12", "")



