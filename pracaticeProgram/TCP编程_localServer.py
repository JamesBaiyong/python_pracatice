#coding=utf-8
import socket,threading,time

#处理每一个连接
def tcpConnect(sock,addr):
	print 'Accept new Connect...'
	sock.send('Welcome...connect me')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if data=='exit' or not data:
			break
		sock.send('Hello,%s!'%data)
	sock.close()
	print 'Connection from %s:%s closed.'%addr

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(4)
print 'Waiting for connection...'

while True:
	#接收新连接
	sock,addr=s.accept()
	t=threading.Thread(target=tcpConnect,args=(sock,addr))
	t.start()


