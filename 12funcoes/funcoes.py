def exibir_mensagem_1():
    print("Olá")

#se não passar o valor dá erro
def exibir_mensagem_2(nome):
    print(f"Olá {nome}!")

#se não passar o valor mostrará Anônimo
#se passar o valor, mostrará o valor
def exibir_mensagem_3(nome = "Anônimo"):
    print(f"Olá {nome}!")

exibir_mensagem_1()
print()
exibir_mensagem_2(nome = "Efraim")
print()
exibir_mensagem_3()
exibir_mensagem_3(nome = "Efraim")