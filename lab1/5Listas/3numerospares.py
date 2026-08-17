# ⭐⭐ Leia 10 números e apenas coloque na lista os números que 
# forem pares. Imprima a lista.

numeros = []
for _ in range(10):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        numeros.append(n)
print(numeros)