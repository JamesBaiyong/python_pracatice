import requests
from lxml import html

headers = {
		'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
	}

start_url = 'http://su.fang.lianjia.com/'

reqContent = requests.get(start_url,headers).content
reqXpath = html.fromstring(reqContent)
house_list = reqXpath.xpath('//div[@class="house-lst"]/ul/li')
for i in house_list:
	name = i.xpath('.//div[@class="title-box"]/h2/a/text()')
	print name
	raw_input()

# print house_list