class Carro:     #self é uma convenção que faz referência explícita para o objeto (pode ser outro nome também)
    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

              #precisa de ao menos 1 argumento posicional. O self aponta para ele mesmo
    def buzinar(self):
        print("Biiii!!")

    def parar(self):
        print("Parando...")

    def correr(self):
        print("Correndo...")

    #para permitir o acesso dos atributos através do print()
    #tem de atualizar a lista manualmente
    #def __str__(self):
    #    return f"Carro: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    #para permitir o acesso dos atributos através do print()
    #atualiza a toda lista dinamicamente
                                            #join para concatenar todos items com ", "
    def __str__ (self):                     #list comprehension para concatenar todas chaves e valores através de dicionário e items para estruturar os atributos
        return f"{self.__class__.__name__} -:- {", ".join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

carro1 = Carro("Azul", "C1", 2000, 50000)

carro1.buzinar()
carro1.correr()
carro1.parar()

print()

        #reutiliza os métodos da classe carro
carro2 = Carro("Roxo", "C2", 1999, 25000)

carro2.buzinar()
carro2.correr()
carro2.parar()

print()

#para acessar os atributos
print(carro1.cor)
print(carro2.cor)

print()

#para acessar os atributos através do __str__
print(carro1)
print(carro2)