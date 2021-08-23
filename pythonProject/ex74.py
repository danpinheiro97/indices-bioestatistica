from random import randint
print(f'Os 5 valores gerados aleatoriamente são: ')
cont = 0
for c in range(0,5):
    na = randint(1, 1000)
    nat = na
    cont += 1
    if cont ==1:
        maior = na
        menor = na
    if cont > 1:
        if na > maior:
            maior = na
        if na < menor:
            menor = na
    print(f'{nat}')
print(f'O menor valor na tupla é {menor} e o maior valor é {maior}')

