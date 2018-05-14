# -*- coding: utf-8 -*-
import scrapy
from .constant import stadium_id

class MatchesKoSpider(scrapy.Spider):
    name = 'matches_ko'
    allowed_domains = ['www.fifa.com']
    start_urls = ['http://www.fifa.com/worldcup/matches///']

    def parse(self, response):
        match_box = response.xpath('//*[@class="fi-mu fixture"]')
        for match in match_box:
            id_no = match.xpath('.//@data-id').extract_first()
            date_time = match.xpath('.//*[@class="fi-mu__info__datetime"]/text()').extract_first()
            stadium = match.xpath('.//*[@class="fi__info__stadium"]/text()').extract_first()
            city = match.xpath('.//*[@class="fi__info__venue"]/text()').extract_first()
            team1_name = match.xpath('.//*[@class="fi-t fi-i--4 home"]//*[@class="fi-t__nText "]/text()').extract_first()
            team2_name = match.xpath('.//*[@class="fi-t fi-i--4 away"]//*[@class="fi-t__nText "]/text()').extract_first()
            s_id = stadium_id[stadium.strip()]

            if team1_name is None:
                team1 = match.xpath('.//*[@class="fi-t home"]//*[@class="fi-t__nText "]/text()').extract_first()
                team2 = match.xpath('.//*[@class="fi-t away"]//*[@class="fi-t__nText "]/text()').extract_first()
                yield {'id': id_no,
                       'date_time': date_time.strip(),
                       'stadium': {'name':stadium.strip(),
                                'id': s_id},
                       'city': city.strip(),
                       'teams' : [team1,team2]
                   }
