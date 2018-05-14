# -*- coding: utf-8 -*-
import scrapy


class TeamStatsSpider(scrapy.Spider):
    name = 'team_stats'
    allowed_domains = ['www.fifa.com']
    start_urls = ['http://www.fifa.com/worldcup/groups//']

    def parse(self, response):
        # teams = response.xpath('//*[@data-team-id]')
        # for team in teams:
        #     team_name = team.xpath('.//*[@class="fi-table__teamname teamname-nolink"]//*[@class="fi-t__nText "]/text()').extract_first()
        #
        # tables = response.xpath('//tbody')
        #
        # for table in tables:
        #     rows = table.xpath('//tr')
        #
        #     for row in rows:
        #         columns = row.xpath('//td')
        #
        #         for column in columns:
        #             yield {'data' : column.xpath('//text()').extract_first()}


        teams = response.xpath('//table/tbody/tr')
        for team in teams:
            team_stats = team.xpath('//td')

            for team_stat in team_stats:

                yield{'stats': team_stat.xpath('//text()')}
