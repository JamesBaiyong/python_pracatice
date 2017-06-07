#coding=utf-8
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for data in ['Jake','James','Tom']:
	#向服务端发送data
	s.sendto(data,('127.0.0.1',8888))
	#接收服务端发来的数据
	print s.recv(1024)
s.close()