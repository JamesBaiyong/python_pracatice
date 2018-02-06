# coding:utf-8
import requests
from lxml import html
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

start_time=time.time()
k=1
user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User_agent': user_agent}
site_url='https://movie.douban.com/top250?'

for i in range(10):

        page=i*25
        WEB=site_url+'start='+str(page)+'&filter='
        print u"正在抓取："+WEB
        html_source=requests.get(WEB).content
        S_URL=html.fromstring(html_source)


        for i in S_URL.xpath('//div[@class="info"]'):


                title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]

                move_info = i.xpath('div[@class="bd"]/p[1]/text()')
                # print move_info

                starts=move_info[0].replace(" ","").replace("\n","")
                date = move_info[1].replace(" ","").replace("\n","").split("/")[0]
                country=move_info[1].replace(" ","").replace("\n","").split("/")[1]
                geners = move_info[1].replace(" ", "").replace("\n", "").split("/")[2]
                rate = i.xpath('//span[@class="rating_num"]/text()')[0]
                comCount = i.xpath('//div[@class="star"]/span[4]/text()')[0]

                with open("DouBanMovie_Top250.txt",'a') as f:
                        f.write("TOP%s\n影片名：%s\n评分：%s\n评分人数：%s\n上映日期：%s\n上映国家:%s\n"%(k,title,rate,comCount,date,country))
                        f.write("======================================\n")
                        # print title,"\n",starts,"\n",date,"\n",country,"\n",geners,"\n",rate,"\n",comCount,"\n",move_info

                k+=1

        time.sleep(0.1)
print u"用时："
print int(time.time()-start_time)