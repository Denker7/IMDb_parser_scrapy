# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Film(scrapy.Item):
    film_url = scrapy.Field()
    title = scrapy.Field()
    genre = scrapy.Field()
    rating = scrapy.Field()
    stars = scrapy.Field()
    type = scrapy.Field()
    blocksDetailsSites = scrapy.Field()
    blocksDetailsCountry = scrapy.Field()
    blocksDetailsLanguage = scrapy.Field()
    blocksOfficeBudget = scrapy.Field()
    blocksOfficeWeekendUSA = scrapy.Field()
    blocksOfficeWorldwide = scrapy.Field()
    blocksTechnicalRuntime = scrapy.Field()
    blocksTechnicalSound = scrapy.Field()
    blocksTechnicalColor = scrapy.Field()
    blocksTechnicalRatio = scrapy.Field()