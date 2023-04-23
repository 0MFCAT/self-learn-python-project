# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MhgChapterItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    page_number = scrapy.Field()
    image_paths = scrapy.Field(serializer=list)
