import socket
import pymongo
import uuid
import hashlib
from time import sleep
#
# # 통신 정보 설정
# from pymongo import MongoClient
# IP = ''
# PORT = 5050
# SIZE = 1024
# ADDR = (IP, PORT)
# name = ''
# pwd = ''
# #nickname = ''
# salt=''
#
# # 서버 소켓 설정
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#
# # 포트 사용중이라 연결할 수 없다는
# # WinError 10048 에러 해결를 위해 필요합니다.
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# server_socket.bind(ADDR)
# server_socket.listen()
#
# client_socket, addr = server_socket.accept()
#
# print('connected by',addr)
#def login_server():
    # 무한루프를 돌면서
def login(conn):
    
    conn.send("ready".encode())
    
    # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다.
    d_name = conn.recv(1024).decode()
    print("name:"+d_name)

    conn.send("ready".encode())
    d_pwd = conn.recv(1024).decode()
    print("pwd:"+d_pwd)
    # 빈 문자열을 수신하면 루프를 중지합니다

   
    #db에 받아온 정보 저장
    myclient = pymongo.MongoClient("mongodb://admin:1111@127.0.0.1:27017/")
    mydb = myclient["user"]
    myinfo = mydb["user_info"]
    myauth = mydb["user_permission"]
    mygroup = mydb["group"]

    ##db에서 아이디 토대로 솔트찾고 솔트랑 d_pwd 더해서 해쉬
    for x in myinfo.find({"name":d_name}):
        salt=x["salt"]

    c_pwd= hashlib.sha256((d_pwd+salt).encode()).hexdigest()
    print(c_pwd) 
    check=''
    flag = 0
    for y in myinfo.find({"pwd":c_pwd}):
        check=y["pwd"]
        
        if check:
            global user_id
            user_id = d_name
            login=True
            flag = 1
            conn.send("True".encode())
            break
    if flag == 0:
        login = False
        conn.send("False".encode())
        return
    user_auth_list = []
    group_name_list = []
    auth=""
    Is_Auth_OK = False
    for x in myauth.find({"name":user_id}):
        auth=x["auth"]
        user_auth_list.append(auth)
        Is_Auth_OK = True
    if Is_Auth_OK == True:
        conn.send("True".encode())
        conn.recv(1024)
        for x in user_auth_list:
            tmp_group_num = int(x) // 10
            print(tmp_group_num)
            for y in mygroup.find({"num":tmp_group_num}):
                print(y["name"])
                group_name_list.append(y["name"])
        print("auth_list_OK")
        len_group_name_list = str(len(group_name_list))
        conn.send(len_group_name_list.encode())
        conn.recv(1024).decode()
        for x in group_name_list:
            # 클라이언트에 그룹명을 보내는 명령어로 대체
            conn.send(x.encode())
            print("group name sent:"+x)
            res = conn.recv(1024)
            print(res.decode())
        return
    else:
        conn.recv(1024)
        conn.send("False".encode())
        conn.recv(1024)
        return
#client_socket.sendall(str(login).encode())
#sleep(1)
# client_socket.close()
# server_socket.close()
