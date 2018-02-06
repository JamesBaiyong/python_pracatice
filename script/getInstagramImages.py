#coding=utf-8
from selenium import webdriver
from lxml import html
import requests,time

def getImgUrl(starturl):
	'''
	获取图片连接
	'''
	browser = webdriver.Chrome()
	browser.get(starturl)
	htmlSoure=browser.page_source
	htmlXml=html.fromstring(htmlSoure)
	imgurl = htmlXml.xpath('//div[@class="_jjzlb"]/img/@src')
	global imgname
	imgname= time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
	return imgurl

def getImg(starturl):
	'''
	保存图片
	'''
	url=getImgUrl(starturl)
	ins_pic=requests.get(url[0],headers=headers).content
	dirname="insimg"

	filename = '%s/%s.jpg' % (dirname, imgname) 
	with open(filename,'wb') as f:
		f.write(ins_pic)

user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User_agent': user_agent}
startUrl=['https://www.instagram.com/p/BUtO81EAn3M/','https://www.instagram.com/p/BUrDPgVAYQl/','https://www.instagram.com/p/BUYyt9ggqvz/','https://www.instagram.com/p/BUMnT1fAwhJ/','https://www.instagram.com/p/BT3wfDTgRrV/','https://www.instagram.com/p/BT0spKHAppC/','https://www.instagram.com/p/BQH6_TZBvdr/','https://www.instagram.com/p/BQCthiohpB-/','https://www.instagram.com/p/BPp7w9gBzNF/','https://www.instagram.com/p/BU9_bOKA2GM/','https://www.instagram.com/p/BUP6cCQDfrs/']
# startUrl=raw_input("Enter instagram url:")
n=0
for i in range(len(startUrl)):
	n=n+1
	starturl = startUrl[i]
	getImg(starturl)
	print u'下载了第%s张图!'%n
print u'图片下载完毕！'


