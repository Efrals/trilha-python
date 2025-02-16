#
#Tuplas são estrutura imutáveis
#
#Tuplas usam parênteses         #Boa prática finalizar com vírgula no último item
moveis = ("cama", "mesa", "sofa",)

#Declara explicitamente que se trata de uma tupla
objeto = tuple("xícara")
numeros = tuple([1, 2, 3])

#Python pode se confundir ao declarar somente 1 item na tupla sem especificar explicitamente que se trata de uma tupla
                                   #Boa prática finalizar com vírgula no último item
palavra = ("otorrinolaringologista",)

matriz = (
    (0, 1, 2, 3),
    ("a", "b", "c"),
    ("0a", "1b", "2c"),
)

print(moveis[-1])
print(objeto[1])
print(numeros[2])
print(palavra[0])


#Sempre retornará exceção ao tentar fazer qualquer alteração nas tuplas
#É permitido fazer alterações antes das variáveis se tornarem tuplas
#É permitido somente fazer consultas em tuplas
matriz.clear()
print(matriz)

palavra.extend(["outra"])
print(palavra)

moveis.pop()
print(moveis)

objeto.remove("xícara")
print(objeto)