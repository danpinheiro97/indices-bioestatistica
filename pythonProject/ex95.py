ficha = list()
cont = 0
while True:
    jogador = dict()
    partidas = list()
    jogador['Nome'] = str(input('Nome do Jogador:'))
    tot = int(input(f'Quantos partidas o {jogador["Nome"]} jogou?'))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
        cont +=1
    jogador['Gols'] = partidas[:]
    jogador['Total de Gols'] = sum(partidas)
    ficha.append(jogador.copy())
    stop = str(input('Continuar? [S/N]'))
    if stop in 'Nn':
        break
print('-=' * 20)
print((f'{"COD":<4}'), end ='')
for k in jogador.keys():
    print(f'{k:>4}', end = '       ')
print()
print('-=' * 20)
for k, v in enumerate(ficha):
    print(f'{k+1}', end ='   ')
    for d in v.values():
        print(f'{str(d):<11}', end='')
    print()
print('-=' * 20)
jog = 0
while True:
    jog = int(input('Mostrar dados de qual jogador? 999 = Stop'))
    if jog == 999:
        print('Volte Sempre')
        break
    if jog <= len(ficha):
        for k, v in jogador.items():
            print(f'{k} : {v}')
        print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
        for i, v in enumerate(jogador['Gols']):
            print(f'   ==> Na partida {i+1}, o {jogador["Nome"]} fez {v} gols')
        print(f'O jogador {jogador["Nome"]} fez um total de {jogador["Total de Gols"]} gols.')





