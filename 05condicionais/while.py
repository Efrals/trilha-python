opcao = -1

while opcao != 0:
    opcao = int(input("[1] Pagar em Cartão de Crédito \n[2] Pagar em PIX \n[0] Sair \n "))

if opcao == 1:
    print("Pagamento com Cartão de Crédito")
elif opcao == 2:
    print("Pagamento com PIX")
elif opcao > 2:
    print("Digite um número válido (1, 2 ou 0)")