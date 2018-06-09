from urllib import request, parse
import json

# 地址和数据
baseUrl = "http://fanyi.baidu.com/sug"
data = {
	"kw": "girl"
}
# 数据需要转码
data = parse.urlencode(data).encode()
# post需要更改头部，至少包括长度
headers = {
	"Content-Length":len(data)
}
# 利用Request对象构造请求
req = request.Request(url=baseUrl, data=data, headers=headers)
# 利用urlopen打开request，得到response
rsp = request.urlopen(req)
# 解码response
json_data = rsp.read().decode()
# 获取的json利用json包解析
json_data = json.loads(json_data)
# 打印结果
for item in json_data["data"]:
	print(item["k"],item["v"])
