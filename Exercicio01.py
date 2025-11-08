while True:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    opracao = input("Digite qual operação deseja fazer + - * / ou digite sair para fechar:")
    if opracao == "+":
        soma = n1 + n2
        print("A soma é: ",soma)
    elif opracao == "-":
        menos = n1 - n2
        print("A subtração é: ",menos)
    elif opracao == "*":
        multi = n1 * n2
        print("A multiplicação é: ",multi)
    elif opracao == "/":
        divi = n1 / n2
        print("A subtração é: ",divi)
    elif opracao == "sair":
        break
    else:
        print("Digite uma operação valida !")


