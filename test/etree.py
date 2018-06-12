'''
用lxml解析HTML代码
'''

from lxml import etree

text = '''
<div>
    <ul>
        <li class="item0"><a href="0.html">item1</0><li>
        <li class="item1"><a href="1.html">item2</0><li>
        <li class="item2"><a href="2.html">item3</0><li>
        <li class="item3"><a href="3.html">item4</0><li>
        <li class="item4"><a href="4.html">item5</0><li>
    </ul>
</div>
'''
# 将文本补全成html
html = etree.HTML(text)
s = etree.tostring(html)
print(s)

# 只能读取xml格式，不能读取html内容
html = etree.parse("./test.xml")
s = etree.tostring(html,pretty_print=True)
