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
        	# fifa_rank = 
        	# appearances = 
        	# titles =  

        	yield {
        		'id': id_no,
        		'team_name': name,
        		'flag_img': flag_img,
        	}


	# def parse(self, response):




