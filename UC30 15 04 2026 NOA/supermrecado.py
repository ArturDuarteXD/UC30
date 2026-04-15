produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))

def calcular_total(produto1, produto2):
        total = produto1 + produto2
        return total

print("O valor total dos produtos é: R$", calcular_total(produto1, produto2))