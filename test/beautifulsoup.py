from urllib import request
from bs4 import BeautifulSoup
import re

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content,"lxml")
# bs自动转码
content = soup.prettify()
print(content)
print("="*100)
print(soup.meta) # 只能获取到第一个
print("="*100)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)  # 字典形式获取属性及值
print("="*100)
print(soup.title)
print(soup.title.string) # 获取标签内容
print("="*100)
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
print("="*100)
tags = soup.find_all(name="meta")  # 可以用name attrs等找
print(tags)
print("="*100)
tags = soup.find_all(name=re.compile("^me"))  # 可以用正则
print(tags)
print("="*100)
tags = soup.select("#lg")  # 可以用css选择器
print(tags[0])
print("="*100)
tags = soup.select(".fm")  # 可以用css选择器
print(tags[0])
