# -*- coding: utf-8 -*-
import scrapy


class TeamsSpider(scrapy.Spider):
    name = 'teams'
    allowed_domains = ['www.fifa.com']
    start_urls = ['http://www.fifa.com/worldcup/teams//']

    def parse(self, response):
        teams = response.xpath('//*[@class="team"]')
        for team in teams:
            id_no = team.xpath('.//@href').extract_first()[21:26]
            name = team.xpath('.//*[@class="team-name"]/text()').extract_first()
            flag_img = team.xpath('.//img/@src').extract_first()
            url = response.urljoin(team.xpath('.//@href').extract_first())
            yield scrapy.Request(url,
                                 callback=self.parse_team,
                                 meta={'main': {
                                     'id': id_no,
                                     'team_name': name,
                                     'flag_img': flag_img,
                                     'team_info': {}
                                 }})

    def parse_team(self, response):
        appearances = response.xpath('//*[@class="table"]//*[@class="num"]/text()')[0].extract()
        titles = response.xpath('//*[@class="table"]//*[@class="num"]/text()')[1].extract()
        fifa_rank = response.xpath('//*[@class="table"]//*[@class="num"]/text()')[2].extract()
        final_dict = response.meta.get('main')
        final_dict['team_info'] = {
            'appearances': appearances,
            'titles': titles,
            'fifa_rank': fifa_rank}
        return final_dict
