casdastros = []
while True:
    print ("\n1 - Adicionar nome\n2 - Listar nomes\n3 - Sair")
    opcao = input("Escolha uma opçao: ")

    if opcao == "1":
        nome = input("Digite o nome:")
        casdastros.append(nome)
        print("Nome cadastrado!")

    elif opcao == "2":
        print("\nLista de nomes:")
        for nome in casdastros:
            print(nome)

    elif opcao == "3":
         print("Saindo programa...")
         break
    
    else:
        print("Opção inválida!Tente novamente.")
