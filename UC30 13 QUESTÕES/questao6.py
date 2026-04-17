temperaturas = []
for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i + 1}: "))
    temperaturas.append(temp)

soma = 0
for t in temperaturas:
    soma += t
media = soma / len(temperaturas)

print(f"A média das temperaturas é: {media:.2f}°C")

# For para coletar valores, temp para armazenar valores, float para ler os valores, len para ver o número de temperaturas.
# 2f eu tinha esquecido como usava, mas tu  ajudou a lembrar aqui na sala.