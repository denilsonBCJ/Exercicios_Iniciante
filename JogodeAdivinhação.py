import random
resultado = random.randint(1, 100)
for i in range(5):
    while True:
        n1 = int(input(" Tente adivinhar o numero entre 1 e 100 que estou pensando tem 5 tentativas: "))
        if resultado == n1:
            print(" Vc acertou o numero parabens !")
            break
        elif resultado < n1:
            print(" Vc errou o numero e menor !")
        elif resultado > n1:
            print(" Vc errou o numero e maior !")