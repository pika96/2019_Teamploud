# python3
import socket
import sys
import threading
import Cipher
import Filemethod
import signup_server
import mkgroup_server
import check_id
import login_server
import select_group
import check_group
import sch_server
t=[]
index=0



# AES KEY
key = 'abcdefg'
cipher = Cipher.AESCipher(key)

def filerecv_server(conn, grouppath):
    print(1)
    # ready for recv fileName
    conn.sendall("Name_ready".encode())
    fileName = conn.recv(1024)
    fileName = fileName.decode()

    # ready for recv file Size
    conn.sendall("Size_ready".encode())
    reSize = conn.recv(1024)
    reSize = reSize.decode()

    conn.sendall("data_ready".encode())

    # recv & write file
    print(grouppath)
    with open(grouppath+"/"+fileName, "wb") as f:
        # encfile Size recv
        encSize = conn.recv(1024)
        nidx = 0
        for i in range(1023):
            if encSize[i] == 0:
                nidx = i
                break
        encSize = encSize[:nidx]

        encSize = encSize.decode()
        data = conn.recv(int(encSize), socket.MSG_WAITALL)
        f.write(cipher.decrypt(data))

        print("file name : " + fileName)
        print("size : " + reSize)

def filesend_server(conn, grouppath):
    # file Name & Directory
    #fileName = "test.hwp"
    #directory = ""

    # recv GN
    conn.sendall("ready".encode())
    groupName = conn.recv(1024)
    groupName = groupName.decode()

    conn.sendall("ready".encode())

    # recv filename
    fileName = conn.recv(1024)
    fileName = fileName.decode()

    conn.sendall(Filemethod.getFileSize(fileName, grouppath).encode())


    # Check Ready
    reReady = conn.recv(1024)
    if (reReady.decode() == "data_ready"):
        # encrypt file & send encfile
        encfile = cipher.encrypt(Filemethod.getFileData(fileName, grouppath))
        conn.sendall((str(len(encfile)) + "\0").encode())
        conn.sendall(encfile.encode())

def connect(conn, addr, index):
    index=index+1
    grouppath = ''
    try:
        while True:
            # receive function
            func = conn.recv(1024)
            func = func.decode()
            print(func)
            if not func:
                conn.close()
                print("disconnect")
                break
            # file upload (client -> server)
            if func == '1':
                filerecv_server(conn, grouppath)

            # file download (server -> client)
            elif func == '2':
                filesend_server(conn,grouppath)
            elif func == '3':
                check_id.check_id(conn)
            elif func == '4':
                signup_server.signup(conn)
            elif func == '5':
                mkgroup_server.make_group(conn)
            elif func == '6':
                login_server.login(conn)
            elif func == '7':
                check_group.check_group(conn)
            elif func == '8':
                sch_server.sch_update(conn)
            elif func == '9':
                print(func)
                sch_server.sch_find(conn)
            elif func == '10':
                grouppath = select_group.select_group(conn)
       


    except:
        print("disconnect")
        exit(0)



HOST = '192.168.56.102'  # all available interfaces
PORT = 8888

# 1. open Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# 2. bind to a address and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind Failed. Error code: ' + str(msg[0]) + ' Message: ' + msg[1])
    sys.exit()

print('Socket bind complete')

# 3. Listen for incoming connections
s.listen(1)
print('Socket now listening')

while 1:
    # 4. Accept connection
    conn, addr = s.accept()
    print('connect with client')
    thconn = threading.Thread(target=connect, args=(conn,addr,index))
    thconn.start()
    t.append(thconn)

    print(t[index])

for i in t:
    t.join()

s.close()
