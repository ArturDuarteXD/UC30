def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Error!, divisão por zero é impossível!"
    return a / b

def menu():
    print("\n ---Calculadora--- ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma das opções: ")

    if opcao == "0":
        print("Saindo da calculador...")
        break

    if opcao in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o seu primeiro número: "))
            num2 = float(input("Digite o seu segundo número: "))

            if opcao == "1":
                print("Resultado:", soma(num1, num2))
            elif opcao == "2":
                print("Resultado:", subtracao(num1, num2))
            elif opcao == "3":
                print("Resultado:", multiplicacao(num1, num2))
            elif opcao == "4":
                print("Resultado:", divisao(num1, num2))

        except ValueError:
            print("Erro!, Digite um valor válido!")
            # Professora aqui eu precisei de ajuda pra fazer
    else:
        print("Opção inválida!, Tente novamente.")