dad = list()
lista = list()
cont = 0
maiorp = 0
menorp = 999
map = ''
mep = ''

while True:
    dad.append(str(input('Nome: ')))
    dad.append(int(input('Peso: ')))
    lista.append(dad[:])
    dad.clear()
    stop = str(input('Você deseja continuar? [S/N] ')).upper().strip()
    if stop == 'N':
        break
for p in lista:
    cont += 1
    if p[1] > maiorp:
        maiorp = p[1]
        map = p[0]
    if p[1] < menorp:
        menorp= p[1]
        mep = p[0]
print(f'Foi cadastrado {cont} pessoas')
print(f'O maior peso {maiorp} Kg pertence há', end=' ')
for p in lista:
    if p[1] == maiorp:
        print(f'{[p[0]]}', end=' ')
print()
print(f'O menor peso {menorp} Kg pertence há', end=' ')
for pi in lista:
    if pi[1] == menorp:
        print(f'{[pi[0]]}', end =' ')



