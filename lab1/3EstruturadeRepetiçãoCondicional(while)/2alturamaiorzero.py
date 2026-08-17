# ⭐ Faça um código que leia uma altura
# mas só aceite valores maiores que 0 e menores que 3. Imprima "Valor Inválido" ou o valor

altura=float(input("Digite sua altura:"))
while altura < 0 or altura >3:
    print("Valor inválido.")
    altura=float(input("Digite sua altura:"))
print(f"Sua altura é {altura}")
