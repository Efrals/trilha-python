saldo = 300
saque = 100
limite = 1000
conta = False

print(saldo > saque)

print(saldo >= saque)

print(saldo < saque)

print(saldo <= saque)

print(saldo != saque)

print(saldo == saque)

print("----------")

#verdade somente se as comparações forem verdade
print(saldo >= saque and saque <= limite)

#verdade somente se uma das comparações for verdade
print(saldo >= saque or saque <= limite)

print((saldo >= saque and saque <= limite) and (conta and saldo >= saque))

print("----------")

#negação
print(saldo == saque)
print(not saldo == saque)
print("sim")
print(not "sim")
print("")
print(not "")
print(saldo)
print(not saldo)