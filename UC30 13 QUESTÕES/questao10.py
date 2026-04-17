frase = input("Digite uma frase: ")
vogais = "a e i o u A E I O U"
contador = 0
for letra in frase:
    if letra in vogais:
        contador += 1
print("Quantidade de vogais:", contador)

#Nada muito diferente professora, Digitei as vogais, e usei of if para checar se a letra é vogal