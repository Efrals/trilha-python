#declarando o dicionário
dicionario = {"nome" : "Efraim", "idade" : 31}

#declarando dicionário através do método explícito
dicionario = dict(nome="Efraim", idade=30)

#adicionando nova chave no dicionario
dicionario["altura"] = 1.7

#extraindo dados do dicionario
print(dicionario["nome"])
print(dicionario["idade"])
print(dicionario["altura"])

#dicionario aninhado
contatos = {
    "efraim@gmail.com" : {"nome" : "Efraim", "telefone" : "1234-1234", "rede_social" : {"insta" : "@efrals"}}
}

#extraindo dados do dicionario
telefone = contatos["efraim@gmail.com"]
print(telefone)

#extraindo dados do dicionario aninhado
telefone = contatos["efraim@gmail.com"]["telefone"]
print(telefone)

#extraindo dados do dicionario aninhado no 3º nível
telefone = contatos["efraim@gmail.com"]["rede_social"]["insta"]
print(telefone)

print()

#percorrer dicionário
for chave, valor in dicionario.items():
    print(chave, valor)