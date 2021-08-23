def area(a, b):
    print('Controle de Terrenos')
    print('-'*30)
    m = a * b
    print(f'O tamanho de um terreno de {largura} X {comprimento} é de {m} m²')

largura = int(input('Largura:  '))
comprimento = int(input('Comprimento:  '))
area(largura, comprimento)

