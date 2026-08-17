# ⭐ Faça um código que leia dois números inteiros, efetue a adição e caso 
# o resultado seja maior ou igual a 10 imprima "Soma maior ou igual a 10"

numero1=int(input("Digite um número:"))
numero2=int(input("Digite outro número:"))
adicao=numero1 + numero2
if adicao >= 10:
    print("Soma maior ou igual a 10.")
else:
    print("Soma menor que 10.")