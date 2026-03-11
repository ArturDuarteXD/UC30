aluno = {}

aluno["nome"] = input("Qual o seu nome?: ")
aluno["nota1"] = input("Qual sua nota da 1° prova?: ")
aluno["nota2"] = input("Qual sua nota da 2° prova?: ")

media =(aluno["prova1"] + aluno["nota2"]) / 2

aluno[media] = media

if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperacao"
else:
    situacao = "reprovado"


print("\nInformações do Aluno:")
print(aluno)
print("situação do aluno: ", situacao) 
