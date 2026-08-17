# ⭐⭐ Faça um programa que leia dois números inteiros e imprima a média ponderada dos dois, pergunte os pesos ao usuário
numero1=int(input("Digite um número:"))
numero2=int(input("Digite outro número:"))
peso1=int(input("Digite um peso:"))
peso2=int(input("Digite outro peso:"))
media_ponderada= (numero1*peso1)+(numero2*peso2)/(peso1+peso2)
print(f"A média ponderada dos números e pesos digitados é :{media_ponderada}.")