
import threading
import time
import random
import socket as mysoc

# server task - given


def server():
    stringManipulation("Hello")
    try:
        ss = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))
    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = mysoc.gethostname()
    print("[S]: Server host name is: ", host)
    localhost_ip = (mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ", localhost_ip)
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at", addr)

    # While the input data exists, keep on reading the data. When there is no input, it is because we have reached the end of file.
    while True:
        try:
            input = csockid.recv(10240)
            print(input)
            data = input.decode('utf-8')
            print("Client sent: " + data)
            msg = stringManipulation(data)
            csockid.send(msg.encode('utf-8'))
        except mysoc.error:
            print("END OF FILE")
            break
    ss.close()
    exit()

# stringManipulation takes in an input String as a parameter and then returns the string converted to ASCII value, character by character.


def stringManipulation(inputString):
    result = ""
    for element in inputString:
        if len(result) == 0:
            result = result + str(ord(element))
        else:
            result = result + "_" + str(ord(element))
    return result


t1 = threading.Thread(name='server', target=server)
t1.start()

input("Hit ENTER  to exit")

exit()
