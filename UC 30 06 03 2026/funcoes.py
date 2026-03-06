notas = [7.5, 8.0, 9.5, 6.0, 8.5]
print("Notas: ", notas)

print("Menor: ", min(notas)) #Vê o menor valor
print("Maior: ", max(notas)) #Vê o maior valor
print("Soma: ", sum(notas)) #Soma os valores
print("Media: ", sum(notas) / len(notas)) #Diz a média dos valores

nomes = ["Adriana", "Breno", "Carla", "Daniel"]
print("Nomes: ", nomes)
#Appenas o elemento
print("usando FOR simples: ")
for nome in nomes: 
    print(f"Olá, {nomes}")

#Indice e elemento
print("\n usando Enumerate: ")
for indice, nome in enumerate(nomes):
    print(f"Posição {indice}: {nome}")


original = ["A", "B", "C"]
copia = list(original)

print("Original: ", original)
print("Copia: ", copia)
print("São iguais: ", original == copia)

copia.append("D")
print("Original: ", original)
print("Copia: ", copia)
print("São iguais: ", original == copia)