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
        item['genre'] = response.xpath("//div[@class='subtext']/a[position()<last()]/text()").extract()
        item['rating'] = response.xpath("//span[@itemprop='ratingValue']/text()").get()
        item['stars'] = response.xpath("//div[@class='plot_summary ']/div[@class='credit_summary_item'][3]/"
                                       "a[position()<last()]/text()").extract()
        # item['type'] = response.xpath("//div[@class='credit_summary_item']/a/text()").get()

        item['blocksDetailsSites'] = response.xpath(
            "//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Official Sites:']/a/text()").get()
        item['blocksDetailsCountry'] = response.xpath(
            "//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Country:']/a/text()").extract()
        item['blocksDetailsLanguage'] = response.xpath(
            "//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Language:']/a/text()").extract()
        item['blocksOfficeBudget'] = response.xpath(
            "//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Budget:']/text()").extract()
        item['blocksOfficeWeekendUSA'] = response.xpath(
            "//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Opening Weekend USA:']/text()").extract()
        item['blocksOfficeWorldwide'] = response.xpath(
            "//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Cumulative Worldwide Gross:']/text()").extract()
        item['blocksTechnicalRuntime'] = response.xpath(
            "//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Runtime:']/time/text()").extract()
        item['blocksTechnicalSound'] = response.xpath(
            "//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Sound Mix:']/a/text()").extract()
        item['blocksTechnicalColor'] = response.xpath(
            "//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Color:']/a/text()").extract()
        item['blocksTechnicalRatio'] = response.xpath(
            "//div[@id='titleDetails']/div[@class='txt-block'][./h4/text()='Aspect Ratio:']/text()").extract()
        return item
