import socket
import pymongo
from pymongo import MongoClient

def sch_update(conn):
    conn.send("ready".encode())
    
    myclient = pymongo.MongoClient("mongodb://admin:1111@localhost:27017/")
    mydb = myclient["user"]
    mycol = mydb["schedule"]
    print(1)
    date = conn.recv(1024)
    print(1)
    conn.send("date recv".encode())
    print(2)
    content = conn.recv(1024)
    conn.send("cont recv".encode())
    group = conn.recv(1024)
    conn.send("group recv".encode())
    print(111111111)
    olddict=''
    newdict=''
    print(232323123)
    date=date.decode()
    content=content.decode()
    group=group.decode()
    for x in mycol.find({"Date":date, "group_name":group}):
        olddict = x
    newdict = {"Date": date, "content": content, "group_name": group}
    if olddict != '':
        mycol.delete_one(olddict)
    if content != '' :
        mycol.insert_one(newdict)

def sch_find(conn):
    conn.send("ready".encode())
    
    myclient = pymongo.MongoClient("mongodb://admin:1111@localhost:27017/")
    mydb = myclient["user"]
    mycol = mydb["schedule"]

    date = conn.recv(1024)
    conn.send("date recv".encode())
    group = conn.recv(1024)
    conn.send("group recv".encode())

    date=date.decode()
    group=group.decode()
    content = ''
    flag = 0
    for x in mycol.find({"Date":date,"group_name":group}):
        content = x["content"]
        if content:
            find_group = True
            flag = 1
    if flag == 0:
        find_group = False

    msg = conn.recv(1024)
    print(msg.decode())
    print(1)
    if not content:
        print("NO")
        conn.send("False".encode())
    else:
        print("YES")
        conn.send(content.encode())
    print(1)
    

