# ⭐⭐ Faça um código que pergunte a nota do usuário 5 vezes e depois imprima a soma das notas e a média das notas

soma = 0
for i in range (5):
    nota= float(input(f"Digite sua nota da {i+1}:"))
    soma += nota
media = soma /5
print(f"A soma das notas foi {soma} e a média foi {media:.2f}.")