def calculadora_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        if imc < 18.5:
            return "Classificação do IMC: Abaixo do peso!"
        elif 18.5 <= imc < 25:
            return "Classificação do IMC: Normal!"
        else:
            return "Classificação do IMC: Acima do peso!"
    except ZeroDivisionError:
        return "Erro de divisão por zero! A altura deve ser maior que zero!"
    
# Não sei se usei o except certo, mas de resto já tinhamos feito.