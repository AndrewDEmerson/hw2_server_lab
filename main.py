#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('', 8000))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(4096)
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.sendall(bytes('\nHTTP/1.1 200 OK\n\n','UTF-8'))
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.sendall(bytes('\nHTTP/1.1 404 Not Found\n\n', 'UTF-8'))
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        # #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data