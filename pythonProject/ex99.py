def maioremenor(numeros):
    maior = 0
    menor = 999
    while True:
        num = int(input('Valor: '))
        numeros.append(num)
        stop = str(input('Continuar?'))
        if stop in 'Nn':
            break
    for i, v in enumerate(numeros):
        if i == 0:
            maior = v
            menor = v
        if v > maior:
            maior = v
        if v < menor:
            menor = v
    print(f'{numeros}')
    print(f'O maior número da lista é {maior} e o menor é {menor}')

num = list()
maioremenor(num)