prod = 'Arroz', 7.99, 'Feijão', 5.99, 'Carne Moída', 19.00, 'Cereal', 9.99, 'Nescau', 8.99
print('=' * 40)
print(f'{"lISTAGEM DE PREÇOS":^40}')
print('=' * 40)
for n in range(0, len(prod)):
    if n % 2 == 0:
        print(f'{prod[n]:.<30}', end='')
    else:
        print(f'R${prod[n]:>7.2f}')
print('-' *40)
