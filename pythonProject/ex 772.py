vogais = 'a', 'e', 'i', 'o', 'u'
palavras = 'banana', 'amor', 'querida', 'aleluia'
for pos in range (0, len(palavras)):
    print(f'Na palavra {palavras[pos]} há as vogais: ', end='')
    for letras in palavras[pos]:
        if letras in vogais:
            print(letras, end='')
    print('')

lanche = [1]
lanche.