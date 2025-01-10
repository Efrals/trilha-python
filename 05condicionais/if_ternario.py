saldo = 200
saque = int(input("Informe o valor do saque: "))

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} em realizar o saque")