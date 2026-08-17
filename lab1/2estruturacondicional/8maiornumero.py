# ⭐⭐ Faça um programa que leia três números e imprima o maior deles.

numero1=int(input("Digite um número:"))
numero2=int(input("Digite outro número:"))
numero3=int(input("Digite o último número:"))

if numero1 > numero2 and numero1 > numero3:
    print(f"O número {numero1} é o maior número.")
elif numero2 > numero1 and numero2 > numero3:
    print (f"O número {numero2} é o maior número.")
elif numero3 > numero1 and numero3 > numero2:
    print (f"O número {numero3} é o maior número.")