#Campeonato de Batalha Mágica Você está desenvolvendo a lógica de um mini-jogo
#  onde os jogadores participam de um campeonato de batalha mágica. Cada jogador 
# tem um nível de poder mágico, que é um número inteiro entre 1 e 100.

#Com base nesse valor, o jogo deve classificar o jogador em uma das seguintes categorias:
#1 a 20: 🧙‍♂️ Aprendiz
#21 a 40: 🔮 Feiticeiro
#41 a 60: 🐉 Mago das Chamas
#61 a 80: ⚡ Feiticeiro Supremo
#81 a 100: 🌌 Arqui-Mago
#Escreva um programa que receba o poder mágico de um jogador e exiba sua classificação.
#[Bônus] Use a biblioteca random para gerar um número aleatório

#https://colab.research.google.com/drive/1ZhW3ZKsgo0-3SyQoybmgvUnQU10j4fj_?usp=
# sharing#scrollTo=k_3qsw-KjaxM

#Mini-jogo para descobrir seu nível e classe mágica
pip install emoji
import random
import emoji
#ENTRADA - Mensagem inicial:
print ("Olá,jogador! Vamos descobrir seu nível de magia e classe mágica!")
# Número inteiro aleatório:
nivelmagico = randon.randint (1,100)
#PROCESSAMENTO:
if nivelmagico 1 >= 20:  Aprendiz
print (f"Seu nível de magia é {nivelmagico}, sua classe mágica é {classemagica}!"")
    elif nivelmagico 21 >= 40:  Feiticeiro
    print (f"Seu nível de magia é {nivelmagico}, sua classe mágica é {classemagica}!"")
    elif nivelmagico 41 >= 60:  Mago das Chamas
    print (f"Seu nível de magia é {nivelmagico}, sua classe mágica é {classemagica}!"")
    elif nivelmagico 61 >= 80:  Feiticeiro Supremo
    print (f"Seu nível de magia é {nivelmagico}, sua classe mágica é {classemagica}!"")
    elif nivelmagico 81 >= 100::  Arqui-Mago