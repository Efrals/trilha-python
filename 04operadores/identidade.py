nome = "Efraim"
nome_completo = "Efraim Rocha"

credito, limite = 500, 500

#para saber se ocupam a mesma região de memória
print(nome is nome_completo)

#para saber se NÃO ocupam a mesma região de memória
print(nome is not nome_completo)

#para saber se ocupam a mesma região de memória
print(credito is limite)

#CONCLUSÃO: OCUPARÃO A MESMA REGIÃO DE MEMÓRIA DESDE QUE OS VALORES SEJAM OS MESMOS