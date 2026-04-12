
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


