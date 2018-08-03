import scrapy
from clwx.items import ClwxItem
from scrapy.http import Request

class ClwxSpider(scrapy.Spider):
    """
    爬虫
    """
    # 名字必须有
    name = 'clwx'
    # 初始urls
    start_urls = ['']

    def parse(self, response):
        """
        解析获得每一个的链接
        """
        urls = response.css('h3 a::attr(href)').extract()[6:]
        for url in urls:
            url = response.urljoin(url)
            yield Request(url, callback=self.parse_novel)

        next_page_url = response.css('.pages').css('a::attr(href)').extract()[-2]
        if 'java' not in next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield Request(next_page_url, callback=self.parse)

    def parse_novel(self, response):
        """
        解析单个获得item
        """
        title = response.css('h4::text').extract()[0]
        content = '\n'.join(response.css('.tpc_content::text').extract())

        item = ClwxItem()
        item['title'] = title
        item['url'] = response.url
        item['content'] = content
        yield item
