# ⭐⭐⭐ Leia várias palavras e as armazene em uma lista. 
# Imprima qual palavra aparece mais vezes e quantas vezes ela apareceu.

palavras=[]
while True:
    p=input("Digite uma palavra:")
    if p == '0':
        break
    palavras.append(p)
print(f"Mais vezes:", max[palavras], ",apareceu {quantidade}" )
