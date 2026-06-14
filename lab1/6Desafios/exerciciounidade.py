#Faça um código em que o usuário indique quanto de cada produto e imprima: quantos itens e o preço dos itens.

produtos = ["Mouse","Teclado","Monitor"]
precos = [29.99, 59.99 , 456.00]
quantidades =[]

for i in len(produtos):
    qtd = int(input(f"Digite a quantidade de {produtos[i]}"))
    quantidades.append(qtd)

print("----------------Orçamento---------------")
for i in len (produtos):
    print(f"")