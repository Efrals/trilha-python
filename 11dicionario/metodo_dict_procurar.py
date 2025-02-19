contato = dict(nome="Efraim", idade=30)

#para adicionar novas chaves sem conteúdo
print(contato)
#procura a chave no dicionário
procurar = contato["idade"]
print(procurar)

#dessa forma, se não achar, dispara uma excessão 
#contato["dfghdfgh"]