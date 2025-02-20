def carro(marca, modelo, ano, placa):
    #salva no BD
    print(f"Inserido! {marca} / {modelo} / {ano} / {placa}")

#salva dados
carro("Honda", "Civic", 2000, "GDS-4567")

#outra forma, um pouco mais segura
carro(marca="Mazda", modelo="R7", ano=2000, placa="GDS-4567")

#outra forma, como dicionário
       #convenção para mostrar que está passando os dados como um dicionário
carro(**{"marca" : "Mazda", "modelo" : "R7", "ano" : 2000, "placa" : "GDS-4567"})

print()

def exibir_texto(data, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()} : {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_texto(
    "19/02/2025",
    "Como foi feito para dividir o *args e o **kwargs?",
    "A primeira linha exibirá a data da função exibir_texto em mensagem",
    "Depois, todo texto (separado por vírgula) entrará entrará como tupla em *args",
    "Quando acabar todo texto separado por vírgula",
    final_do_texto = "e começar o para chave valor",
    final_do_texto = "vai entender que não é mais *args e sim **kwargs"
)