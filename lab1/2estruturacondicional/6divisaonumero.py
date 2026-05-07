# ⭐⭐ Faça um código que leia um número e informar se ele é divisível 
# por 10, por 7, por 5, por 3, por 2 ou se não é divisível por nenhum destes.

numero=int(input("Digite um número:"))
if numero % 10 == 0:
    print(f"O número {numero} é múltiplo de 10.")
elif numero % 7 == 0:
    print(f"O número {numero} é múltiplo de 7.")
elif numero % 5 == 0:
    print (f"O número {numero} é múltiplo de 5.")
elif numero % 3 == 0:
    print (f"O número {numero} é múltiplo de 3.")
elif numero % 2 == 0:
    print(f"O número {numero} é múltiplo de 2.")
else:
    print(f"O número {numero}, não é dívisivel por 10,7,5,3 ou 2.")