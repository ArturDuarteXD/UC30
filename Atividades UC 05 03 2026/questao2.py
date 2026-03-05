import random

numeros = [91, 34, 67, 15, 82]

print("Números na ordem da professora: ", numeros)

numeros.sort()
print("Números ordenados em ordem crescente: ", numeros)

numeros.sort(reverse = True )
print("Números ordenados em ordem decrescente: ", numeros)

numeros3 = [6, 7, 8, 9, 10]
random.shuffle(numeros3)
print("Números 3 embaralhados aleatóriamente: ", numeros3)

numerosartur = [6, 7, 67, 76, 677, 667]

numerosartur.sort()
print("Números ordenados em ordem crescente: ", numerosartur)

numerosartur.sort(reverse = True)
print("Números ordenados em ordem decrescente: ", numerosartur)

random.shuffle(numerosartur)
print("Meus números embaralhados aleatóriamente: ", numerosartur)