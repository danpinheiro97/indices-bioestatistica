from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
jogadores['Jogador1'] = randint(1, 6)
jogadores['Jogador2'] = randint(1, 6)
jogadores['Jogador3'] = randint(1, 6)
jogadores['Jogador4'] = randint(1, 6)
ranking = ()
print('-=' *15)
print(f'{"VALORES SORTEADOS":^15}')
print('-=' *15)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse=True) #ordena do maior para o menor
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)