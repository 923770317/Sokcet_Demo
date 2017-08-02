from socket import *
from time import ctime

host = ''
port = 21567
bufsize = 1024
addr =(host,port)

udpSerSokc = socket(AF_INET,SOCK_DGRAM)
udpSerSokc.bind(addr)

while True:
    print 'waiting for message....'
    data,addr = udpSerSokc.recvfrom(bufsize)
    udpSerSokc.sendto('[%s] %s' %(ctime(),data),addr)
    print '...received from adn return to :',addr
udpSerSokc.close()