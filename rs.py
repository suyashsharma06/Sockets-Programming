import threading
import time
import random
import socket

rootSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Root Socket has been created.")
portBinding = ('', 50000)
rootSocket.bind(portBinding)
rootSocket.listen(1)
hostName = socket.gethostname()
print("Host Name is " + hostName)
ipAddress = socket.gethostbyname(hostName)
print("The IP Address is " + ipAddress)

# Preprocessing - Creating a nested array for all the links.

f = open("PROJI-DNSRS.txt", "r")
mainArr = []
for x in f:
    word = x.split()
    mainArr.append(word)
f.close()
print(mainArr)

clientSocket, address = rootSocket.accept()
# Send message to the client. 
message = "RS is trying to communicate with you (client)"
rootSocket.send(message.encode('utf-8'))

rootSocket.close()
input("Hit Enter to EXIT")
exit()


# def server():
#     try:
#         ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         print("[S]: Server socket created")
#     except socket.error as err:
#         print('{} \n'.format("socket open error ", err))
#     server_binding = ('', 50007)
#     ss.bind(server_binding)
#     ss.listen(1)
#     host = socket.gethostname()
#     print("[S]: Server host name is: ", host)
#     localhost_ip = (socket.gethostbyname(host))

#     # Open file and read all the data and store it in Data Structure
#     f = open("PROJI-DNSTS.txt", "r")
#     mainArr = []
#     for x in f:
#         word = x.split()
#         mainArr.append(word)
#     f.close()
#     print(mainArr)
#     localhost_ip=(socket.gethostbyname(host))

#     # Get data from Client.    
#     inputStr = ""
#     print("[S]: Server IP address is  ", localhost_ip)

#     while True:
#         csockid, addr = ss.accept()
#         print("[S]: Got a connection request from a client at", addr)
#         intro = "rs is working..."
#         csockid.send(intro.encode('utf-8'))
#         input = csockid.recv(1024)
#         if not input:
#             break
#         receivedData = input.decode('utf-8')
#         print(receivedData)
#         csockid.sendall()
#         csockid.close()


#     resultStr = ""
#     notExist = True
#     # Looking for the name in the current directory
#     for x in mainArr:
#         for y in x:
#             if (y == inputStr):
#                 notExist = False
#                 resultStr = " ".join(str(p) for p in x)
#                 print(resultStr)   
    
#     # If the lookup is not found, then it has to be redirected to another server.
#     if (notExist):
#         print("ilab2.cs.rutgers.edu NS")

#     ss.close()
#     exit()


# t1 = threading.Thread(name="server", target="client")
# t1.start()
# input("Hit ENTER to Exit \n")
# exit()
