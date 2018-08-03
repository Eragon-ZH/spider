# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
# import logging

# logger = logging.getLogger(__name__)

class ClwxPipeline(object):
    def process_item(self, item, spider):
        """
        对item进行处理
        """
        # logger.warning(item)
        # 当前目录
        current_path = os.getcwd()
        # 建立存放目录
        path = os.path.join(current_path, 'novel')
        if not os.path.exists(path):
            os.mkdir(path)
        # 保存文件
        target_path = os.path.join(path, str(item['title']) + '.txt')
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(item['url'] + '\n')
            f.write(item['content'])

        return item
