'''
1.使用compile函数将正则表达式字符串变成一个Pattern对象
2.通过Pattern对象的一些方法对文本进行匹配，得到一个Match对象
3.用Match对象的方法对结果进行操纵
'''

import re

s = r"\d+"
pattern = re.compile(s)
m = pattern.match("one123two245three345four456")
# 默认从头部开始，因而匹配不到任何东西
print(m)
# 制定查找范围
m = pattern.match("one123two245three345four456", 3, 10)
print(m)
print(m.group())
print(m.start(0))
print(m.end(0))
print(m.span(0))
