#coding=utf-8
import socket
#创建一个基于TCP连接的套接字，AF_INFT代表IPv4，SOCK_STRAM代表使用面向流的TCP协议
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('music.163.com',80))

#发送数据
s.send('GET / HTTP/1.1\r\nHost: music.163.com\r\nConnection: close\r\n\r\n')
#接收数据
buffer=[]
while True:
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
print buffer
data=''.join(buffer)
print data
s.close()
header,html=data.split('\r\n\r\n',1)
print header
with open('music.html','wb') as f:
	f.write(html)

