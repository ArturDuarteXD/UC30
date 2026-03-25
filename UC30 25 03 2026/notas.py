def resumo_notas(*notas):
    soma = 0
    maior = notas[0]
    menor = notas[0]
    
    for nota in notas:
        soma += nota
    if nota < menor:
        menor = nota

    media = soma / len(notas)

    return soma, media, maior, menor
