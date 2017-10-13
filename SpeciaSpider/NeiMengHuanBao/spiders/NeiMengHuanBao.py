#coding=utf-8
from scrapy import Spider
from scrapy import Request
from ..items import NeimenghuanbaoItem

class NeiMengHuanBaoSpider(Spider):
   '''**爬虫'''

   # 设置爬虫相关信息
   name = 'NeiMengHuanBao'
   start_url = '***********'
   list = [start_url+'.html',start_url+'_1.html',
           start_url+'_2.html',start_url+'_3.html',
           start_url+'_4.html',start_url+'_5.html']
   headers = {
      'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
   }

   def start_requests(self):
      #爬取网页链接
      for url in self.list:
         yield Request(url,headers=self.headers)

   def parse(self, response):
      #爬取子页
      all_url = response.xpath('//div[3]//div//div[3]//div[2]//ul//li')
      for url in all_url:
         sub_url =  url.xpath('.//a/@href').extract()[0]
         complete_sub_url = 'http://www.nmgepb.gov.cn/ywgl/hjpj/xmslqk' \
                        + sub_url[1:]
         yield Request(complete_sub_url,headers=self.headers,
                       callback=self.get_page_info,meta={'url':complete_sub_url})


   def get_page_info(self,response):
      #获取子页信息
      item = NeimenghuanbaoItem()

      #设置子页结构差异变量，按照变量不同获取不同子页信息
      info = response.xpath('//div[@class="TRS_Editor"]/p') 
      table = response.xpath('//div[@class="TRS_PreExcel TRS_PreAppend"]') 
      table_plus = response.xpath('//div[@class="TRS_PreAppend"]/span')
      fxd_table = response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[2]/p/span') 
      fxd_table_plus = response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[2]/p/span/a') 
      fxd_table_plus1 = response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[2]/p/a')
      fxd_table_plus2 = response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[2]/p/a')



      if len(info) == 0 and table == [] and fxd_table == [] \
            and table_plus == [] and fxd_table_plus == [] \
            and fxd_table_plus1 == [] and fxd_table_plus2 == []:
         #页面中有多个P标签且无表格的子页信息
         item['project_name'] = response.xpath('//div[@class="xl_nr_16"]//p/text()').extract()[4]
         item['location'] = response.xpath('//div[@class="xl_nr_16"]//p/text()').extract()[5]
         item['company'] = response.xpath('//div[@class="xl_nr_16"]//p/text()').extract()[6]
         item['institution'] = response.xpath('//div[@class="xl_nr_16"]//p/text()').extract()[7]
         item['accept_date'] = response.xpath('//div[@class="xl_nr_16"]//p/text()').extract()[8]
         item['url'] = response.meta['url']
         yield item

      if len(info) == 0 and table != [] and fxd_table == [] \
            and table_plus == [] and fxd_table_plus == [] \
            and fxd_table_plus1 == [] and fxd_table_plus2 == []:
         #页面中是完整表格的子页信息提取
         item['project_name'] = response.xpath('//div[@class="TRS_PreExcel TRS_PreAppend"]/table/tbody/tr[3]/td[2]/text()').extract()[0]
         item['location'] = response.xpath('//div[@class="TRS_PreExcel TRS_PreAppend"]/table/tbody/tr[3]/td[3]/text()').extract()[0]
         item['company'] = response.xpath('//div[@class="TRS_PreExcel TRS_PreAppend"]/table/tbody/tr[3]/td[4]/text()').extract()[0]
         item['institution'] = response.xpath('//div[@class="TRS_PreExcel TRS_PreAppend"]/table/tbody/tr[3]/td[5]/text()').extract()[0]
         item['accept_date'] = response.xpath('//div[@class="TRS_PreExcel TRS_PreAppend"]/table/tbody/tr[3]/td[6]/text()').extract()[0]
         item['url'] = response.meta['url']
         yield item

      if len(info) == 0 and table == [] and fxd_table != [] \
            and table_plus == [] and fxd_table_plus == [] \
            and fxd_table_plus1 == [] and  fxd_table_plus2 == []:
         #页面中是混乱表格的子页信息提取
         item['project_name'] = response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[2]/p//span/text()').extract()[0]
         item['location'] = response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[3]/p//span/text()').extract()[0]
         item['company'] = response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[4]/p//span/text()').extract()[0]
         item['institution'] = response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[5]/p//span/text()').extract()[0]
         item['accept_date'] =  ''.join(response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[6]/p//span/text()').extract()[0:5])
         item['url'] = response.meta['url']
         yield item

      if len(info) == 0 and table == [] and fxd_table == [] \
            and table_plus == [] and fxd_table_plus != [] \
            and fxd_table_plus1 == [] and fxd_table_plus2 == []:
         #页面中是混乱表格的子页特殊页1
         item['project_name'] = \
         response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[2]/p/span/a/text()').extract()[0]
         item['location'] = \
         response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[3]/p//span/text()').extract()[0]
         item['company'] = \
         response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[4]/p//span/text()').extract()[0]
         item['institution'] = \
         response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[5]/p//text()').extract()[0]
         item['accept_date'] = \
         ''.join(response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[6]/p//span/text()').extract()[0:5])
         item['url'] = response.meta['url']
         yield item

      if len(info) == 0 and table == [] and fxd_table == [] \
            and table_plus == [] and fxd_table_plus == [] \
            and fxd_table_plus1 != [] and fxd_table_plus2 == []:
         ##页面中是混乱表格的子页特殊页2
         item['project_name'] = \
         response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[2]/p/a/text()').extract()[0]
         item['location'] = \
         response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[3]/p//span/text()').extract()[0]
         item['company'] = \
         response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[4]/p//span/text()').extract()[0]
         item['institution'] = \
         response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[5]/p//span/text()').extract()[0]
         item['accept_date'] = \
         ''.join(response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[6]/p//span/text()').extract()[0:5])
         item['url'] = response.meta['url']
         yield item

      if len(info) == 0 and table == [] and fxd_table == [] \
               and table_plus == [] and fxd_table_plus == [] \
               and fxd_table_plus1 == [] and fxd_table_plus2 !=[]:
         # 页面中是混乱表格的子页特殊页3
            item['project_name'] = \
               response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[2]/p/a/text()').extract()[0]
            item['location'] = \
               response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[3]/p//span/text()').extract()[0]
            item['company'] = \
               response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[4]/p//span/text()').extract()[0]
            item['institution'] = \
               response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[5]/p//span/text()').extract()[0]
            item['accept_date'] = \
               ''.join(response.xpath('//*[@id="zoomfont"]/div/span/table/tbody/tr[2]/td[6]/p//span/text()').extract()[0:5])
            item['url'] = response.meta['url']
            yield item

      if table_plus != [] and fxd_table_plus != []:
         # 页面中是混乱表格的子页特殊页4
         item['project_name'] = response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[2]/p/span/a/text()').extract()[0]
         item['location'] = response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[3]/p/span/text()').extract()[0]
         item['company'] = response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[4]/p/span/text()').extract()[0]
         item['institution'] = response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[5]/p/span/text()').extract()[0]
         item['accept_date'] = ''.join(response.xpath('//*[@id="zoomfont"]/div/div/span/table/tbody/tr[2]/td[6]/p/span/text()').extract()[0:5])
         item['url'] = response.meta['url']
         yield item


      if len(info) == 11:
         #页面中是有严格的P标签包围的子页的信息提取
         item['project_name'] = response.xpath('//div[@class="TRS_Editor"]/p/text()').extract()[5]
         item['location'] = response.xpath('//div[@class="TRS_Editor"]/p/text()').extract()[6]
         item['company'] = response.xpath('//div[@class="TRS_Editor"]/p/text()').extract()[7]
         item['institution'] = response.xpath('//div[@class="TRS_Editor"]/p/text()').extract()[8]
         item['accept_date'] = response.xpath('//div[@class="TRS_Editor"]/p/text()').extract()[9]
         item['url'] = response.meta['url']
         yield item

      if len(info) == 1:
         #页面中的信息在一个P标签中的子页的信息提取
         item['project_name'] = response.xpath('//div[@class="xl_nr_16"]//p/text()').extract()[4]
         item['location'] = response.xpath('//div[@class="xl_nr_16"]//p/text()').extract()[5]
         item['company'] = response.xpath('//div[@class="xl_nr_16"]//p/text()').extract()[6]
         item['institution'] = response.xpath('//div[@class="xl_nr_16"]//p/text()').extract()[7]
         item['accept_date'] = response.xpath('//div[@class="xl_nr_16"]//p/text()').extract()[8]
         item['url'] = response.meta['url']
         yield item

      if len(info) == 5:
         # 页面中是混乱表格的子页特殊页5
         point = response.xpath('//*[@id="zoomfont"]/div/table/tbody/tr[2]/td[2]/p/a')
         if point == []:
            item['project_name'] = response.xpath('//*[@id="zoomfont"]/div/table/tbody/tr[2]/td[2]/text()').extract()[0]
         else:
            item['project_name'] = response.xpath('//*[@id="zoomfont"]/div/table/tbody/tr[2]/td[2]/p/a/text()').extract()[0]
         item['location'] = response.xpath('//*[@id="zoomfont"]/div/table/tbody/tr[2]/td[3]/p//span/text()').extract()[0]
         item['company'] = response.xpath('//*[@id="zoomfont"]/div/table/tbody/tr[2]/td[4]/p//span/text()').extract()[0]
         item['institution'] = response.xpath('//*[@id="zoomfont"]/div/table/tbody/tr[2]/td[5]/p//span/text()').extract()[0]
         item['accept_date'] = ''.join(response.xpath('//*[@id="zoomfont"]/div/table/tbody/tr[2]/td[6]/p//span/text()').extract()[0:5])
         item['url'] = response.meta['url']
         yield item
