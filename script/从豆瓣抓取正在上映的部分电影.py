#coding:utf-8
from lxml import html
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def getHtml(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    headers = {'User_agent': user_agent}
    site_url=url
    html_S=requests.get(site_url,headers=headers).content
    html_R=html.fromstring(html_S)
    return html_R

def getInfo(url):
    html_R=getHtml(url)
    for i in html_R.xpath('//div[@id="nowplaying"]//ul[@class="lists"]/li'):
        title = i.xpath('@data-title')
        move_grade = i.xpath('@data-score')
        move_year = i.xpath('@data-release')
        move_time = i.xpath('@data-duration')
        move_contry = i.xpath('@data-region')
        move_director = i.xpath('@data-director')
        move_actors= i.xpath('@data-actors')
        move_votecount = i.xpath('@data-votecount')

        move_name = title[0]
        move_grade = move_grade[0]
        move_year = move_year[0]
        move_time = move_time[0]
        move_contry = move_contry[0]
        move_director = move_director[0]
        move_actors = move_actors[0]
        move_votecount = move_votecount[0]




        with open("NowPlaying_move01.txt",'a') as f:
            f.write("*-------------------*\n")
            f.write("片名：%s\n评分：%s\n导演：%s\n演员：%s\n地区：%s\n时间：%s\n时长：%s\n评价人数：%s人\n"%(move_name,move_grade,move_director,move_actors,move_contry,move_year,move_time,move_votecount))
            f.write("*-------------------*\n")


url = 'https://movie.douban.com/cinema/nowplaying/'
getInfo(url)




