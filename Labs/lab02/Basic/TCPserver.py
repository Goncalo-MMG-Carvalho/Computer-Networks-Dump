#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cpm
"""
"""
from socket import *

serverPort = 12000
sockBuffer = 2048

serverName   = "Amazon Web Services Server"
serverNumber = 1

def main():

    serverSocket = socket(AF_INET,SOCK_STREAM)   # create TCP welcoming socket
    serverSocket.bind(("", serverPort))

    serverSocket.listen(1)              # begin listening for incoming TCP requests
    print("Server is running")

    while True:
        connSocket, addr = serverSocket.accept()    # waits for incoming requests:
                                                    # new socket created on return
        print("Connected by: ", str(addr))

        sentence = connSocket.recv(sockBuffer).decode()     # read a sentence of bytes
                                                            # received from client
  
        print("Data from connected user: ", sentence)       # display received sentence

        arr = sentence.split("-")

        if int(arr[1]) < 0 or int(arr[1]) > 100:
            print("Number received from client is invalid.")
            connSocket.close()
            exit(69420)

        print("Client's Name: "+ arr[0] + ", Server's Name: " + serverName)
        print("Client's Number: " + arr[1] + ", Server's Number: " + str(serverNumber) + ", Sum of numbers: " + str(int(arr[1]) + serverNumber) )


        setenceServer = serverName + "-" + str(serverNumber)

        connSocket.send(setenceServer.encode())             # send modified sentence over
                                                            # TCP connection

        connSocket.close()      # close TCP connection:
                                # the welcoming socket continues

main()
"""

from socket import *

serverPort = 12000
sockBuffer = 2048

serverName   = "Amazon Web Services Server"
serverNumber = 1

def main():

    serverSocket = socket(AF_INET,SOCK_STREAM)   # create TCP welcoming socket
    serverSocket.bind(("", serverPort))

    serverSocket.listen(1)              # begin listening for incoming TCP requests
    print("Server is running")

    while True:
        connSocket, addr = serverSocket.accept()    # waits for incoming requests:
                                                    # new socket created on return
        print("Connected by: ", str(addr))

        clientSentence = connSocket.recv(sockBuffer).decode()     # read a sentence of bytes
                                                                  # received from client

        clientSentence = "D:\Programas em Python\\" + clientSentence

        file = open(clientSentence, "r")



        while True:
            setenceServer = ""
            setenceServer = file.read(1024)

            if len(setenceServer) <= 0:
                break

            connSocket.send(setenceServer.encode())             # send modified sentence over
                                                                # TCP connection

        connSocket.close()      # close TCP connection:
                                # the welcoming socket continues

main()
