import hashlib


def main(text, hashType):
   encoder = text.encode('utf-8')
   myHash = ''

   if hashType.lower() == 'md5':
     myHash = hashlib.md5(encoder).hexdigest()

   elif hashType.lower() == 'sha1':
     myHash = hashlib.sha1(encoder).hexdigest()

   elif hashType.lower() == 'sha224':
     myHash = hashlib.sha224(encoder).hexdigest()

   elif hashType.lower() == 'sha256':
     myHash = hashlib.sha256(encoder).hexdigest()

   elif hashType.lower() == 'sha384':
     myHash = hashlib.sha384(encoder).hexdigest()

   elif hashType.lower() == 'sha512':
     myHash = hashlib.sha512(encoder).hexdigest()

   else:
      print("[!!] O script nao suporta esse tipo de hash.")

   print(f"[hash] O seu hash e: {myHash}") 

if __name__ == '__main__':
  verde = "\033[1;32m"
  vermelho = "\033[1;31m"
  reset = "\033[0;0m"
  
  print(f""" {vermelho}
=========3DemonHat6=======
 _   _    _    ____  _   _ 
| | | |  / \  / ___|| | | |
| |_| | / _ \ \___ \| |_| |
|  _  |/ ___ \ ___) |  _  |
|_| |_/_/   \_\____/|_| |_|
@DemonHat... Ja se hackiou?

[*] O script suporta somente tipos: md5, sha1, sha224, sha384, sha512
[*] Se esta usando esta ferramenta gracas aos ensinamentos do Bruno fraga
[*] Criador: -@DemonHat- {reset}

  """)          

  txt = input("[Texto]: ").strip()
  hType = input("[Tipo] Hash: ").strip()
  main(txt,hType)
