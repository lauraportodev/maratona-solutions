# ⭐⭐ Faça um programa que leia dois números inteiros e imprima a média ponderada dos dois, considere os pesos 3 e 4

numero1=int(input("Digite um número:"))
numero2=int(input("Digite outro número:"))
media_ponderada= (numero1*3 + numero2*4) / (3 + 4)
print(f"A média ponderada dos números digitados é:{media_ponderada:.2f}.")