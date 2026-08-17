# ⭐⭐ O programa deve ler números do usuário até ele digitar 0. 
# Ao final, mostre qual foi o maior número digitado.

numero = int(input("Digite um número:"))
maior = numero
while numero != 0:
    if numero > maior:
        maior = numero
    numero=int(input("Digit um número:"))
print (f"O maior número digitado foi o  {maior}")