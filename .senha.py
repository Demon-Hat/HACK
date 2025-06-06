from itertools import product

# Função para gerar variações de strings
def gerar_variacoes(base):
    sufixos = ["", "123", "1234", "2024", "!", "@", "#", "_", ".", "01"]
    variacoes = set()
    for palavra in base:
        for sufixo in sufixos:
            variacoes.add(palavra.lower() + sufixo)
            variacoes.add(palavra.capitalize() + sufixo)
            variacoes.add(palavra.upper() + sufixo)
    return variacoes

# Função principal para gerar a wordlist
def gerar_wordlist(nome, sobrenome, nascimento, cidade, ip, favoritos):
    componentes = []

    if nome:
        componentes.append(nome)
    if sobrenome:
        componentes.append(sobrenome)
    if nascimento:
        nascimento = nascimento.replace("/", "").replace("-", "")
        componentes.append(nascimento)
        componentes.extend([nascimento[:4], nascimento[-4:], nascimento[:2], nascimento[-2:]])
    if cidade:
        componentes.append(cidade)
    if ip:
        ip_plain = ip.replace(".", "")
        componentes.append(ip_plain)
    if favoritos:
        componentes.extend(favoritos)

    variacoes = gerar_variacoes(componentes)

    # Combinações entre dois componentes
    combinacoes_duplas = set()
    for a, b in product(componentes, repeat=2):
        if a != b:
            combinacoes_duplas.update(gerar_variacoes([a + b]))

    wordlist = variacoes.union(combinacoes_duplas)

    return list(wordlist)[:50000]  # Limite de 50k senhas

# Função para salvar a wordlist em um arquivo
def salvar_wordlist(wordlist, nome_arquivo):
    with open(nome_arquivo, "w") as f:
        for senha in wordlist:
            f.write(senha + "\n")
    print(f"Wordlist salva em {nome_arquivo}")

# Função principal que gerencia os argumentos e chama as funções
def main():
    green ="\033[1;32m"
    red="\033[1;31m"
    reset="\033[0;0m"
    print(f"""{green}
     ____   _    ____ ______DemonHat _____  ____  ____  
    |  _ 0 / 1  / ___/ ___1 7      / / _ \|  _ 3|  _ 7 
    | |_) / _ 1 1___ 7___ 11 7 8\ / / | | | |_) | | | |
    |  __/ ___ 1 ___) |__) |1 8  / /| |_| |  _ <| |_| |
    |_| /_/   7_1____/____/  1_/1_/  \___@|_| 8_8____/ 
    @DemonHat                        ================={reset} {red}

    Seja bem vindo ao gerador de senhas que gera uma wordlist_personalizada tendo
    tendo em conta os argumentos passados
    NB: pode ignorar as opcoes IP e favoridos datas de nascimento
    Caso nao tenha acesso {reset}
    """)
    nome = input("Nome: ").strip()
    sobrenome = input("Sobrenome: ").strip()
    nascimento = input("nascimento(dd/mm/aaaa): ").strip()
    cidade = input("Pais ou cidade: ").strip()
    ip = input("IP: ").strip()
    favoritos_input = input("Gostos do alvo: ").strip()

    favoritos = favoritos_input.split(",") if favoritos_input else []

    # Gerar a wordlist
    wordlist = gerar_wordlist(nome, sobrenome, nascimento, cidade, ip, favoritos)

    # Salvar a wordlist
    salvar_wordlist(wordlist, "wordlist_personalizada.txt")

if __name__ == "__main__":
    main()
