# ⭐⭐ Faça um código que pergunte a altura e peso do usuário e imprima o IMC.

altura=float(input("Digite seu altura:"))
peso=float(input("Digite seu peso:"))
imc=peso/(altura**2)
print(f"Seu IMC é:{imc:.2f}.")