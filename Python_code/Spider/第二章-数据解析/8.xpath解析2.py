from lxml import etree
tree = etree.parse("b.html")  # 直接加载html文件
# result = tree.xpath('/ html/body/ul/li/a/text()')  # 返回值为一列表
# result = tree.xpath('/ html/body/ul/li[1]/a/text()')  # 返回第一个li里面的值，xpath的顺序是从1开始数的
# result = tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')  # 找出herf属性值为dapao的标签内容
ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    result = li.xpath("./a/text()")  # 在li中继续寻找，./表示下一层目录
    print(result)
    result2 = li.xpath("./a/@href")  # 获取到标签a里面属性href的值
    print(result2)
print(tree.xpath('/html/body/ul/li/a/@href'))  # 获取多个href的属性值
