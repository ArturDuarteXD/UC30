valor = float(input("Digite o valor do produto: "))
if valor > 500:
    desconto = 0.2
elif 200 <= valor <= 500:
    desconto = 0.1
else:
    desconto = 0
preco_final = valor - (valor * desconto)
print("Preço final:", preco_final)

# Desconto, pelo que eu tava vendo precisa usar 0. e o número, e usei elif para adicionar uma variável