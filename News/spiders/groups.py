# -*- coding: utf-8 -*-
import scrapy


class GroupsSpider(scrapy.Spider):
    name = 'groups'
    allowed_domains = ['www.fifa.com']
    start_urls = ['http://www.fifa.com/worldcup/groups/']

    def parse(self, response):
        groups = response.xpath('//*[@class="fi-table fi-standings"]')

        for group in groups:
            id_no = group.xpath('.//@id').extract_first()
            name = group.xpath('.//*[@class="fi-table__caption__title"]/text()').extract_first()
            teams_ids = group.xpath('.//tbody/tr/@data-team-id').extract()

            yield {
                'id': id_no,
                'name': name,
                'teams_ids': teams_ids,
            }
