# @Nov 15, 2016 @HYE
# TCP Server in Python
# Step 1: bind a port, cause it is in an OS, you should obey to OS;
# Step 2: a socket relies on: server ip address, server port, client ip address, client port;
# Step 3: a server should response to many clients, so multi-process/thread is required;
import socket
import time, threading


# TCP Server: create a IPv4 and TCP socket firstly;
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 9999))
s.listen(2)		# Max connections = 5; 	
print('Waiting for connection...')

def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' %addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(5)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' %data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' %addr)

while(True):
	sock, addr = s.accept()
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()




