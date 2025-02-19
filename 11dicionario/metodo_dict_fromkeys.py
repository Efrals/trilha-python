contato = dict(nome="Efraim", idade=30)

print(contato)
#para adicionar novas chaves sem conteúdo
vazio = contato.fromkeys(["nome", "telefone"], "vazio")
print(vazio)