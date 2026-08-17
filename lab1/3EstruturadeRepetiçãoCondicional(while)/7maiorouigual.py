# ⭐⭐ Faça um código que leia idades 
# até que seja digitado 0. Imprima quantas idades 
# maiores ou iguais a 18 foram digitadas

idade=int(input("Digite uma idade:"))
maior_idade = 0
while idade !=0:
    maior_idade += idade >= 18
    idade=int(input("Digite uma idade:"))
print (f"O número de idades iguais ou maiores que 18 foi de: {maior_idade}")
    