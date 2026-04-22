cardapio = [
    {
        "id": "1", 
        "nome": "Prato Feito", 
        "preco": 15.00, 
        "desc": "Arroz, feijão, farofa e ovo mexido. Opção barata e nutritiva.",
        "tags": "Contém Glúten, Vegetariano"
    },
    {
        "id": "2", 
        "nome": "Salada Completa", 
        "preco": 20.00, 
        "desc": "Mix de folhas, tomate, e cenoura.",
        "tags": "Vegano, Sem Glúten"
    },
    {
        "id": "3", 
        "nome": "Sopa de Legumes", 
        "preco": 12.00, 
        "desc": "Sopa quente,com batata, cenoura e macarrão.",
        "tags": "Vegetariano"
    }
]

print("=======================================")
print("     CARDÁPIO DIGITAL INCLUSIVO        ")
print("   Feito por: Artur D., Lucas C., Vinicius L.   ")
print("=======================================")
executando = True

while executando:
    print("\nMENU PRINCIPAL:")
    print("1 - Menu principal")
    print("2 - Informações para alérgicos")
    print("3 - Sobre o nosso projeto (ODS 10)")
    print("0 - Sair")
    
    escolha = input("\nDigite o número da opção desejada!: ")

    if escolha == "1":
        print("\n--- LISTA DE PRATOS ---")
        for item in cardapio:
            print(f"[{item['id']}] {item['nome']} - R$ {item['preco']:.2f}")
            print(f"    Descrição: {item['desc']}")
            print("-" * 30)

    elif escolha == "2":
        print("\n--- INFORMAÇÕES DE INCLUSÃO ALIMENTAR ---")
        for item in cardapio:
            print(f"{item['nome']}: {item['tags']}")

    elif escolha == "3":
        print("\n--- OBJETIVO ODS 10 ---")
        print("O nosso sistema visa reduzir a desigualdade à:")
        print("- Facilitar a leitura para quem tem dificuldade visual.")
        print("- Fornecer informações claras sobre a comida.")
        print("- Ser simples e rodar em qualquer dispositivo.")

    elif escolha == "0":
        print("\nObrigado por usar o sistema! Até logo!")
        executando = False
    
    else:
        print("\n[Erro] Opção inválida! Use apenas os números do menu!")
