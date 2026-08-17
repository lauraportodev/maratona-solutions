# ⭐⭐⭐ Vamos fazer um menu de caixa eletrônico, executando em loop até que o usuário peça para sair. Suponha que o saldo inicial seja R$1000. O usuário deverá digitar qual item do menu para prossegir. Imprima: """
# 1 - Ver saldo
# 2 - Sacar dinheiro
# 3 - Depositar dinheiro
# 4 - Sair
# """

# Caso o usuário digite 1 imprima o saldo atual
# Caso o usuário digite 2 pergunte quanto dinheiro ele deseja sacar e remova do saldo (atenção, o usuário não pode sacar mais do que possui!)
# Caso o usuário digite 3 pergunte quanto dinheiro ele deseja depositar e adicione o valor ao saldo
# Caso o usuário digite 4 encerre o programa
# Caso o usuário digite outro valor no menu apresente a mensagem "Opção Inválida" e imprima o menu novamente.
# Tente fazer a primeira vez usando if e a segunda usando match case (python 3.10)

saldo = 1000

opcao = int(input("\n1- Ver saldo\n2- Sacar dinheiro\n3- Depositar dinheiro\n4- Sair\nDigite uma opção: "))

while opcao != 4:
    if opcao == 1:
        print(f"Seu saldo é R$ {saldo:.2f}")
    elif opcao == 2:
        saque = float(input("Qual valor para o saque? "))
        if saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= saque
            print("Saque realizado.")
    elif opcao == 3:
        deposito = float(input("Digite valor para depósito: "))
        saldo += deposito
        print("Depósito realizado.")
    else:
        print("Opção inválida.")

    opcao = int(input("\n1- Ver saldo\n2- Sacar dinheiro\n3- Depositar dinheiro\n4- Sair\nDigite uma opção: "))

print("Até a próxima.")
