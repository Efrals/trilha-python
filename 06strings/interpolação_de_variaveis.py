nome = "Efraim"
idade = 30
altura = 1.65
linguagem = "Python"

dados = {"nome": "Efraim", "idade": 30, "altura": 1.65, "linguagem": "Python"}

PI = 3.14159

#Velho método, que apesar de ser compatível com Python 3, não é muito usada
# %s para string   %d para inteiro   %f para ponto flutuante
print("Olá, sou %s, minha idade é %d, minha altura é %f, estou adorando a linguagem %s." % (nome, idade, altura, linguagem))

#O método format é um pouco melhor, mas tem de passar todas variáveis em ordem
print("Olá, sou {}, minha idade é {}, minha altura é {}, estou adorando a linguagem {}.".format (nome, idade, altura, linguagem))

#Método format passando dados através de um array
print("Olá, sou {nome}, minha idade é {idade}, minha altura é {altura}, estou adorando a linguagem {linguagem}.".format(**dados))

#O método f-string é melhor, tem de reescrever a variável várias vezes mas deixa o código bem mais legível
print(f"Olá, sou {nome}, minha idade é {idade}, minha altura é {altura}, estou adorando a linguagem {linguagem}.")

#Limitar número de casas decimais
print(f"Valor de PI: {PI:.2f}")