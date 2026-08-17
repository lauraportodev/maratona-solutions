# ⭐⭐ Faça um código que leia a altura e peso do usuário, 
# calcule IMC e imprima a facha do peso. (Até 18.5 abaixo do peso, 
# de 18.5 até 25 peso normal, de 25 até até 30 acima do peso e acima de 30 obeso)

nome=input("Qual seu nome?")
altura=float(input("Qual sua altura?"))
peso=float(input("Qual seu peso?"))
imc= peso/(altura**2)
if imc <= 18.5:
    print (f"{nome},você está abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print (f"{nome},você está com peso normal.")
elif imc >= 25 and imc <=30 :
    print (f"{nome},você está acima do peso.")
else:
    print (f"{nome}, você está obeso.")