lista = ["a", "um", "dois", "3", "e", "e", "E"]
print(lista)

#copia a lista para uma nova instância
#lista ainda permanece a mesma
#lista_copiada receberá uma cópia de lista
lista_copiada = lista.copy()

print(lista)
print(lista_copiada)

#alterará o item na determinada posição
lista_copiada[3] = "alterada"
print(lista_copiada)

#Limpa a os valores da lista que foi copiada
lista_copiada.clear()
print(lista_copiada)

#conta quantas vezes determinado item repete na lista
#diferencia maiúculas de minúsculas
contar_repeticoes = lista.count("e")
print(contar_repeticoes)

#incrementa novos valos res na lista (e não substitui valores)
lista.extend(["f", 6, 7, "i", 10])
print(lista)

#pega o primeiro item da lista que corresponde a procura
print(lista.index("f"))

#remove o último elemento da lista
lista.pop()
print(lista)
lista.pop()
print(lista)
lista.pop()
print(lista)
#pode-se especificar a posição qual item da lista a ser removido
lista.pop(4)
print(lista)
#dessa forma, mostra qual item da posição foi removido
print(lista.pop(3))
print(lista)

#remove o primeiro item especificado que será encontrado
lista.remove(6)
print(lista)
lista.remove("e")
print(lista)

#espelha a lista
lista.reverse()
print(lista)


print(lista)
#ordena a lista om ordem alfabética
#não suporte organizar lista mista de números e strings
#organiza maiúsculas primeiro e minúsculas depois (interesante padronizar escrita antes de ordenar)
lista.sort()
print(lista)

#organiza lista de forma alfabética inversa
lista.sort(reverse=True) #T de True sempre em maiúsculo
print(lista)

#organiza por quantidade de caracteres
                        #len de length = comprimento de cada item da lista (que retorna um inteiro de quantos caracteres da item possui)
lista.sort(key=lambda x: len(x))
print(lista)

#organiza por quantidade de caracteres de forma reversa
lista.sort(key=lambda x: len(x), reverse=True)
print(lista)

#mostra quantos itens tem na lista
print(len(lista))

#mostra quantos caracteres tem no item correspondente de determinada posição
print(len(lista[0]))
print(len(lista[1]))