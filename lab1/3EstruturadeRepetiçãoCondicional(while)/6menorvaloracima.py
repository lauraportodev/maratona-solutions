# ⭐⭐ Faça um código que leia valores 
# até que seja digitado 0. Imprima o menor valor digitado

valor=float(input("Digite um valor:"))
menor = valor

while valor != 0:
    if valor < menor:
        menor = valor
    valor=float(input("Digite um valor."))
print("O menor valor digitado foi de:", menor)