galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: ')).upper()
        if pessoa['Sexo'] in 'MF':
            break
        print('Digite apenas M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Continuar? [S/N]')).upper()
        if resp in 'SN':
            break
        print('Digite Apenas S ou N')
    if resp in 'N':
            break
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma/len(galera)
print(f'A média das idades é {media:.2f}')
print('As mulheres cadastradas foram: ', end='')
for p in galera: #Verifica dentro de galera os Sexos F e printa eles
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end =' ')
print()
print('Idades acima da média:', end='')
for peso in galera: #Verifica a idade dentro da galera e
    if peso['Idade'] > media:
        print('    ')
        for k, v in peso.items():
            print(f'{k} = {v};', end = ' ')
