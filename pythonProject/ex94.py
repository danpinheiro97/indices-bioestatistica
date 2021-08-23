ficha = dict()
lista = list()
listaf = list()
listai = list()
cont = 0
soma = 0
while True:
    ficha['Nome'] = str(input('Nome: '))
    ficha['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    ficha['Idade'] = int(input('Idade: '))
    stop = str(input('Continuar? [S/N]'))
    lista.append(ficha.copy())
    cont += 1
    soma += ficha['Idade']
    media = soma/cont
    if ficha['Sexo'] in 'Ff':
        listaf.append(ficha['Nome'])
    if stop in 'Nn':
        break
print(f'Ao todo {len(lista)} pessoas foram cadastradas')
print(f'A média de idade dos inscritos foi {media:.2f} anos')
print(f'A lista de mulheres do grupo é: {listaf}')
print(f'A lista de pessoas mais velhas do que a média é: {listai}')



