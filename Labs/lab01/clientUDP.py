import socket

# My vars
clientName          = "Client of Carvalho"
clientNumber        = input("Input a number between 1 and 100, inclusive")



msgFromClient       = clientNumber + "-" + clientName

print("|" + msgFromClient + "|")

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

 # Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])

#print(msg)

arrMsg          = msg.decode().split("-")
serverNumberstr = arrMsg[0]
serverName      = arrMsg[1]

print("Server number: " + serverNumberstr + ", ClientNumber: " + clientNumber)
print("Sum of numbers: " + str( int(serverNumberstr) + clientNumber ))