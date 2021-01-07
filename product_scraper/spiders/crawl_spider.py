# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from product_scraper.items import Film


class MySpider(CrawlSpider):
    name = 'crawl_spider'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?title_type=feature']

    rules = (
        # follow=True,
        Rule(LinkExtractor(allow=('https://www.imdb.com/title/',)), callback='parse_product'),
    )

    def parse_product(self, response):
        item = Film()
        item['film_url'] = response.url
        item['title'] = response.xpath("//div[@class='title_wrapper']/h1/text()").get()
        # item['genre'] доделать до корректного получения значений
        item['genre'] = response.xpath("//div[@class='subtext']/a/text()").get()
        item['rating'] = response.xpath("//div[@class='ratingValue']/strong/text()").get()
        item['stars'] = response.xpath("//div[@class='credit_summary_item']/a/text()").get()
        # item['type'] = response.xpath("//div[@class='credit_summary_item']/a/text()").get()
        item['blocks'] = response.xpath("//div[@id='titleDetails']/div[@class='txt-block']/*/text()").get()
        return item
