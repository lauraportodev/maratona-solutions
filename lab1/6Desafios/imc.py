
#só aceitar valores dentro de um valor específico

altura = float(input("Qual a sua altura? "))

while (altura < 1.50 or altura > 2.0):
    print ("Valores inválidos !")
    altura = float(input("Qual a sua altura? "))
    
peso = float(input("Qual o seu peso? "))

while (peso < 40 or peso > 200):
    print ("Valores inválidos !")

    peso = float(input("Qual o seu peso? "))
    
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc}")

# Algoritmo IMC em Python

nome = input("Qual seu nome? ")
peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))

IMC = peso / (altura ** 2)

if IMC < 17:
    print(f"{nome}, você está muito abaixo do peso. Seu IMC é: {IMC:.2f}")
elif IMC >= 17 and IMC < 18.5:
    print(f"{nome}, você está abaixo do peso. Seu IMC é: {IMC:.2f}")
elif IMC >= 18.5 and IMC < 25:
    print(f"{nome}, parabéns! Você está com peso ideal. Seu IMC é: {IMC:.2f}")
elif IMC >= 25 and IMC < 30:
    print(f"{nome}, você está com sobrepeso. Seu IMC é: {IMC:.2f}")
elif IMC >= 30 and IMC < 35:
    print(f"{nome}, você está com obesidade. Seu IMC é: {IMC:.2f}")
elif IMC >= 35 and IMC < 40:
    print(f"{nome}, você está com obesidade severa. Seu IMC é: {IMC:.2f}")
else:
    print(f"{nome}, você está com obesidade mórbida. Seu IMC é: {IMC:.2f}")



