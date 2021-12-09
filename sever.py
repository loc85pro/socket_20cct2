import socket
import threading
import json
import requests
from requests.api import request

HOST = "127.0.0.1"
PORT  = 65432
FORMAT = "utf8"
#------------------------------------

def registerUser(userName, password):
    data={} 
    with open('userInformation.js') as json_file:
        data = json.load(json_file)
    data['login'].append({
        'userName': userName,
        'password': password
    })
    with open('userInformation.js', 'w') as outfile:
        json.dump(data, outfile)

#----------------------------------

def check_Login(userName, password):
    data={}
    with open('userInformation.js') as json_file:
        data = json.load(json_file)
    for i in data['login']:
        if i['userName'] == userName and i['password'] == password:
            return 1
    return 0

#--------------------------------------

def check_Available_User(user):
    with open('userInformation.js') as json_file:
        data = json.load(json_file)
    for i in data['login']:
        if i['userName']==user:
            return 0
    return 1

#-----------------------------------

def login_User(conn : socket, addr):
    print(addr,": Connected")
    while 1:
        try:
            userName = conn.recv(1024).decode(FORMAT)
            password = conn.recv(1024).decode(FORMAT)
            if check_Login(userName, password)==0:
                conn.sendall("0".encode(FORMAT))
            else:
                conn.sendall("1".encode(FORMAT))
                break
        except:
            print("Error")
            conn.close()        
            break

#----------------------------------------------------------

def getDataAPI():
    key = requests.get("https://vapi.vnappmob.com/api/request_api_key?scope=exchange_rate")
    key = 'Bearer '+key.json()['results']
    header = {
        'Accept': 'application/json',
        'Authorization': key
        }
    data = requests.get("https://vapi.vnappmob.com/api/v2/exchange_rate/sbv", headers = header)
    return data.json()

#----------------------------------------------------------

def Client(conn:socket, addr):
    print(addr, " connected")
    try:
        if conn.recv(1024).decode(FORMAT)=="0":
            print(addr, " registing")
            while 1:
                    userName = conn.recv(1024).decode(FORMAT)
                    password = conn.recv(1024).decode(FORMAT)
                    if check_Available_User(userName)==1:
                        print("ok")
                        conn.sendall("1".encode(FORMAT))
                        registerUser(userName, password)
                        break
                    else:
                        print("nope")
                        conn.sendall("0".encode(FORMAT))
        login_User(conn, addr)
        data = str(getDataAPI())
        print("strlenght data= ", len(data))
        print(data)
        conn.sendall(data.encode(FORMAT))
        print("Sent")
    except:
        return 0

#------------------MAIN----------------------
def main():
    s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()  
    while(1):
        print("Waiting...\n")
        conn, addr = s.accept()
        thr = threading.Thread(target=Client, args=(conn, addr))
        thr.daemon = True
        thr.start()
#-----------------------------

main()
print("Finish")
input()