# -*- coding: utf-8 -*-
import scrapy


class WcNewsSpider(scrapy.Spider):
    name = 'wc_news'
    allowed_domains = ['www.skysports.com']
    start_urls = ['http://www.skysports.com/world-cup-news']

    def parse(self, response):
        news_box = response.xpath('//*[@class="news-list__item news-list__item--show-thumb-bp30"]')
        for news in news_box:
            headline = news.xpath('.//*[@class="news-list__headline"]/a/text()').extract_first()
            thumb_img = response.urljoin(news.xpath('.//img/@src').extract_first())
            description = news.xpath('.//*[@class="news-list__snippet"]/text()').extract_first()
            url = news.xpath('.//*[@class="news-list__headline"]/a/@href').extract_first()
            data_id = news.xpath('.//@data-id').extract_first()
            yield {
                'Headline': headline.strip(),
                'Thumb_img': thumb_img,
                'Description': description.strip(),
                'Url': url,
                'Data_id': data_id
            }

        more_news_url = response.urljoin(
            response.xpath('//*[@class="loadmore1 button button--light button--fluid"]/@href').extract_first())
        yield scrapy.Request(more_news_url)
