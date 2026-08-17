# ⭐⭐ Faça um programa que leia cinco notas, armazene em uma lista e depois calcule e 
# imprima: soma das notas, média das notas e quantidade de elementos na lista

notas=[]
for i in range(1,6):
    notas.append(float(input(f"Digite a {i}º nota:")))
print("Soma:", sum(notas))
print("Média:", sum(notas)/ len(notas))
print("Quantidade:", len(notas))


nomes = []
while True:
    nome =input("Digite um nome:")
    if nome == "fim":
        break
    nomes.append(nome)
print ("QUANTIDADE:", len (nomes))
print (nomes)
