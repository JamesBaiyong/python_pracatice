#coding=utf-8

from scrapy import Spider,Request
from ..items import HouspriceItem
from checkupdata import checkdata

class HouseSpider_HangZhou(Spider):

	name = 'HousePrice_HangZhou'
	headers = {
		'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
	}
	start_url = 'https://hz.fang.lianjia.com/loupan/'
	num = 1

	def start_requests(self):
		yield Request(self.start_url,headers=self.headers)

	def parse(self, response):
		items = HouspriceItem()
		house_list = response.xpath('//ul[@id="house-lst"]/li')
		for house_info in house_list:
			items['name'] = house_info.xpath('.//div[@class="info-panel"]/div[1]/h2/a/text()').extract()[0]
			items['type'] = house_info.xpath('.//div[@class="type"]/span[2]/text()').extract()[0]
			items['position'] = house_info.xpath('.//div[@class="where"]/span/text()').extract()[0]
			items['state'] = house_info.xpath('.//div[@class="type"]/span[1]/text()').extract()[0]

			logo = house_info.xpath('.//div[@class="sum-num"]/span/text()')
			if logo is not None:
				try:
					items['price'] = logo.extract()[0] + u'万/套'
				except IndexError:
					try:
						items['price'] = house_info.xpath(
							'.//div[@class="price"]/div/span/text()').extract()[0] + u'元/平'
					except IndexError:
						items['price'] = u'价格待定'
			else:
				items['price'] = 'shit'

			try:
				items['area'] = house_info.xpath('.//div[@class="area"]/span/text()').extract()[0]
			except IndexError:
				items['area'] = "--"
			items['table'] = "hangzhou"
			items['hash_data'] = checkdata(items['name'] + items['position'])

			yield items

		#翻页
		if self.num <= 42:
			self.num += 1
			next_page_url = self.start_url + 'pg' + str(self.num)
			print next_page_url
			yield Request(next_page_url, headers=self.headers)

