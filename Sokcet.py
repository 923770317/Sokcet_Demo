from socket import *
from time import ctime

host = ''
port = 21567
bufsize = 1024
addr =(host,port)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(addr)
tcpSerSock.listen(5)

while True:
    print 'waiting  for connection ....'
    tcpCliSokc,c_addr = tcpSerSock.accept()
    print '.....connected from ',addr

    while True:
        data = tcpCliSokc.recv(bufsize)
        if not data:
            break
        tcpCliSokc.send('[%s] %s' %(ctime(),data))
    tcpCliSokc.close()

tcpSerSock.close()