lista = []
dad = []
cont = 0
maior = 0
menor = 999
map = mep = ''
while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    dad.append(nome)
    dad.append(peso)
    lista.append(dad[:])
    dad.clear()
    stop = str(input('Continuar? [S/N]'))
    if stop in 'Nn':
        break
for p in lista:
    cont =+1
    if p[1] > maior:
        maior =p[1]
        map = p[0]
    if p[1] < menor:
        menor = p[1]
        mep =p[0]
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi de {maior}Kg e pertence há: ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{[p[0]]}', end='')
print()
print(f'O menor peso foi de {menor}Kg e pertence há: ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{[p[0]]}', end= '')
print()
