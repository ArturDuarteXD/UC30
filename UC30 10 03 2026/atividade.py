paciente = {}

paciente["nome"] = input("Qual seu nome: ")
paciente["idade"] = int(input("Quantos anos você tem: "))
paciente["peso"] = float(input("Digite seu peso(kg): "))
paciente["altura"] = float(input("Digite sua altua (m): "))

imc = paciente["peso"] / (paciente["altura"] ** 2)
paciente["imc"] = imc

print("\n Dados")
print("Nome: ", paciente["nome"])
print("Idade: ", paciente["Idade"])
print("Peso: ", paciente["Peso"])
print("Altura: ", paciente["Altura"])
print("IMC: ", round(paciente["altura"], 2))
