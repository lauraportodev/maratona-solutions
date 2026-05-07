# ⭐⭐ Faça um programa que leia três notas e imprima: "Aprovado", se a nota 
# for maior ou igual a sete. "Prova Final", se a nota for menor que 7.

nota1=float(input("Qual sua primeira nota?"))
nota2=float(input("Qual sua segunda nota?"))
nota3=float(input("Qual sua terceira nota?"))

media= (nota1 + nota2 + nota3)/3

if media >= 7:
    print(f"Sua média foi de {media:.2}, você foi aprovado.")
else:
    print(f"Sua média foi de {media:.2}, você está de prova final.")