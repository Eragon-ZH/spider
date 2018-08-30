import json
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://www.vgtime.com/topic/index/load.jhtml?page=1&pageSize=222222"
    vg_url = "https://www.vgtime.com"
    news_list = []

    r = requests.get(url)
    soup = BeautifulSoup(r.json()['data'], 'lxml')
    lis = soup.find_all("li")
    for li in lis:
        news = {}
        news['title'] = li.find('h2').text
        news['link'] = vg_url+ li.find('a')['href']
        news['time'] = li.find(class_='time_box').text
        news['comment_num'] = int(li.find(class_='comm_num').text)
        news_list.append(news)
        print(news)

    with open('vgnews.json', 'w', encoding='utf-8') as f:
        print(len(news_list))
        f.write(json.dumps(news_list, ensure_ascii=False))
