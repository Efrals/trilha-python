contato = dict(nome="Efraim", idade=30)

print(contato)
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