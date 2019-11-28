import hashlib
import socket
import Filemethod, Cipher
from time import sleep
import os
s = socket

# 1.fileupload
def fileupload_client(file_directory):
    s.sendall('1'.encode())
    print("recv function 1")

    # file Name & Directory
    fileName = "%s" % file_directory
    directory = ""

    # send fileName
    reReady = s.recv(1024)
    if (reReady.decode() == "Name_ready"):
        splitfile = os.path.split(fileName)
        s.sendall(splitfile[1].encode())
        print("FileName : " + fileName)

    # send file Size
    reReady = s.recv(1024)
    if (reReady.decode() == "Size_ready"):
        s.sendall(Filemethod.getFileSize(fileName).encode())
        print("FileSize : " + Filemethod.getFileSize(fileName))

    # Check Ready
    reReady = s.recv(1024)

    if (reReady.decode() == "data_ready"):
        # encrypt file & send encfile
        encfile = cipher.encrypt(Filemethod.getFileData(fileName))
        print(encfile)
        s.sendall((str(len(encfile)) + "\0").encode())
        print("send enclen")
        s.sendall(encfile.encode())
        print("send encfile")

# 2.filedownload
def filedownload(group_name, file_name):
    s.sendall('2'.encode())
    print("recv function 2")

    # recv ready
    s.recv(1024)

    # ready for recv fileName
    groupName = group_name
    s.sendall(groupName.encode())
    print("send groupName : "+groupName)
    s.recv(1024)
    print(file_name)

    fileName = file_name
    s.sendall(fileName.encode())
    print("send fileName : "+fileName)

    # ready for recv file Size
    reSize = s.recv(1024)
    reSize = reSize.decode()
    print("reSize : " + reSize)

    s.sendall("data_ready".encode())

    dir = "C:\\Users\\" + os.getenv('USERNAME') + "\\Desktop\\" +fileName

    print(dir)
    # recv & write file
    with open(dir, "wb") as f:
        print("in open")
        # encfile Size recv
        encSize = s.recv(1024)
        print("recv encSize")
        nidx = 0
        for i in range(1023):
            if encSize[i] == 0:
                nidx = i
                break
        encSize = encSize[:nidx]

        encSize = encSize.decode()
        data = s.recv(int(encSize), socket.MSG_WAITALL)
        print(data)
        f.write(cipher.decrypt(data))

        print("directory : " + dir)
        print("size : " + reSize)


# 3.check ID
def send_id(userid):
    s.sendall('3'.encode())
    print("recv function 3")

    s.recv(1024)

    ID = userid
    print("ID : " + ID)
    # ID send
    s.send(ID.encode())

    # check
    check = s.recv(1024)
    check = check.decode()
    sleep(1)
    print("check : " + check)
    s.send("good".encode())
    return check


# 4.sign up
def send_userinfo(userid, userpwd, username):
    s.sendall('4'.encode())
    print("recv function 4")
    id = str(userid)
    pwd = userpwd
    name = username

    print(id)
    result2 = hashlib.sha256(pwd.encode()).hexdigest()
    ready = s.recv(1024)
    print(ready)
    s.sendall(id.encode())  # 서버에 메시지 전송
    print("send ID")
    s.recv(1024)
    print("1")

    s.send(result2.encode())  # 서버에 메시지 전송
    print("send PW")
    s.recv(1024)

    s.send(name.encode())  # 서버에 메시지 전송
    print("send name")
    s.recv(1024)


# 5.make group
def mk_group(group_list):
    s.sendall('5'.encode())
    print("recv function 5")
    print(group_list)
    # ready
    check_ready = s.recv(1024)
    print(check_ready.decode())
    tmp = 0
    for i in group_list:
        if not i:
            tmp += 1
    for i in range(tmp):
        del(group_list[6 - tmp])
    for i in range(tmp):
        group_list.append("NULL")
    for i in group_list:
        s.send(i.encode())
        get_msg = s.recv(1024)
        print(get_msg.decode())
    print("send group list")


