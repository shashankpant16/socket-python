#! /usr/bin/python3

import socket

#creating udp socket
#                       IPv4           UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#now generating message to send
msg = input("please enter your message:- ")

#where to send data
target_ip = "13.233.180.208"
target_port = 8888

#finally sending data
s.sendto(msg.encode('ascii'),(target_ip,target_port))

#now receiving the data
print(s.recvfrom(100))


