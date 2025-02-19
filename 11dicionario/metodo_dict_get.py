contato = dict(nome="Efraim", idade=30)

print(contato)
#pode-se declarar explicitamente para fazer a procura sem gerar erro
procurar = contato.get("nome")
print(procurar)

#se não encontrar a chave retornará none
procurar = contato.get("nenhum")
print(procurar)

#se não encontrar a chave retornará alguma mensagem especificada
procurar = contato.get("nenhum", {"Chave não encontrada"})
print(procurar)