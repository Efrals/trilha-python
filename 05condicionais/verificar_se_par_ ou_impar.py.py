# Solicita ao usuário um número inteiro
numero = float(input("Digite qualquer valor inteiro: \n"))

# TODO: Verifique se o número é par ou ímpar e imprima o resultado:

modulo = numero % 2

if modulo == 0:
    print ("Número par")
else:
    print("Número ímpar")