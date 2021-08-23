n = (int(input('Entre com um valor: ')),
     int(input('Entre com um outro valor: ')),
     int(input('Entre com um valor: ')),
     int(input('Entre com um outro valor: ')))
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('Não há número 3')
print('Os números pares são: ', end='')
for num in n:
    if num % 2 ==0:
        print(f'{num}\t', end='')

