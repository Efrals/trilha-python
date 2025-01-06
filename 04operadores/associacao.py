#Verifica se um objeto está presente em uma sequência

texto = "O artigo de opinião é um tipo de texto dissertativo-argumentativo onde o autor apresenta seu ponto de vista sobre determinado tema e, por isso, recebe esse nome. A argumentação é o principal recurso retórico utilizado nos textos de opinião, que tem como característica informar e persuadir o leitor sobre um assunto."
cor = ["azul", "laranja", "verde"]
quantidade_tipo1 = [100, 200]
quantidade_tipo2 = 500
quantidade, preco = [10, 20]

print("Assunto" in texto)
print("assunto" in texto)
print("ssunto" in texto)
print("assu" in texto)
#Concluí-se que retorna TRUE quando procura somente uma parte da palavra e respeita caixa baixa e alta

print("--------------")

print("azu" in cor)
print("Azul" in cor)
print("azul" in cor)
#Concluí-se que em vetor, procura a palavra correta

print("--------------")

print(200 in quantidade_tipo1)
#procura o valor em vetor onde armazena uma variável
print(100 in quantidade_tipo2)
#NÃO procura o valor sem vetor
print(20 in preco)
#NÃO procura o valor em vetor onde armazena mais de uma variável