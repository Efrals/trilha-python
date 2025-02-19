contato = {
    "efraim1@gmail.com" : {"nome" : "Efraim1", "idade" : 31},
    "efraim2@gmail.com" : {"nome" : "Efraim2", "idade" : 32},
    "efraim3@gmail.com" : {"nome" : "Efraim3", "idade" : 33}
}

#atualiza o dicionário de toda a chave se ela já existir

contato.update({"efraim@1gmail.com" : {"nome" : "Efraim", "idade" : "mais novo"}})
print(contato)

print()

#verificar se existe chave em um dicionário
verificacao = "idade" in contato["efraim@1gmail.com"]
print(verificacao)
verificacao = "altura" in contato["efraim@1gmail.com"]
print(verificacao)
verificacao = "nome" in contato["efraim@1gmail.com"]
print(verificacao)
