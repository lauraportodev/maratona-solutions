# ⭐⭐ Faça um código que leia valores até 
# que seja digitado 0. Imprima o maior valor digitado

valor=float(input("Digite um valor:"))
maior = valor
menor = valor

while valor !=0:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    valor=float(input("Digite um valor:"))
print(f"Maior:{maior},Menor:{menor}")
