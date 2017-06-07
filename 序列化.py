#coding=utf-8
import cPickle as pickle

'''
序列化
'''
d = dict(name='Bob',age=20,score=88)
pickle.dumps(d)
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

'''
反序列化
'''
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print d