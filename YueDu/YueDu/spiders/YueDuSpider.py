#coding=utf-8

from scrapy import Spider
from scrapy import Request
from ..items import YueduItem

class YueDuSpider(Spider):

	name = 'YueDuSpider'
	start_url = 'https://yuedu.baidu.com/book/list/3?show=1'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
	}
	domain_name = 'https://yuedu.baidu.com'

	#开始请求
	def start_requests(self):
		url = self.start_url
		yield Request(url,headers=self.headers)

	#网页解析
	def parse(self, response):
		num = 0
		item = YueduItem()
		book_list = response.xpath('//div[@class="booklist-inner clearfix"]/div')
		for info in book_list:
			item['name'] = info.xpath('.//a[2]/span/text()').extract()[0]
			try:
				item['author'] = info.xpath('.//p/span[1]/text()').extract()[0]
			except IndexError:
				item['author'] = u'暂无'
			try:
				item['price'] = info.xpath('.//p/span[2]/text()').extract()[1]
			except IndexError:
				item['price'] = u'免费'
			item['url'] = self.domain_name+info.xpath('.//a[2]/@href').extract()[0]
			yield item

		#翻页
		while num < 2920:
			next_link = self.start_url + '&pn=%s' % (num)
			num += 20
			print num
			yield Request(next_link,headers=self.headers)
