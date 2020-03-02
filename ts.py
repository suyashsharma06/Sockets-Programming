import threading
import time
import random
import socket

topSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("top Socket has been created.")
portBinding = ('', 50000)
topSocket.bind(portBinding)
topSocket.listen(1)
hostName = socket.gethostname()
print("Host Name is " + hostName)
ipAddress = socket.gethostbyname(hostName)
print("The IP Address is " + ipAddress)

# Preprocessing - Creating a nested array for all the links.

f = open("PROJI-DNSTS.txt", "r")
mainArr = []
for x in f:
    word = x.split()
    mainArr.append(word)
f.close()
print(mainArr)

clientSocket, address = topSocket.accept()
# Send message to the client. 
message = "RS is trying to communicate with you (client)"
topSocket.send(message.encode('utf-8'))

topSocket.close()
input("Hit Enter to EXIT")
exit()


# import threading
# import time
# import random
# import socket as mysoc

# # def makeString(intputArr):
# #     outputStr = ""
# #     for x in inputArr:
# #         outputStr = x + " "
# #     return outputStr

# # server task
# def server():
#     try:
#         ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
#         print("[S]: Server socket created")
#     except mysoc.error as err:
#         print('{} \n'.format("socket open error ",err))
#     server_binding=('',50007)
#     ss.bind(server_binding)
#     ss.listen(1)
#     host=mysoc.gethostname()
#     print("[S]: Server host name is: ",host)
#     f = open("PROJI-DNSTS.txt", "r")
#     mainArr = []
#     for x in f:
#         word = x.split()
#         mainArr.append(word)
#     f.close()
#     print(mainArr)
#     localhost_ip=(mysoc.gethostbyname(host))
#     inputStr = "www.rutgers.com"
#     for x in mainArr:
#         for y in x:
#             if (y == inputStr):
#                 print("Got it")
                
#     print("[S]: Server IP address is: ",localhost_ip)
#     csockid,addr=ss.accept()
#     print ("[S]: Got a connection request from a client at", addr)
# # send a intro  message to the client.
#     msg= "Welcome to CS 352"
#     csockid.send(msg.encode('utf-8'))
    

#    # Close the server socket
#     ss.close()
#     exit()


# t1 = threading.Thread(name='server', target=server)
# t1.start()


# input("Hit ENTER to exit")

# exit()