conjunto_1 = {1, 2, 3}
conjunto_2 = {4, 5, 6}
conjunto_3 = {1, 7}


#retorna se primeiro conjunto está separado do segundo 
nao_esta_junto = (conjunto_1.isdisjoint(conjunto_2))
print(nao_esta_junto)

nao_esta_junto = (conjunto_1.isdisjoint(conjunto_3))
print(nao_esta_junto)