     #Irá executar infinitamente
while True:
    numero = int(input("Informe um número: \n[50] Para sair \n"))

    if numero == 50:
        #parará a execução com o número informado
        break

    if numero == 10:
        #pulará a execução do número informado
        continue

    print(numero)