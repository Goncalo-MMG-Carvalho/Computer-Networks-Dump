#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cpm
"""
"""
from socket import *

serverName = "localhost"            # server name
serverPort = 12000                  # socket server port number
sockBuffer = 2048                   # socket buffer size

def main():
    clientSocket = socket(AF_INET,SOCK_STREAM)       # create TCP socket
    clientSocket.connect((serverName, serverPort))   # open TCP connection

    clientName = input("Input a name: ")   # take input
    num = input("Input a number: ")

    if int(num) < 0 or int(num) > 100:
        print("Invalid number")
        clientSocket.close()
        exit(69420)


    clientSocket.send((clientName + "-" + num).encode())             # send user's sentence
                                                                   # over TCP connection

    receivedSentence = clientSocket.recv(sockBuffer).decode()  # receive response
    #print("Message received: ", receivedSentence)

    arrServer = receivedSentence.split("-")

    print("Client's Name: " + clientName + ", Server's Name: " + arrServer[0])
    print("Client's Number: " + num + ", Server's Number: " +
          str(arrServer[1]) + ", Sum of numbers: " + str(int(num) + int(arrServer[1])))
    
    clientSocket.close()            # close TCP connection

main()
"""

from socket import *
import time

serverName = "localhost"  # server name
serverPort = 12000  # socket server port number
sockBuffer = 1024  # socket buffer size

fileName = "hello.txt"

def main():
    clientSocket = socket(AF_INET, SOCK_STREAM)  # create TCP socket
    clientSocket.connect((serverName, serverPort))  # open TCP connection

    clientSocket.setblocking(0)

    clientSocket.send(fileName.encode())  # send user's sentence
    # over TCP connection

    while True:
        time.sleep(0.1)
        data = clientSocket.recv(sockBuffer)
        if data:
            # Process the received data here
            print(data.decode())

        else:
            # No data received, the connection might have been closed
            break



    clientSocket.close()  # close TCP connection


main()