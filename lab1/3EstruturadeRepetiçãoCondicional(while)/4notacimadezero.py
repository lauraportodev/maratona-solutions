# ⭐⭐ Faça um código que leia 
# valores até que seja digitado 0. Imprima quantos 
# itens foram lidos e qual a média dos valores.

soma = 0
quantidade = 0
valor = float(input("Digite um valor:"))
while valor !=0:
    soma += valor
    quantidade += 1
    valor = float(input("Digite um valor:"))

if quantidade >0:
    media = soma/ quantidade
    print (f"itens lidos: {quantidade}, média: {media:.2f}")
else:
    print("Nenhum valor digitado.")
