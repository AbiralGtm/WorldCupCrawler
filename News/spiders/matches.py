# -*- coding: utf-8 -*-
import scrapy


class MatchesSpider(scrapy.Spider):
    name = 'matches'
    allowed_domains = ['www.fifa.com/worldcup/matches/']
    start_urls = ['http://www.fifa.com/worldcup/matches//']

    def parse(self, response):
        match_box = response.xpath('//*[@class="fi-mu fixture"]')
        for match in match_box:
            id_no = match.xpath('.//@data-id').extract_first()
            date_time = match.xpath('.//*[@class="fi-mu__info__datetime"]/text()').extract_first()
            stadium = match.xpath('.//*[@class="fi__info__stadium"]/text()').extract_first()
            city = match.xpath('.//*[@class="fi__info__venue"]/text()').extract_first()
            yield {'id': id_no,
                   'date_time': date_time,
                   'stadium': stadium,
                   'city': city,
                   # 'teams' : [,]
                   }
        # team1_name = match.xpath('.//*[@class="fi-t fi-i--4 home"]//*[@class="fi-t__nText "]/text()').extract_first()
        # team1_img = match.xpath('.//*[@class="fi-t fi-i--4 home"]//*[@class="fi-t__i "]/img/@src').extract_first()
        # team2_img = match.xpath('.//*[@class="fi-t fi-i--4 away"]//*[@class="fi-t__i "]/img/@src').extract_first()
        # team2_name = match.xpath('.//*[@class="fi-t fi-i--4 away"]//*[@class="fi-t__nText "]/text()').extract_first()
