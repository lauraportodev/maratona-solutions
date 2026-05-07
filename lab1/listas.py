'''Faça um programa que leia cinco notas, armazene em uma 
lista e depois calcule e imprima: soma das notas, média das notas e 
quantidade de elementos na lista'''


# Exercício 1 
notas = []
for i in range (1,6):
    notas.append(float(input(f"Qual a sua nota da {i}?")))
soma_nota = sum(notas) 
quantidade_lista = len(notas) 
media_notas = soma_nota / quantidade_lista

print(f'''NOTAS
Soma das notas:{soma_nota}
Quantidade na lista: {quantidade_lista}
Média Notas {media_notas}''')

#Exercício 2 
while True:
    lista =[]
    lista_maiuscula = [letra.upper() for letra in lista]
    palavra = (input("Digite uma palavra aleatória:"))
    lista.append(palavra)
    if palavra == '0':
        break

    '''Aula sobre listas'''
#Monte uma lista com os elementos 2**n do 0 até o 10

lista = []
for i in range(11):
    lista.append(2**i)

print(lista)

# Ler notas dos alunos
notas = []
for i in range(1,4):
    nota = float(input(f"Qual a nota c {i}?"))