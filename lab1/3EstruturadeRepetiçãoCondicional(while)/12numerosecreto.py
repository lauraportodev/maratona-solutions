# ⭐⭐ O programa define um número secreto entre 1 e 10 (fixo mesmo, tipo 7).
# O usuário tem no máximo 3 tentativas para acertar. A cada tentativa: informe 
# se o chute está certo ou errado. No final: informe se o jogador venceu ou perdeu.

import random

secreto = random.randint(1, 10)
tentativa = 0

while tentativa < 3:
    palpite = int(input("Digite um número: "))
    tentativa += 1

    if palpite == secreto:
        print("Você acertou!")
        break
else:
    print(f"Suas chances acabaram. O número secreto era {secreto}.")

