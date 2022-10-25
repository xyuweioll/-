# 注意，运行该程序时numpy包的版本不可过高，不然会报错，用命令 pip install numpy==1.15.0
# 对numpy进行降版本
import os
import netCDF4 as nc
from osgeo import gdal, osr, ogr
import numpy as np
import glob


def NC_to_tiffs(data, file_name, Output_folder):
    nc_data_obj = nc.Dataset(data)
    # print(nc_data_obj, type(nc_data_obj))  # 了解NC_DS的数据类型，<class 'netCDF4._netCDF4.Dataset'>
    # print(nc_data_obj.variables)  # 了解变量的基本信息
    # print(nc_data_obj)
    Lon = nc_data_obj.variables['lon'][:]
    Lat = nc_data_obj.variables['lat'][:]
    print(Lon)
    print(Lat)
    u_arr = np.asarray(nc_data_obj.variables['PM2.5'])  # 这里根据需求输入想要转换的波段名称
    print(u_arr)
    # # print('time_1=',time_1.min(),'time_max=',time_1.max())
    #
    # 影像的左上角和右下角坐标
    LonMin, LatMax, LonMax, LatMin = [Lon.min(), Lat.max(), Lon.max(), Lat.min()]

    # 分辨率计算
    N_Lat = len(Lat)
    N_Lon = len(Lon)
    Lon_Res = (LonMax - LonMin) / (float(N_Lon) - 1)
    Lat_Res = (LatMax - LatMin) / (float(N_Lat) - 1)

    # # 创建.tif文件
    driver = gdal.GetDriverByName('GTiff')
    out_tif_name = Output_folder + '\\'+file_name +'.tif'
    print(out_tif_name)
    out_tif = driver.Create(out_tif_name, N_Lon, N_Lat, 1, gdal.GDT_Float32)

    # 设置影像的显示范围
    # -Lat_Res一定要是-的
    geotransform = [LonMin, Lon_Res, 0, LatMax, 0, -Lat_Res]
    out_tif.SetGeoTransform(geotransform)

    # 获取地理坐标系统信息，用于选取需要的地理坐标系统
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)  # 定义输出的坐标系为"WGS 84"，AUTHORITY["EPSG","4326"]
    out_tif.SetProjection(srs.ExportToWkt())  # 给新建图层赋予投影信息

    # 去除异常值
    u_arr[u_arr[:, :] == -32768] = -99

    # 数据写出
    out_tif.GetRasterBand(1).WriteArray(u_arr)
    out_tif.GetRasterBand(1).SetNoDataValue(-99)
    out_tif.FlushCache()  # 将数据写入硬盘
    del out_tif  # 注意必须关闭tif文件
    nc_data_obj.close()
    # # return nc_data_obj.variables


def main():
    Input_folder = input('please input the file_path you store your .nc files\n===>>>')
    Output_folder = input('please input the file_path you store your tif files\n===>>>')
    Value_name = input('please input the name of the value you want to process, like "PM2.5" \n===>>>')

    # 读取所有nc数据
    data_list = glob.glob(Input_folder + '\*.nc')  # 获取指定目录下所以.nc文件，也可通过其他方法实现

    for i in range(len(data_list)):
        data = data_list[i]
        File_name = data.rsplit('\\', 1)[1][:-3]   # 从右边分割一次后取第二个,再去掉.nc后缀
        print(File_name)
        NC_to_tiffs(data, File_name, Output_folder)
        print(data + '转tif成功')


if __name__ == '__main__':
    main()

# G:\Overall datasets\Air_20220901\CHAP_PM2.5_M1K_2005_V4
# G:\Overall datasets\Air_test
