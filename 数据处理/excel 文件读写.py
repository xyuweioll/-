#按行写入数据代码：
# -*- coding: utf-8 -*-
import xlwt

# 创建工作簿
f = xlwt.Workbook()
# 创建一个sheet
sheet1 = f.add_sheet('test', cell_overwrite_ok=True)

test_data = [['姓名','性别', '电话'],['张三','女','13800138000'],['李四','男','13800138001'],['王五','男','13800138002']]
for i in range(len(test_data)):
    t = test_data[i]
    for j in range(len(t)):
        sheet1.write(i, j, t[j])
# 保存文件
#f.save("d:\\test.xls")
f.save("C:\\Users\\xianyu\\Desktop\\test.xlsx")
