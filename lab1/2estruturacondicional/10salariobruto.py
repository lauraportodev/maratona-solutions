# ⭐⭐⭐ Faça um programa para ler o salário bruto e imprima o valor devido do 
# imposto. Salário Bruto * Alíquota - Valor a deduzir
# Faixa	Alíquota	Valor a Deduzir
# Até 1903,98	Isento	0
# De 1903,99 até 2826,65	7%	R$ 142,80
# De 2826,66 até 3751,05	15%	R$ 354,80
# De 3751,06 até 4664,68	22.5%	R$ 636,13
# Acima de 4664,68	27,5%	R$ 869,36

salario = float(input("Digite seu salário: "))
desconto=0
salario_liquido = salario - desconto
if salario <= 1903.98:
    desconto = salario 
    print(f"O seu salário líquido é {salario_liquido:.2f}")
elif salario >= 1903.99 and salario <= 2826.65:
    desconto = (salario *(7/100)) - 142.80
    print(f"O seu salário líquido é {salario_liquido:.2f}")
elif salario >= 2826.66 and salario <= 3751.05:
    desconto = (salario * (15/100)) - 354.80
    print(f"O seu salário líquido é {salario_liquido:.2f}")
elif salario >= 3751.06 and salario <= 4664.68:
    desconto = (salario *(22.5/100)) - 636.13
    print(f"O seu salário líquido é {salario_liquido:.2f}")
elif salario > 4664.68:
    desconto = (salario *(27.5/100))- 636.13
print(f"O seu salário líquido é {salario_liquido:.2f}")     