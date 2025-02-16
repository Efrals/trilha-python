texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
       #transforma letras para CAIXA ALTA
    if letra.upper() in VOGAIS:
        print(letra,end="")
#opcional
else:
    print("")
    print("Executado")