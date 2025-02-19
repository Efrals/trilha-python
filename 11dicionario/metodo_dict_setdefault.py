contato = dict(nome="Efraim")

print(contato)
#adiciona valor somente se não exitir no dicionário
contato.setdefault("idade", 30)
print(contato)
contato.setdefault("idade", 25)
print(contato)