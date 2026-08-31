opcao = ""

tarefas = []


while opcao != "0":
    print("================================")
    print("      GERENCIADOR DE TAREFAS")
    print("================================")
    print("")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")
    opcao = input("escolha uma opção: ")


    if opcao == "1":
        print("Você escolheu Adicionar Tarefa")
        tarefa = input("digite sua tarefa: ")
        tarefas.append(tarefa)


    elif opcao == "2":
        print("Você escolheu Listar Tarefas")
        cont = 1
        for tarefa in tarefas:
            print(f"{cont} - {tarefa}")
            cont=cont+1
    elif opcao == "3":
        print("Você escolheu Concluir Tarefa")
    elif opcao == "4":
        print("Você escolheu Excluir Tarefa")
    elif opcao == "0":
        print("Você escolheu Sair")
    else:
        print("Opção inválida")