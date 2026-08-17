# ⭐⭐ Uma pessoa quer juntar dinheiro até atingir R$ 1000. 
# O programa deve pedir valores de depósito (um por vez) e somar ao total. 
# Quando o valor total atingir ou ultrapassar 1000, o programa deve parar 
# e informar: o total acumulado e quantos depósitos foram feitos.

depositos=0
soma= depositos
quantidade=0
depositos=float(input("Digite um valor:"))
while soma != 1000:
    depositos=float(input("Digite um valor:"))
    soma += depositos
    quantidade += 1
print(f"O total de depósito foi de {soma}, foram feitos {quantidade} depósitos.")