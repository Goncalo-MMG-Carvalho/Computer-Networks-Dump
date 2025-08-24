#!/usr/bin/env python3

# Importing libraries
from socket import *

serverName = "localhost"
serverPort = 8000
#print("Server info: ", serverName, str(serverPort))

bufferSize = 2048

# Ask file fig.jpg
msg1 = "GET index.html HTTP/1.0\r\n"
msg2 = "host:localhost:8000\r\n"
msg3 = "\r\n"

s = socket(AF_INET,SOCK_STREAM)
s.connect((serverName, serverPort))
s.send((msg1+msg2+msg3).encode())

#infile = open("nova_5.png", "wb")
infile = open("index2.txt", "wb")

while True:
    data = s.recv(bufferSize)
    # recebe dados do servidor
    # processa response message (header e body)
    #process http response message

    if len(data) == 0:
        break

    infile.write(data)
    #print(data.decode())

infile.close()

infile = open("index2.txt", "r")
lines = infile.read().splitlines()
infile.close()

header = ""
i = 0

while i + 1 < len(lines):
    if lines[i] == "" and lines[i + 1] == "":
        i += 1
        break
    header += lines[i] + "\n"
    i += 1


infile = open("index2.html", "w")
while i < len(lines):
    data = lines[i]
    infile.write(data + "\n")
    i += 1

infile.close()
s.close()
print("Connection close")
