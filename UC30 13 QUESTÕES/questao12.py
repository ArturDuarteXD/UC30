# Pegou pesado professora, mas já fizemos uma parecida com essa então eu acho q eu sei
while True:
    print("Menu de Calculadora:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '5':
        print("Saindo da calculadora! Até mais!")
        break
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    try:
        if escolha == '1':
            resultado = num1 + num2
            print(f"Resultado da soma: {resultado}")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"Resultado da subtração: {resultado}")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"Resultado da multiplicação: {resultado}")
        elif escolha == '4':
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida!")

#Prints são para mostrar as opções, input é para decidir a opção, try para executar os códigos, e except para tratar o erro
#Break para acabar com o codigo .