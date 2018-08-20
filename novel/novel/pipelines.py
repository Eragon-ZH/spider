# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

from novel.items import NovelItem, ChapterItem

class NovelPipeline(object):
    def process_item(self, item, spider):
        """
        对item进行处理
        """
        # 当前目录
        current_path = os.getcwd()
        # 建立存放目录
        path = os.path.join(current_path, 'novels')
        if not os.path.exists(path):
            os.mkdir(path)
        novel_path = os.path.join(path, str(item['id']) + item['name'])
        # 建立该小说的目录
        if not os.path.exists(novel_path):
            os.mkdir(novel_path)
        # isinstance方法用来处理多个item
        if isinstance(item, ChapterItem):
            target_path = os.path.join(novel_path, str(item['title']) + '.txt')
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(item['content'])

        return item
