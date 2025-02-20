#parâmetros antes da barra são obrigatoriamente por posição
                                #parâmetros depois da barra podem ser passados nomeados ou por posição
                                              #parâmetros depois do esterísco são somente por nome
def criar_carro(marca, modelo, /, placa, ano, *, combustivel, cor):
    print("Honda", "Civic", "ads-5236", ano = 2000, combustivel = "gasolina", cor = "preto")

                #parâmetros depois do esterísco são somente por nome
def criar_carro(*, combustivel, cor):
    print(combustivel = "gasolina", cor = "preto")

#parâmetros antes da barra são obrigatoriamente por posição
                                  #parâmetros depois do esterísco são somente por nome
def criar_carro(marca, modelo, /, *, combustivel, cor):
    print("Honda", "Civic", combustivel = "gasolina", cor = "preto")