# 6.login
def login(username, userpwd):
    s.sendall('6'.encode())
    print("recv function 6")

    str1 = "%s" % username
    str2 = "%s" % userpwd

    # ready
    s.recv(1024)

    # hash-256 pwd
    result2 = hashlib.sha256(str2.encode()).hexdigest()

    # id send
    s.send(str1.encode())
    print("send login ID")

    # ready
    s.recv(1024)

    # hash pwd send
    s.send(result2.encode())
    print("send login hash PW")

    Is_login_OK = s.recv(1024)
    Is_login_OK = Is_login_OK.decode()
    print("login OK : " + Is_login_OK)

    if Is_login_OK == "False":
        return False
    else:
        print(1)
        s.send("ready".encode())
        Is_Auth_OK = s.recv(1024)
        s.send("1".encode())
        Is_Auth_OK = Is_Auth_OK.decode()
        print(Is_Auth_OK)
        if Is_Auth_OK == "True":
            group_count = s.recv(1024)
            print("group count : " + group_count.decode())
            group_count = int(group_count.decode())
            s.send("ready".encode())
            group_name_list = []
            print(group_count, "done")
            for x in range(group_count):
                gr_name = s.recv(1024)
                s.send("get_group".encode())
                group_name_list.append(gr_name.decode())
            print("break")
            for i in range(5 - group_count):
                group_name_list.append('')
            print("dfajlsjdfkjsaldjflsajdlf")
            print(group_name_list)
            return group_name_list
        else:
            return

# 7.group check
def send_group(groupname):
    s.sendall('7'.encode())
    print("recv function 7")

    s.recv(1024)

    ID = groupname

    # ID send
    s.send(ID.encode())
    print("send groupname : " + groupname)

    # check
    check = s.recv(1024)
    check = check.decode()
    print("check : " + check)


# 8.send schedule
def send_schedule(now_date, text, groupname):
    s.sendall('8'.encode())
    print("recv function 8")
    # ready
    s.recv(1024)

    date = now_date
    content = text
    group_name = groupname

    print("date : " + date)

    s.send(date.encode())
    print("send date")
    s.recv(1024)

    s.send(content.encode())
    print("send content")
    s.recv(1024)

    s.send(group_name.encode())
    print("send group name")
    s.recv(1024)

# 9.find schedule
def find_schedule(nowdate, gruopname):
    s.sendall('9'.encode())
    print("recv function 9")
    # ready
    s.recv(1024)

    date = nowdate
    group_name = gruopname
    s.send(date.encode())
    print("send date")
    s.recv(1024)

    s.send(group_name.encode())
    print("group name")
    s.recv(1024)

    s.send("ready".encode())

    content = s.recv(1024)
    content = content.decode()
    print("recv content : " + content)

    return content


# 10.get file list
def get_file_list(groupname):
    s.sendall('10'.encode())
    print("recv function 10")
    group_name = groupname

    print("group name : " + group_name)

    # ready
    s.recv(1024)
    file_list = []

    s.send(group_name.encode())
    print("send group name")

    file_len = s.recv(1024)
    file_len = file_len.decode()
    print("recv file len : " + file_len)
    file_len = int(file_len)

    s.send("1".encode())
    for i in range(file_len):
        file_name = s.recv(1024)
        file_name = file_name.decode()
        file_list.append(file_name)
        s.send("1".encode())
    return file_list

# 11.get date list
def get_date_list(groupname):
    print("recv function 11")
    group_name = groupname
    print(group_name)
    date_list = []

    inp_date_len = s.recv(1024)
    inp_date_len = inp_date_len.decode()
    print(inp_date_len)
    date_len = int(inp_date_len)
    print(1)
    s.send("1".encode())
    for i in range(date_len):
        date_name = s.recv(1024)
        date_name = date_name.decode()
        date_list.append(date_name)
        s.send("1".encode())
    return date_list

#def login_close():
#    s.sendall('11'.encode())
#    s.close()

def connect(ip):
    global s
    # HOST = '192.168.137.155'
    PORT = 8888
    HOST = ip
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))


# AES KEY
key = 'abcdefg'
cipher = Cipher.AESCipher(key)
