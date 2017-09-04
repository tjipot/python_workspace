# @Nov 15, 2016 @HYE;
# Client Side Of UDP;
import socket, time

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM is UDP type;
# s.connect(('127.0.0.1', 9998))

# print('Bind UDP on 9998...')
# while True:
# 	data, addr = s.recvfrom(1024)
# 	print('Received from %s:%s.' %addr)
# 	s.sendto(b'Hello, %s!' %data, addr)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    time.sleep(1)
    s.sendto(b'Hello, %s!' % data, addr)