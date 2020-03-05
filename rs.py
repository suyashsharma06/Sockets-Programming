import threading
import time
import random
import socket
import argparse

# Parsing the arguements.
parser = argparse.ArgumentParser()
parser.add_argument('rsListenPort', type=int, help='Root Server Port Number')
args = parser.parse_args()
rsPORT = args.rsListenPort # Root Server Port Number.

def rootServer():

    # Preprocessing - Creating a dictionary.

    f = open("PROJI-DNSRS.txt", "r")
    dictionary = {}
    for x in f:
        x = x.strip()
        word = x.split(' ')
        lastElement = len(word) - 1
        if (word[lastElement] == "NS"):
            dictionary['tsHostname'] = x
        else:
            dictionary[word[0]] = x
    f.close()

    # Creating Socket and doing all the connection requirements here.

    rootSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Root Socket has been created.")
    portBinding = ('', rsPORT)
    rootSocket.bind(portBinding)
    rootSocket.listen(5)
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)
    print("Host Name is " + hostName + ". The IP Address is " + ipAddress + " . The PORT IS ", rsPORT)

    clientSocketID, address = rootSocket.accept()
    print("got a connection request from: ", address)

    while True:
        data = clientSocketID.recv(1024).decode('utf-8').strip()
        print(data)
        if not data:
            break
        if data in dictionary:
            res = dictionary.get(data)
            clientSocketID.sendall(res.encode('utf-8'))
        else:
            clientSocketID.sendall(dictionary.get('tsHostname').encode('utf-8'))

    # Now wait for connection from Client to run queries.
    clientSocketID.close()
    rootSocket.close()
    exit()

t1 = threading.Thread(name='rootServer', target=rootServer)
t1.start()
exit()
