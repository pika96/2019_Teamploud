import socket
import pymongo
import uuid
import hashlib
import os
from pymongo import MongoClient

group_count = 0

# # 통신 정보 설정
# IP = ''
# PORT = 5050
# SIZE = 1024
# ADDR = (IP, PORT)
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

def select_group(conn):
    # 무한루프를 돌면서
    conn.send("ready".encode())

    # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다.
    group_name = conn.recv(1024)
    d_group_name = group_name.decode()
    print(d_group_name)
    #db에 받아온 정보 저장
    myclient = pymongo.MongoClient("mongodb://admin:1111@localhost:27017/")
    mydb = myclient["user"]
    mycol = mydb["schedule"]

    file_list = []
    cur_path = "/workspace/" + d_group_name
    for root, dirs, files in os.walk(cur_path):
        for file in files:
            file_list.append(file)
    file_len = str(len(file_list))
    print(file_len)
    conn.send(file_len.encode())

    conn.recv(1024)
    for x in file_list:
        conn.send(x.encode())
        print("file list:"+x)
        conn.recv(1024)
    
    date_list = []
    for x in mycol.find({"group_name":d_group_name}):
        x = x["Date"]
        date_list.append(x)
    date_len = str(len(date_list))
    conn.send(date_len.encode())
    print("date len:"+date_len)
    msg = conn.recv(1024)
    print(msg.decode())
    for x in date_list:
        conn.send(x.encode())
        print("date list:"+x)
        conn.recv(1024)
    
    print(cur_path)
    return cur_path
