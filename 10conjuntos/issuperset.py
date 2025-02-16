conjunto_1 = {1, 2, 3}
conjunto_2 = {1, 2, 3, 4, 5, 6}

#retorna se primeiro conjunto contém todos elementos do segundo conjunto 
superconjunto = (conjunto_1.issuperset(conjunto_2))
print(superconjunto)

superconjunto = (conjunto_2.issuperset(conjunto_1))
print(superconjunto)