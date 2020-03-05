import threading
import time
import random
import socket
import argparse

# Parsing the arguements.
parser = argparse.ArgumentParser()
parser.add_argument('rsHostname', type=str, help='Root Server Host Name')
parser.add_argument('rsListenPort', type=int, help='Root Server Port Number')
parser.add_argument('tsListenPort', type=int, help='Top Server Port Number')
args = parser.parse_args()

rsPORT = args.rsListenPort
tsPORT = args.tsListenPort
hostname = args.rsHostname

def client():

    dataStore = []

    try:        
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Client Socket has been created.")
    except socket.error as err:
        print("Socket Open Error: " + err)
        
    serverBinding = (hostname, rsPORT)
    clientSocket.connect(serverBinding)

    file = open("PROJI-HNS.txt", "r")
    failSwitch = True
    for line in file:
        line = line.lower()
        clientSocket.sendall(line.encode('utf-8'))
        time.sleep(0.5) # Make the client wait for a message from the Root Server.
        message_from_rs = clientSocket.recv(1024).decode('utf-8')
        print(message_from_rs)
        arr = message_from_rs.split(' ')
        if arr[-1] == "NS":
            if failSwitch:
                newServerBinding = (arr[0], tsPORT)
                clientSocket2.connect(newServerBinding)
                failSwitch = False
            clientSocket2.sendall(line.encode('utf-8'))
            message_from_ts = clientSocket2.recv(1024).decode('utf-8')
            if message_from_ts == "Error:HOST NOT FOUND":
                print(line.strip() + " - " + message_from_ts.strip())
                dataStore.append(line.strip() + " - " + message_from_ts.strip())
            else:
                print(message_from_ts.strip())
                dataStore.append(message_from_ts.strip())
        else:
            dataStore.append(message_from_rs)
    file.close()

    clientSocket.close()

    # At the end, write all the data from Data Store to the RESOLVED.txt.

    file = open("RESOLVED.txt", "w")
    counter = 0
    for entry in dataStore:
        lastIndex = len(dataStore) - 1
        if counter == lastIndex:
            file.write(entry)
        else:
            file.write(entry+'\n')

        counter += 1
    file.close()

    exit()

t1 = threading.Thread(name='client', target=client)
t1.start()
exit()