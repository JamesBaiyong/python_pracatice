#coding=utf-8
import json
'''
把python对象变成JSON
'''
d = dict(name='Bob',age=20,socre=88)
print json.dumps(d)

'''
JSON反序列化为python对象
'''
json_str = '{"age": 20, "socre": 88, "name": "Bob"}'
print json.loads(json_str)

'''
类序列化为JSON
'''
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
s = Student('Bob',20,88)

'''
转换student类的函数
'''
def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
print (json.dumps(s,default=student2dict))

'''
转换为student类的函数s
'''
def dict2student(d):
	return Student(d['name'],d['age'],['score'])

json_str = '{"age": 20, "socre": 88, "name": "Bob"}'
print (json.loads(json_str,object_hook=dict2student))