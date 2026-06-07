# ⭐⭐ Faça um código que leia idades até que seja digitado 0. 
# Calcule a média de idades de quem possui mais que 21 anos e imprima.

idade =int(input("Digite uma idade:"))
quantidade=0
soma=0
while idade !=0:
    if idade >= 21:
        quantidade += 1
        soma += idade
    idade=int(input("Digite uma idade:"))
    if quantidade > 0:
        media = soma / quantidade
print(f"A média das idades digitadas maiores ou iguais a 21, foi de:{media:.2f}")







