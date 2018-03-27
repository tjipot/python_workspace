# @Nov 14, 2016 @HYE
# TCP in Python
import socket  # A module of Python

# A socket created, after it, connect needed if you want a connection;
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # 2 args: Address Type, TCP protocal;
s.connect(('www.sina.com.cn', 80)) # Argument is in form of a tuple: (ip/domain, port);

# After connection, data can be sent;
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n') # A TCP connection is a dual connection: any side can send data to the other; HTTP protocal rules the client side should send the data first, which is known as a client request; after receiving the request data, server send the response data(absolutely, the response text data will have a standardized format);

# Receive data;
buffer = [] # buffer is a temporary data hub, this concept is everywhere including in C/C++/JAVA;
while True:
	d = s.recv(1024) # recv(max): max bytes to receive in a time, receive strictly every byte from server, including non-visible characters;
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

# After receiving all data, socket should be closed;
# Don't ask why it is like it, the socket and the rules behind it are invented by someone and there is also the natural laws(include how human manages the things they see in this world) work on it;
s.close()

# A HTTP response has 2 parts: header, body (distinguish with the <header> and <body> tags in .html file)
header, html = data.split(b'\r\n\r\n', 1) # A '\r\n\r\n' is a strict split format between head and body in a http response;
print(header.decode('utf-8'))
# Write the received data into .html file;
with open('sina.html', 'wb') as f:
	f.write(html)











