from urllib import request
import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"

'''
分析网址
“id=100%3A90”   90%~100%
start=40&limit=20  从第40个开始请求20个
因而每次仅start+=20即可
'''


rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)

print(data[1])
