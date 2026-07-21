# ⭐⭐ Leia palavras até que o usuário digite '0', salve em uma lista, 
# imprima a lista colocando todas as palavras em letras maíuscula


palavras =[]
while True:
    s =input("Digite uma palavra ou 0 para sair:").strip()
    if s == '0':
        break
    palavras.append(s)
print([p.upper() for p in palavras])





