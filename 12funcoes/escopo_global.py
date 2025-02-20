salario = 1000

def salario_bonus(bonus):
    #informa que salario é global para incluir a informação da variável
    global salario
    #mesmo que salario = salario + bonus
    salario += bonus
    return salario

salario_final = salario_bonus(1000)

print(salario_final)