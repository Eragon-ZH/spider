import requests
import re

def chuangguan():
    base_url = "http://www.heibanke.com/lesson/crawler_ex00/"
    r = requests.get(base_url)
    while True:
        number = parse_url(r.text)
        url = base_url + number
        print(url)
        r = requests.get(url)

def parse_url(html):
    start = html.find('<h3>')
    end = html.find('</h3>')
    try:
        h3 = html[start+4:end]
        number = re.findall(r'\d{5,5}', h3)[0]
        print(h3)
        print(number)
    except:
        print(html)
        print(start, end)
    return number

if __name__ == '__main__':
    chuangguan()
