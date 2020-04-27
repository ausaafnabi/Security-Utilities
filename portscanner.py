#!/usr/bin/env python3
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear',shell=True)

remoteServer = input("Enter a remote host to scan : ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Printing a nice banner with information on which host we are about to scan

print("-"*60)
print("Please wait, scanner remote host",remoteServerIP)
print("-"*60)

#Check what time the scan started

t1 = datetime.now()
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        if result ==0:
            print("PORT {}: Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.Exiting")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()

t2 = datetime.now()

total = t2-t1

#Printing the information to the screen
print("Scanner Complete in : "+total)

