#Inteiro para float
valor_inteiro = 15
inteiro_em_float = float(valor_inteiro)
print(inteiro_em_float)

valor = 15 / 2
print(valor)

print("--------------")

#Converter por divisão
valor = 15
print(valor)

print(valor / 2)
#Mantém somante o valor inteiro
print(valor // 2)

print("--------------")

#Número para string
valor1 = 10.5
valor2 = 20
print(str(valor1))
print(type (valor1))
#Direto e concatenado
print(f"Valor 1 = {valor1} e Valor 2 = {valor2}")
print(type (valor1))

print("--------------")

#String para número
texto1 = "26.45"
texto2 = "45"

print(float(texto1))
#Não pode se converter uma string decimal em int
print(int(texto2))

#Não pode converter letras para int ou float

print("--------------")

#Mostra o tipo reconhecido em cada variável
print(type (valor))
print(type (texto1))
print(type (valor1))