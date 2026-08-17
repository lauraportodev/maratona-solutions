# ⭐⭐⭐ Faça um código que imprima todos os números primos de 2 até 100

for n in range(2, 101):
    primo = True
    for d in range(2, n):
        if n % d == 0:    # % = resto da divisão
            primo = False
            break         # para o for interno
    if primo:
        print(n)