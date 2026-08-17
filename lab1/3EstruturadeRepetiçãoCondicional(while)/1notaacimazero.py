# ⭐ Faça um código que leia uma nota mas 
# só aceite valores acima ou igual a 0 e menores ou 
# iguais a 10. Imprima "Valor Inválido" ou o valor.
nota=float(input("Digite sua nota:"))
while nota < 0 or nota > 10:
    print("Valor inválido.")
    nota=float(input("Digite sua nota:"))
print (f"Sua nota é: {nota}")