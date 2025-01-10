saldo = 200
alto_saque = 1000
saque = float(input("Informe o valor do saque: "))

if saque >= alto_saque:
    print ("Não é possível sacar valor acima de R$ 1000,00")
elif saldo >= saque:
    print("Saque realizando")
else:
    print("Saldo insuficiente")