total = 0.0
while True:
    valor = float(input("Digite o valor do item , ou digite 0 para finalizar!: "))
    if valor == 0:
        break
    total += valor
print("Total final:", total)

#Usei o break para finalizar o loop, e while para continuar pedindo o valor dos itens.