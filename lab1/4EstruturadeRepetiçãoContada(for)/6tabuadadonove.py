# ⭐⭐ Faça um código que leia um número e imprima a tabuada do número de 1 a 9

n = int(input("Digite um número:"))
print(f"A tabuada do número {n} é :")
for i in range (1,10):
    print(f"{n}x{i} = {n*i}")
