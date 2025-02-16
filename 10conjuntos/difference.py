conjunto_1 = {4, 5, 1, 2, 3, 10}
conjunto_2 = {5, 6, 1, 2, 11}

#retorna somente o que tem no primeiro conjunto
diferenca = (conjunto_1.difference(conjunto_2))
print(diferenca)

#retorna todos itens diferentes em todos conjuntos
diferenca = (conjunto_1.symmetric_difference(conjunto_2))
print(diferenca)


conjunto_1 = {"a", "b", "c", "d", "ab"}
conjunto_2 = {"e", "f", "b", "d", "dd"}

#retorna somente o que tem no primeiro conjunto
diferenca = (conjunto_1.difference(conjunto_2))
print(diferenca)