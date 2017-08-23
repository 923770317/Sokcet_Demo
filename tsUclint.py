from socket import *

host ='172.29.32.162'
port = 21567
bufsize = 1024
addr =(host,port)
udpCliSokc = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    udpCliSokc.sendto(data,addr)
    data,addr = udpCliSokc.recvfrom(bufsize)
    if not data:
        break
    print data

udpCliSokc.close()