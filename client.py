
import threading
import time
import random
import socket as mysoc


# client task - given


def client():
    # try:
    #     cs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    #     print("[C]: Client socket created")
    # except mysoc.error as err:
    #     print('{} \n'.format("socket open error ", err))

# Define the port on which you want to connect to the server
    port = 50007
    sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())
# connect to the server on local machine
    server_binding = (sa_sameas_myaddr, port)
    cs.connect(server_binding)

# Opening the file in which string data is present which is to be sent to the server.
    file = open("HW1test.txt", "r")
    for line in file:
        print(line)
        cs.sendall(bytes(line, 'utf-8'))
    file.close()

# Opening the file in which data recieved back from the server has to be written in form of ASCII values.
    writeFile = open("HW1out.txt", "w")

    while True:
        data_from_server = cs.recv(1024)
        strReceived = data_from_server.decode('utf-8')
        print("[C]: Data received from server::  ",
              strReceived)

        writeFile.write(strReceived + "\n")

    writeFile.close()


t2 = threading.Thread(name='client', target=client)
t2.start()

input("Hit ENTER  to exit")

exit()
