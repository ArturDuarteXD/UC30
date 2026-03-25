def somar_todos(*numeros):
#E se você não souber quantos números o usuário vai enviar? o asterísco (*) diz ao Python
#para empacotar todos os argumentos como uma TUPLA (Pasta imutável)
    total = 0
    for num in numeros:
            total += num
    return total


print(somar_todos(1, 2, 3))
print(somar_todos(10, 20, 30, 40, 50))
print(somar_todos())