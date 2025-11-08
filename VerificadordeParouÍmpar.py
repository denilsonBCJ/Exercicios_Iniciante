while True:
    print('================================================================')
    print('|                                                              |')
    print('|            📋 Verificador de Par ou Ímpar                    |')
    print('|                Digite sair para fechar                       |')
    print('|                                                              |')
    print('================================================================')

    resposta = input('Digite um numero e direi se ele e par ou impar:')

    if resposta.lower() == "sair":
        break

    try:
        n1 = int(resposta)

    except ValueError:
        print(f"Erro: '{resposta}' não é um número válido nem 'sair'. Tente novamente.")

    if n1 % 2 == 0:
        print('O numero ',n1,'é Par !')
        
    elif resposta == "sair":
        break

    else:
        print('O numero ',n1,'é Impar !')
