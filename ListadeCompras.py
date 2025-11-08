lista_compras = []
def adicionar():
    item = input(" Digite um item para lista de compras: ")
    lista_compras.append(item)
    print(" Item adicionada com sucesso!\n")
def listar():
    if not lista_compras:
        print(" Nenhuma tarefa cadastrada.\n")
        return
    print("\n Lista de tarefas:")
    print(lista_compras)
        
def remover():
    listar()
    try:
        num = input("Digite o nome do item para remover: ")
        lista_compras.remove(num)
        print("O item ",num,"foi removido!")

    except (ValueError, IndexError):
        print(" Número inválido!\n")
    
while True:
    print('================================================================')
    print('|                                                               |')
    print('|                 📦 3. Lista de Compras                        |')
    print('|                                                               |')
    print('================================================================')
    print(" 1 - Adicionar itens a uma lista.")
    print(" 2 - listar todos items.")
    print(" 3 - Remover um item pelo nome.")
    print(" 4 - Sair")
    resposta = int(input(" Selecione uma opção: "))
    if resposta == 1:
        adicionar()
        print(" Item adicionado com sucesso! ")
    elif resposta == 2:
        print(" ==== lista de Compras ==== ")
        listar()
    elif resposta == 3:
        remover()
        print("Item removido com sucesso!")
    elif resposta == 4:
        break

