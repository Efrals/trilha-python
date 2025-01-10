nome = "     efRaiM 5  r   "

print("String passada")
print(nome)

print()
print("Caixa alta e baixa")
print(nome.upper())
print(nome.lower())
print(nome.title())
print(nome.swapcase())

print()
print("Eliminar espaços em branco")
#elimina espaços de ambos os lados
print(nome.strip() + ".")
#elimina espaços da esquerda
print(nome.lstrip() + ".")
#elimina espaços da direita
print(nome.rstrip() + ".")

print()
print("Junção e centralização")
print(nome.center(30, "*"))
print(nome.center(30, " "))
print("_".join(nome))

print()
print("Tranformar string em array")
print(nome.split())