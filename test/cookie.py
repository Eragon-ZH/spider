from urllib import request, parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar();
# 创建cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建cookie请求管理器
http_handler = request.HTTPHandler()
# 创建https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

# 初次登录输入用户名密码获取登录cookie
def login():
    # 登录form提交的网址
    url = ""
    # 表单提交input的name
    data = {
        "email":"test"
        "password":"123456"
    }
    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建请求对象
    req = request.Request(url,data=data.encode())
    # 使用opener发送请求
    rsp = opener.open(req)
# 利用cookie登录网页
def getHomePage():
    # 登录网址
    url = ""
    # 若已经执行了login函数，则opener已自动包含相对应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("filename","w") as f:
        f.write(html)

if __name__ == '__main__':
    login()
    # print(cookie)
    # for item in cookie:
    #     print(item)
    getHomePage()
