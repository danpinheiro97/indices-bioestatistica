listanum = list()
stop = ''
while stop != 'N':
    n = int(input('Entre com um valor: '))
    if n not in listanum:
        print('Número adicionado na lista')
        listanum.append(n)
    else:
        print(f'O número {n} já existe e não foi adicionado')
    stop = str(input('Você deseja continuar? [S/N]: ')).upper().strip()
listanum.sort()
print(f'Os números na sua lista são {listanum}')



