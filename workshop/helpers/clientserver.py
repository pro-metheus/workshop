from socket import *

def create_server(ip='127.0.0.1',port=1234,accept=2):
    server=socket(AF_INET,SOCK_STREAM)
    server.bind((ip,port))
    server.listen(accept)
    return server


def runserver(server):
    client,port=server.accept()
    return client,port

def send(server,msg):
    server.send(str(msg).encode())


def rec(client):
    data=client.recv(1024).decode()
    return data


def openchat_s(server,client):
    if client:
        while True:
            data=input('?')
            send(server,data)
            msg=rec(client)
            print(msg)

def create_client(ip='127.0.0.1',port=1234,accept=2):
    client=socket(AF_INET,SOCK_STREAM)
    client,port=client.connect((ip,port))
    return client,port

def openchat_c(client):
    if client:
        while True:
            msg=rec(client)
            print(msg)
            data=input('?')
            send(client,data)

            
