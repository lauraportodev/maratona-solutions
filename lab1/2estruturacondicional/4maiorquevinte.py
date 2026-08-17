# ⭐⭐ Faça um código que leia dois números inteiros, efetue a adição 
# e caso o resultado seja maior que 20 imprima o valor somado a 8

numero1= int(input("Digite um número:"))
numero2= int(input("Digite outro número:"))
adicao= numero1 + numero2
if adicao > 20:
    adicao = numero1 + numero2 + 8 
    print(f"O valor é:{adicao}")
else:
    print("Os valores informados não atendem aos requisitos.")
