from socket import *

host = '172.29.32.162'
port = 21567
bufsize = 1024
addr =(host,port)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(addr)

while True:
    data= raw_input(">")
    if not data:
        break

    tcpCliSock.send(data)
    data = tcpCliSock.recv(bufsize)
    if not data:
        break
    print data
tcpCliSock.close()
