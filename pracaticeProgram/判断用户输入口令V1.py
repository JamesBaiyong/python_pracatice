#coding=utf-8
import hashlib,json

def Psss_w_md5(pass_word):
	'''
	计算用户输入密码的MD5值
	'''
	md5=hashlib.md5()
	md5.update(pass_word)
	md5_value=md5.hexdigest()
	return md5_value

def login(user_name,pass_word):
	'''
	判断用户输入的用户名和密码是否正确
	:param user_name: 
	:param pass_word: 
	:return: 
	'''
	db=Db_value()
	try:
		if md5_value == db[user_name]:
			print u'用户密码正确！^_^'
		else:
			print u'用户密码错误！0.0'
	except KeyError:
		print u'还没有此用户0.0！'

def Db_value():
	'''
	读取本地文件，反序列化为dict
	:return: 
	'''
	with open('pass.json','rb') as f:
		db = json.load(f)
	return db

User_n=raw_input("请输入用户名：")
Pass_w=raw_input("请输入用户密码：")
md5_value=Psss_w_md5(Pass_w)
login(User_n,md5_value)
