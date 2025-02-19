contato = {
    "efraim1@gmail.com" : {"nome" : "Efraim1", "idade" : 31},
}

#atualiza o dicionário de toda a chave se ela já existir
contato.update({"efraim@1gmail.com" : {"nome" : "Efraim"}})
print(contato)

print()

contato.update({"efraim@1gmail.com" : {"nome" : "Efraim", "idade" : "mais novo"}})
print(contato)

print()

contato.update({"efraim@1gmail.com" : {"nome" : "Luiz"}})
print(contato)