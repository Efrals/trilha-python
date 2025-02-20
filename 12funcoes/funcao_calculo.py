def calcular_soma(numeros):
    return sum(numeros)

print(calcular_soma([1,2,3,4,5]))


def antecessor_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1

    return antecessor, sucessor

#retorna em uma tupla
print(antecessor_sucessor(20))

print()

def somar (a, b):
    return a + b

def subtrair(a, b):
     return a - b

def exibir_resultado (a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(15, 10, somar)
exibir_resultado(15, 10, subtrair)

op = subtrair
print(op(5,25))
op = somar
print(op(5,25))