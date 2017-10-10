#coding=utf-8
from scrapy.spider import Spider
from scrapy import Request
from ..items import  JdBookItem
import requests,re,json

class JDBook(Spider):

	name = 'jd_book'
	start_url = 'http://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10001-1#comfort'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
	}
	price_url = 'http://p.3.cn/prices/mgets?type=1&skuIds=J_'
	def start_requests(self):
		url = self.start_url
		yield Request(url,headers=self.headers)

	def parse(self, response):
		item = JdBookItem()
		book_info = response.xpath('//ul[@class="clearfix"]/li')
		for book in book_info:
			#获取在页面的书籍信息
			item['book_name'] = book.xpath('.//div[@class="p-img"]/a/@title').extract()[0]
			item['author'] = book.xpath('.//div[@class="p-detail"]/dl[1]/dd/a[1]/text()').extract()[0]
			item['press'] = book.xpath('.//div[@class="p-detail"]/dl[2]/dd/a/text()').extract()[0]
			item['number'] = book.xpath('.//div[@class="p-num"]/text()').extract()[0]
			item['book_id'] = book.xpath('.//div[@class="p-detail"]/dl[3]/dd/del/@data-price-id').extract()[0]

			#获取ajax接口地址，将返回的JSON处理为字典
			json_url = self.price_url+item['book_id']
			json_price = requests.get(json_url).text
			data = json.loads(json_price)[0]
			#分析字典数据，获取价格
			
			item['price'] = data['m'] + '￥'.decode('utf-8')
			item['preferential_price'] = data['op'] + '￥'.decode('utf-8')
			yield item
			
                        #获取下一页
			nextLink = response.xpath('//div[@class="m m-page"]/div/div/span/a[@class="pn-next"]/@href').extract()[0]
			if nextLink:
				nextLink = 'http:' + nextLink
				yield Request(nextLink, headers=self.headers)



