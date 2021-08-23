prod = 'Arroz', 19.99, 'Feijão', 8.99, 'Coca-Cola', 8.99, 'Sal', 4.99, 'Açucar ', 6.99
print('=' *42)
print(f'{"Nota Fiscal":^42}')
print('=' *42)
for c in range(0, len(prod)):
    if c % 2 == 0:
        print(f'{prod[c]:.<35}', end='')
    if c % 2 == 1:
        print(f'R${prod[c]:>5.2f}')
print('=' *42)