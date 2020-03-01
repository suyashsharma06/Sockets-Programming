
import threading
import time
import random
import socket as mysoc


# def makeString(intputArr):
#     outputStr = ""
#     for x in inputArr:
#         outputStr = x + " "
#     return outputStr


# server task - given


def server():
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
    f = open("PROJI-DNSTS.txt", "r")
    mainArr = []
    for x in f:
        word = x.split()
        mainArr.append(word)
    f.close()
    print(mainArr)
    localhost_ip=(mysoc.gethostbyname(host))
    inputStr = "www.rutgers.edu"
    resultStr = ""
    notExist = True
    # Looking for the name in the current directory
    for x in mainArr:
        for y in x:
            if (y == inputStr):
                notExist = False
                resultStr = " ".join(str(p) for p in x)
                print(resultStr)   
    
    # If the lookup is not found, then it has to be redirected to another server.
    if (notExist):
        print("ilab2.cs.rutgers.edu NS")
     

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


t1 = threading.Thread(name='server', target=server)
t1.start()
exit()
