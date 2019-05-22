import socket

target_ip = "0.0.0.0"
target_port = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((target_ip,8888))
while True:
 data = s.recvfrom(100)
 print(data)

