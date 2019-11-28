import socket
import pymongo
import uuid
import hashlib
import os
from pymongo import MongoClient


# # 통신 정보 설정
# IP = ''
# PORT = 5050
# SIZE = 1024# ADDR = (IP, PORT)
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

def make_group(conn):
    # 무한루프를 돌면서
    conn.send("ready".encode())

    # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다.
    gname = conn.recv(1024)
    print("group name:"+gname.decode())
    conn.send("ready".encode())
  
    mem1 = conn.recv(1024)
    print("mem1:"+mem1.decode())
    conn.send("ready".encode())

    mem2 = conn.recv(1024)
    print("mem2:"+mem2.decode())
    conn.send("ready".encode())

    mem3 = conn.recv(1024)
    print("mem3:"+mem3.decode())
    conn.send("ready".encode())
       
    mem4 = conn.recv(1024)
    print("mem4:"+mem4.decode())
    conn.send("ready".encode())
    
    mem5 = conn.recv(1024)
    print("mem5:"+mem5.decode())
    conn.send("ready".encode())
    
    # 빈 문자열을 수신하면 루프를 중지합니다
         
    d_gname = gname.decode()
    d_mem1 = mem1.decode()
    d_mem2 = mem2.decode()
    d_mem3 = mem3.decode()
    d_mem4 = mem4.decode()
    d_mem5 = mem5.decode()

    # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코)
    #client_socket.sendall(name+pwd+nickname)


    #db에 받아온 정보 저장
    myclient = pymongo.MongoClient("mongodb://admin:1111@127.0.0.1:27017/")
    mydb = myclient["user"]
    mycol1 = mydb["group"]
    mycol2 = mydb["user_permission"]
    
    group_list = []
    for x in mycol1.find():
        group_list.append(x)
    group_count = len(group_list) + 1
    print(group_count)
    mydict = {"name":d_gname,"num":group_count}
    admin_auth = group_count * 10 + 1
    member_auth = group_count * 10
    admin_auth = str(admin_auth)
    member_auth = str(member_auth)
    #mylist = [
    #        {'name':d_mem1,'auth':admin_auth},
    #        {'name':d_mem2,'auth':member_auth},
    #        {'name':d_mem3,'auth':member_auth},
    #        {'name':d_mem4,'auth':member_auth},
    #        {'name':d_mem5,'auth':member_auth}
    #        ]

    x = mycol1.insert_one(mydict)
    #y = mycol2.insert_many(mylist)
    
    if d_mem1 !='NULL':
        mylist = {'name':d_mem1, 'auth':admin_auth}
        mycol2.insert_one(mylist)
     
    if d_mem2 !='NULL':
        mylist = {'name':d_mem2, 'auth':member_auth}
        mycol2.insert_one(mylist)
     
    if d_mem3 !='NULL':
        mylist = {'name':d_mem3, 'auth':member_auth}
        mycol2.insert_one(mylist)
     
    if d_mem4 !='NULL':
        mylist = {'name':d_mem4, 'auth':member_auth}
        mycol2.insert_one(mylist)
     
    if d_mem5 !='NULL':
        mylist = {'name':d_mem5, 'auth':member_auth}
        mycol2.insert_one(mylist)
    curpath = "/workspace/" + d_gname
    os.makedirs(curpath)           
