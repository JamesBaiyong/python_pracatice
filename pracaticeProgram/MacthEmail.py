#coding=utf-8
import re

def Re_Email(text):
	'''
	按照匹配规则匹配字符
	:param text: 
	:return: 
	'''
	if re_Email.match(text):
		m=re_Email.match(text)
		print 'OK,this is a Email address'
		print u'邮箱用户名为:%s'% m.group(1)
	else:
		print 'Oh,place enter a Email address'


re_Email = re.compile(r'^(\w.+)@(\w+).(\w+)$')
text=raw_input("请输入一个邮箱地址：")
Re_Email(text)
