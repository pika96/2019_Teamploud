import socket
import pymongo
import uuid
import hashlib
from time import sleep
from pymongo import MongoClient

# # 통신 정보 설정
# IP = ''
# PORT = 5050
# SIZE = 1024
# ADDR = (IP, PORT)
# name = ''
# pwd = ''
# # nickname = ''
# salt = ''
#
# # 서버 소켓 설정
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
# print('connected by', addr)


def check_id(conn):
    # 무한루프를 돌면서
 
    conn.send("ready".encode())
  
    
    # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다.
    d_name = conn.recv(1024).decode()
    print("name:"+d_name)
    # pwd = client_socket.recv(1024)
    
    #d_name = name.decode()

    # 소켓을 닫습니다.
    # client_socket.close()
    # server_socket.close()

    # db에 받아온 정보 저장
    myclient = pymongo.MongoClient("mongodb://admin:1111@127.0.0.1:27017/")
    mydb = myclient["user"]
    mycol = mydb["user_info"]
    ##db에서 사용자 id검색
    check = ''
    flag = 0
    for y in mycol.find({"name": d_name}):
        check = y["name"]
        if check:
            login = True
            flag = 1
    if flag == 0:
        login = False

    conn.sendall(str(login).encode())
    conn.recv(1024)
