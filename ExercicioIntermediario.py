usuarios = []  # L1

def cadastrar():  # L2
    nome = input("Nome do aluno: ")  # L3
    notas = []  # L4
    for i in range(3):  # L5
        while True:  # L6
            try:
                n = float(input(f"Nota {i+1}: "))  # L7
                break  # L8
            except ValueError:
                print("Valor inválido. Digite um número.")  # L9
        notas.append(n)  # L10
    media = sum(notas) / len(notas)  # L11
    usuarios.append({"nome": nome, "notas": notas, "media": media})  # L12
    print(f"Aluno {nome} cadastrado com média {media:.2f}.\n")  # L13

def boletim():  # L14
    if not usuarios:  # L15'''
        print("Nenhum aluno cadastrado.\n")  # L16
        return  # L17
    print("=== BOLETIM ===")  # L18
    for i, aluno in enumerate(usuarios, start=1):  # L19
        print(f"{i}. {aluno['nome']} - Média: {aluno['media']:.2f}")  # L20
    print()  # L21

def buscar():  # L22
    if not usuarios:  # L23
        print("Nenhum aluno cadastrado.\n")  # L24
        return  # L25
    termo = input("Digite o nome para buscar: ").strip().lower()  # L26
    encontrado = False  # L27
    for aluno in usuarios:  # L28
        if aluno["nome"].strip().lower() == termo:  # L29
            print(f"Nome: {aluno['nome']}")  # L30
            print("Notas:", ", ".join(f"{x:.2f}" for x in aluno["notas"]))  # L31
            print(f"Média: {aluno['media']:.2f}\n")  # L32
            encontrado = True  # L33
            break  # L34
    if not encontrado:  # L35
        print("Aluno não encontrado.\n")  # L36

def menu():  # L37
    while True:  # L38
        print("1 - Cadastrar aluno")  # L39
        print("2 - Mostrar boletim")  # L40
        print("3 - Buscar aluno por nome")  # L41
        print("4 - Sair")  # L42
        opc = input("Escolha uma opção: ").strip()  # L43

        if opc == "1":  # L44
            cadastrar()  # L45
        elif opc == "2":  # L46
            boletim()  # L47
        elif opc == "3":  # L48
            buscar()  # L49
        elif opc == "4":  # L50
            print("Saindo...")  # L51
            break  # L52
        else:  # L53
            print("Opção inválida.\n")  # L54

menu()  # L55
