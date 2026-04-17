vendas = []

for i in range(5):
    temp = float(input(f"Digite o total de vendas {i + 1}: "))
    vendas.append(temp)

soma_pares = 0

for v in vendas:
    if v % 2 == 0:
        soma_pares += v

print("Soma dos valores pares:", soma_pares)

#Não sabia se usava valores prédeterminados, ou não, então usei a mesma estrutura da outra questão
#de resto, também já tinha usado em outras questões.