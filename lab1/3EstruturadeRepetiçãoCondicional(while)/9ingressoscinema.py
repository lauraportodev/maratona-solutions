# ⭐⭐⭐ Vamos fazer um sistema de ingressos de Cinema. 
# Pergunte a idade até que a pessoa digite 0 para sair. 
# Se a pessoa tiver menos que 10 anos ou mais que 60 informe 
# "Meia Entrada" se não, informe "Inteira". Ao terminar imprima: 
# "Total de x ingressos vendidos, sendo y meia entrada"

idade=int(input("Digite uma idade:"))
quantidade=0
meia_entrada=0
while idade != 0:
    quantidade += 1
    if idade < 10 or idade > 60:
        meia_entrada += 1
        print("Você possui meia-entrada.")
    else:
        print("Seu ingresso é inteira.")
    idade=int(input("Digite uma idade:"))
print(f"Total de ingressos vendidos:{quantidade},sendo ingressos de meia entrada : {meia_entrada}")