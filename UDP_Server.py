#coding=utf-8
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8888))

print 'Welcome UDP connect..'
while True:
	#接收客户端传来的数据
	data,addr=s.recvfrom(1024)
	print 'Received from %s:%s.',addr
	s.sendto('Hello,%s!'%data,addr)
