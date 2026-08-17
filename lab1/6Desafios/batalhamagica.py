# Campeonato de Batalha Mágica Você está desenvolvendo a lógica de um mini-jogo
#  onde os jogadores participam de um campeonato de batalha mágica. Cada jogador 
# tem um nível de poder mágico, que é um número inteiro entre 1 e 100.

# Com base nesse valor, o jogo deve classificar o jogador em uma das seguintes categorias:
# 1 a 20: 🧙‍♂️ Aprendiz
# 21 a 40: 🔮 Feiticeiro
# 41 a 60: 🐉 Mago das Chamas
# 61 a 80: ⚡ Feiticeiro Supremo
# 81 a 100: 🌌 Arqui-Mago
# Escreva um programa que receba o poder mágico de um jogador e exiba sua classificação.
# [Bônus] Use a biblioteca random para gerar um número aleatório

import random

poder = random.randint(1, 100)

# Estrutura condicional para classificar
nome=input("Qual seu nome?")
if poder >= 1 and poder <= 20:
    classificacao = "🧙‍♂️ Aprendiz"
elif poder <= 40:
    classificacao = "🔮 Feiticeiro"
elif poder <= 60:
    classificacao = "🐉 Mago das Chamas"
elif poder <= 80:
    classificacao = "⚡ Feiticeiro Supremo"
else:
    classificacao = "🌌 Arqui-Mago"

# Saída
print(f"Olá {nome}, seu poder mágico é : {poder} e sua classe é: {classificacao} .")
