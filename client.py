import threading
import time
import random
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client Socket has been created.")
clientAddress = socket.gethostbyname(socket.gethostname())

# Root Server is at port 50,000.
serverBinding = (clientAddress, 50000)
clientSocket.connect(serverBinding)

# Top Server is at port 60,000.
serverBinding2 = (clientAddress, 60000)
clientSocket.connect(serverBinding2)

# Check if return string below matches 
errorMessage = " - Error:HOST NOT FOUND"

# Read line by line, send data to the Root Server and wait for response.
file = open("PROJI-HNS.txt", "r")
for line in file:
    encodedLine = line.encode('utf-8')
    clientSocket.send(encodedLine)
    # Receive Data from RS now.
    receivedData = clientSocket.recv(1024).decode('tuf-8')
    if receivedData == "DOES NOT EXIST":
        # Check Top Server now.
        aowidn = ""
    else:
        writeFile = open("RESOLVED.txt", "a")
        writeFile.write(line + errorMessage)

file.close()


print("Data received from server is " + receivedData.decode('utf-8'))
clientSocket.close()
exit()


# # client task - given

# def client():
#     try:
#         cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
#         print("[C]: Client socket created")
#     except mysoc.error as err:
#         print("{} \n".format("socket open error ",err))

# # Define the port on which you want to connect to the server
#     port = 50007
#     sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())
# # connect to the server on local machine
#     server_binding = (sa_sameas_myaddr, port)
#     cs.connect(server_binding)
#     data_from_server=cs.recv(1024)
# #receive data from the server

#     print("[C]: Data received from server::  ",data_from_server.decode('utf-8'))

# # Opening the file in which string data is present which is first checked on RS, TS.
#     file = open("PROJI-HNS.txt", "r")
#     for line in file:
#         encoded = line.encode('utf-8')
#         print(encoded)
#         cs.send(encoded)
#     file.close()
    
#     toWrite = open("RESOLVED.txt", "w")
#     serverData = data_from_server.decode('utf-8')
#     toWrite.write(serverData + "\n")
#     toWrite.close()

# # Opening the file in which data recieved back from the server has to be written in form of ASCII values.
#     # 

#     # while True:
#     #     data_from_server = cs.recv(1024)
#     #     strReceived = data_from_server.decode('utf-8')
#     #     print("[C]: Data received from server::  ",
#     #           strReceived)

#     #     writeFile.write(strReceived + "\n")

#     # writeFile.close()


# t2 = threading.Thread(name='client', target='client')
# t2.start()
# input("Hit ENTER to Exit")
# exit()
