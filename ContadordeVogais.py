print('================================================================')
print('|                                                               |')
print('|              📚 5. Contador de Vogais                         |')
print('|                                                               |')
print('================================================================')

vogais = "aeiou"
palavra = input("Digite uma palavra: ")
contagem_vogais = 0
for letra in palavra:
    if letra.lower() in vogais:
        contagem_vogais += 1  
print(f"\nA palavra '{palavra}' tem {contagem_vogais} vogais.")