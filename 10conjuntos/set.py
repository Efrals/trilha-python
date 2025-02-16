#set elimina conteúdos com mesmo valor de uma variável
#NÃO É exibido na mesma ordem que foi escrito
#NÃO CONFIA NA ORDEM EXIBIDA

numeros = set([10, 12, 15, 20, 12, 12, 10, 9, 20, 5])
print(numeros)

#declarando explicitamente e entre parênteses para 1 item
forma = set("paralelepípedo")
print(forma)

#para 1 item não funciona bem com chaves
forma = {"paralelepípedo"}
print(forma)

#o mesmo declarando implicitamente, através de chaves
#entre chaves para mais de 1 item
bolsa = {"carteira", "batom", "moeda", "Dinheiro", "batom", "dinheiro", "espelho", "moeda", "moeda", "batom", "moeda", "Dinheiro", "batom", "dinheiro"}
print(bolsa)

#para acessar os valores de set, tem de tranformar em lista
bolsa = list(bolsa)
print(bolsa[1])

#pode-se percorrer um set através de um for
for numero in numeros:
    print(numero)

for indice, itens_da_bolsa in enumerate(bolsa):
    print(f"{indice} : {itens_da_bolsa}")

