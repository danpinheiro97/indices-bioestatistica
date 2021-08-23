jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do Jogador:'))
tot = int(input(f'Quantos partidas o {jogador["Nome"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
jogador['Gols'] = partidas[:]
jogador['Total de Gols'] = sum(partidas)
for k, v in jogador.items():
    print(f'{k} : {v}')
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'   ==> Na partida {i+1}, o {jogador["Nome"]} fez {v} gols')
print(f'Foi um total de {jogador["Total de Gols"]} gols.')

