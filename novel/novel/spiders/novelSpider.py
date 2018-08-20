# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup

from novel.items import NovelItem, ChapterItem

class NovelSpider(scrapy.Spider):
    name = 'novelSpider'
    # 爬取限制，非必须
    allowed_domains = ['https://www.x23us.com']
    base_url = 'https://www.x23us.com/quanben/'

    def start_requests(self):
        """
        全本小说url规则为'https://www.x23us.com/quanben/1'，最后的数字即为页数。
        """
        # 暂时只爬取前3页，可以更改爬取更多
        for i in range(1, 4):
            url = self.base_url + str(i)
            yield Request(url, self.parse)

    def parse(self, response):
        """
        获取每一个novel的地址
        """
        soup = BeautifulSoup(response.text, 'lxml')
        tds = soup.find_all('tr')
        for td in tds[1:]:
            novel_name = td.find_all('a')[1].get_text()
            novel_url = td.find_all('a')[1]['href']
            yield Request(novel_url, callback=self.parse_novel,
                          meta={'novel_name':novel_name})

    def parse_novel(self, response):
        """
        对每一个novel进行解析，获取章节地址
        """
        item = NovelItem()
        item['url'] = response.url
        item['id'] = int(response.url.split('/')[-2])
        item['name'] = response.meta['novel_name']
        yield item

        soup = BeautifulSoup(response.text, 'lxml')
        chapter_list = soup.find('table').find_all('a')
        for chapter in chapter_list:
            chapter_url = item['url'] + chapter['href']
            yield Request(chapter_url, callback=self.parse_chapter,
                          meta={'novel_id':item['id'],
                                'novel_name':item['name']})

    def parse_chapter(self, response):
        """
        解析章节，获取章节内容
        """
        item = ChapterItem()
        item['id'] = response.meta['novel_id']
        item['name'] = response.meta['novel_name']
        soup = BeautifulSoup(response.text, 'lxml')
        item['title'] = soup.find('h1').get_text()
        # 用'\n'取代html的'<br/>'的换行标签
        item['content'] = soup.find(id='contents').get_text('\n', '<br/>')
        yield item
