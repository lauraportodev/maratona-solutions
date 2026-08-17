# ⭐⭐ Leia duas notas de um aluno, informe a sua média. Seu programa deve forçar 
# ao usuário a digitar notas na faixa de 0 a 10, informando
# "Valor inválido" no caso de nota inválida.

nota1=float(input("Digite sua primeira nota:"))
nota2=float(input("Digite sua segunda nota:"))
while (nota1 < 0 or nota1 >10) or (nota2 < 0 or nota2 > 10):
    print("Valores inválidos.")
    nota1=float(input("Digite sua primeira nota:"))
    nota2=float(input("Digite sua segunda nota:"))
media= (nota1+nota2) /2
print(f"Sua média é {media:.2}")