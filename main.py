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
        tarefa = input("Digite sua tarefa: ")

        nova_tarefa = {
            "descricao": tarefa,
            "concluida": False
        }

        tarefas.append(nova_tarefa)


    elif opcao == "2":
        print("Você escolheu Listar Tarefas")
        cont = 1
        for tarefa in tarefas:
            if tarefa["concluida"]:
                status = "[x]"
            else:
                status = "[ ]"
            print(f"{cont} -{status} {tarefa["descricao"]}")
            cont=cont+1
    elif opcao == "3":
       
        print("Você escolheu Concluir Tarefa")

        cont = 1

        for tarefa in tarefas:

            if tarefa["concluida"]:
                status = "[x]"
            else:
                status = "[ ]"

            print(f"{cont} - {status} {tarefa['descricao']}")

            cont = cont + 1

        numero = int(input("Qual tarefa você quer concluir? "))

        indice = numero - 1

        tarefas[indice]["concluida"] = True


    elif opcao == "4":
        print("Você escolheu Excluir Tarefa")
        numero = int(input("Qual tarefa você quer Excluir? "))
        indice = numero - 1

        tarefas.pop(indice)

    elif opcao == "0":
        print("Você escolheu Sair")
    else:
        print("Opção inválida")