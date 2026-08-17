# ⭐⭐ Faça um programa que faça um cronometro imprimindo minutos e segundos. Dica: procure pela função sleep da biblioteca os

import time

print("Cronometro")

# Faz uma animação com três pontos
for i in range(10):
    time.sleep(1)   # pausa de 1 segundo
    print(".", end="")

print("\nPronto!")

