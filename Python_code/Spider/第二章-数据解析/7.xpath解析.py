# xpath 是在XML文档中搜索内容的一门语言
# html是xml的一个子集
'''
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
    </author>
</book>
'''

# 安装 lxml模块
# xpath解析
from lxml import etree
xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
        <div>
            <nick>热热1</nick>
        </div>
        <span>
            <nick>热热2</nick>
        </span>
    </author>
</book>
"""
tree = etree.XML(xml)   # 将xml加载卫etree的对象
# result = tree.xpath("/book")  # /表示层级关系.第一个/是根节点
# result = tree.xpath("/book/name/text()")  # text() 拿name结点里面的文本
# result = tree.xpath("/book/author//nick/text()")   # // 后代里的文本全部拿出来
result = tree.xpath("/book/author/*/nick/text()")   #  * 表示任意的节点,通配符
result2 = tree.xpath("/book//nick/text()")
print(result)
print(result2)







