# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawldataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    link = scrapy.Field()
    image_urls = scrapy.Field()  # Đổi tên trường từ img_url thành image_urls để tương thích với ImagesPipeline
    images = scrapy.Field()
    summary = scrapy.Field()
    content = scrapy.Field()
