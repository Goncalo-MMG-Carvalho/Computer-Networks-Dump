import socket

# My vars
serverNumber = 7
serverName   = "Servidor do Gonçalo"

# Prof vars
localIP      = "127.0.0.1"
localPort    = 20001
bufferSize   = 1024


msgFromServer       = str(serverNumber) + "-" + serverName
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while True:

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    arrMsg = message.decode().split("-")
    clientNumberstr = arrMsg[0]
    clientName   = arrMsg[1]

    address = bytesAddressPair[1]

    # clientMsg = "Message from Client:{}".format(message)
    # clientIP  = "Client IP Address:{}".format(address)

    # print(clientMsg)
    # print(clientIP)

    print("Server: " + serverName + ", Client: " + clientName)
    print("Server number: " + str(serverNumber) + ", ClientNumber: " + clientNumberstr)
    print("Sum of numbers: " + str(serverNumber + int(clientNumberstr)) )
    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)