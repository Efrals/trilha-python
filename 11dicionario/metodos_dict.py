contato = dict(nome="Efraim", idade=30)

#cópia de dicionário
copia_contato = contato.copy()
print(copia_contato)

#limpa dados do dicionário
copia_contato.clear()
print(copia_contato)

#para adicionar novas chaves sem conteúdo
vazio = contato.fromkeys(["nome", "telefone"], "vazio")
print(vazio)

print()

#procura a chave no dicionário
procurar = contato["idade"]
print(procurar)

#dessa forma, se não achar, dispara uma excessão 
#contato["dfghdfgh"]

print()

#pode-se declarar explicitamente para fazer a procura sem gerar erro
procurar = contato.get("nome")
print(procurar)

#se não encontrar a chave retornará none
procurar = contato.get("nenhum")
print(procurar)

#se não encontrar a chave retornará alguma mensagem especificada
procurar = contato.get("nenhum", {"Chave não encontrada"})
print(procurar)

print()

#percorrer dicionário com items e for
for chave, valor in contato.items():
    print(chave, valor)

print()

#remove um valor específico do dicionário
pop = contato.pop("nenhum", {"não encontrado"})
print(pop)

#remove valores em sequência
pop = contato.popitem()
print(pop)
pop = contato.popitem()
print(pop)

#após remover todos itens retorna uma excessão
#pop = contato.popitem()
#print(pop)

print()

#adiciona valor somente se não exitir no dicionário
contato.setdefault("idade", 30)
print(contato)

print()

contato = {
    "efraim1@gmail.com" : {"nome" : "Efraim1", "idade" : 31},
    "efraim2@gmail.com" : {"nome" : "Efraim2", "idade" : 32},
    "efraim3@gmail.com" : {"nome" : "Efraim3", "idade" : 33}
}

#atualiza o dicionário de toda a chave se ela já existir
contato.update({"efraim@1gmail.com" : {"nome" : "Efraim"}})
print(contato)
contato.update({"efraim@1gmail.com" : {"nome" : "Efraim", "idade" : "mais novo"}})
print(contato)

print()

#retorna somente as chaves do dicionário
print(contato.keys())

print()

#retorna somente os valores do dicionário
print(contato.values())

print()

#verificar se existe chave em um dicionário
verificacao = "idade" in contato["efraim@1gmail.com"]
print(verificacao)
verificacao = "altura" in contato["efraim@1gmail.com"]
print(verificacao)
verificacao = "nome" in contato["efraim@1gmail.com"]
print(verificacao)

print()

#remove objetos do dicionario
print(contato["efraim1@gmail.com"])
del contato["efraim1@gmail.com"]["idade"]
verificacao = "idade" in contato["efraim@1gmail.com"]
print(contato["efraim1@gmail.com"])

#remove chaves do dicionario
#del contato["efraim1@gmail.com"]
#verificacao = "idade" in contato["efraim@1gmail.com"]
#print(contato["efraim1@gmail.com"])