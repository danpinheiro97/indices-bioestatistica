tup = (int(input('Entre com um primeiro valor')), int(input('Entre com um segundo valor')),
       int(input('Entre com um terceiro valor')), int(input('Entre com um quarto valor')))
print(f'O valor 9 apareceu {tup.count(9)} vezes')
if 3 in tup:
    print(f'O valor 3 apareceu na posição {tup.index(3)}')
if 3 not in tup:
    print('Não há número 3 nas entradas')
for num in tup:
    if num % 2 == 0:
        print(f'Os números pares foram {tup}')