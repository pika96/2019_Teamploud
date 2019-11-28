import socket
import pymongo
import uuid
import hashlib
from pymongo import MongoClient

# # 통신 정보 설정
# IP = ''
# PORT = 5050
# SIZE = 1024
# ADDR = (IP, PORT)
# name = ''
# pwd = ''
# nickname = ''
salt=uuid.uuid4().hex
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

def signup(conn):
    # 무한루프를 돌면서

    conn.send("func_ready".encode())
    print("sent")


    # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다
    d_name = conn.recv(1024)
    d_name = d_name.decode()
    print("name:"+d_name)
    conn.send("name".encode())

    d_pwd = conn.recv(1024).decode()
    print("pwd"+d_pwd)
    conn.send("pwd".encode())

    d_nick = conn.recv(1024).decode()
    print("nickname : "+d_nick)
    conn.send("nickname".encode())


    
    d_pwd = hashlib.sha256((d_pwd+salt).encode()).hexdigest()
    
    myclient = pymongo.MongoClient("mongodb://admin:1111@127.0.0.1:27017/")
    mydb = myclient["user"]
    mycol = mydb["user_info"]


    #db에 받아온 정보 저장
    print(d_pwd)

    mydict = {"name":d_name,"pwd":d_pwd, "nickname":d_nick, "salt": salt}

   
    x = mycol.insert_one(mydict)
