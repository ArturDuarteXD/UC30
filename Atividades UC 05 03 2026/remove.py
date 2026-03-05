nomes = ["Ana", "Bruno", "Carlos", "Diana"]
print("Nomes: ", nomes)

nomes.remove("Bruno")
print("Lista Atualizada: ", nomes)

removido = nomes.pop(1)
print(f"removido: {removido}")
print("Após pop(): ", nomes)

del nomes[0]
print("Após del nomes [0]", nomes)

nomes.clear()
print("Lista atualizada: ", nomes)