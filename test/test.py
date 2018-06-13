from urllib import request, parse
from bs4 import BeautifulSoup

url =
    with open('cookie_file') as f:
        cookie = f.read()
    cookie = cookie.replace('\n', '')

    return cookie

cookie = get_cookie()

headers = {'host': 'h5.qzone.qq.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh,zh-CN;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': cookie,
            'connection': 'keep-alive'}

req = request.Request(url=url, headers=headers)
# 利用urlopen打开request，得到response
rsp = request.urlopen(req)

print(rsp.read().decode())

# soup = BeautifulSoup(html.text,"lxml")
# contents = soup.select(".f_toggle")
# # print(contents)
#
# with open( "test.html", "w" ) as f:
#     f.write(html.text)
