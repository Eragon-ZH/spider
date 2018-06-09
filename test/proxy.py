from urllib import request

url = "http://www.baidu.com"
# 设置代理
proxy = { "http:":"115.221.118.248:808" }
# 创建proxyHandler
proxy_handler = request.ProxyHandler(proxy)
# 创建Opener
opener = request.build_opener(proxy_handler)
# 安装Opener
request.install_opener(opener)

try:
	rsp = request.urlopen(url)
	html = rsp.read().decode()
	print(html)
except:
	print("aa")
