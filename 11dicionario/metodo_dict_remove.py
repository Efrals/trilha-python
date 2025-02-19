contato = {
    "efraim1@gmail.com" : {"nome" : "Efraim1", "idade" : 31},
    "efraim2@gmail.com" : {"nome" : "Efraim2", "idade" : 32},
    "efraim3@gmail.com" : {"nome" : "Efraim3", "idade" : 33}
}

#remove objetos do dicionario
print(contato["efraim1@gmail.com"])
del contato["efraim1@gmail.com"]["idade"]
print(contato["efraim1@gmail.com"])

#remove chaves do dicionario
#del contato["efraim1@gmail.com"]
#print(contato["efraim1@gmail.com"])