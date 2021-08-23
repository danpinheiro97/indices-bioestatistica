ficha = dict()
ficha['Jogador'] = str(input('Nome do Jogador: '))
ficha['Partidas'] = int(input('Quantas partidas jogou?' ))
cont = 0
soma = 0
while cont < ficha['Partidas']:
    gol = int(input(f'Quantos gols na partida {cont+1}: '))
    cont += 1
    ficha['Total de Gols'] = soma = soma + gol
for k, v in ficha.items():
    print(f'{k} : {v}')
print(f'{ficha["Jogador"]} fez: {soma} gols no campeonato')
print(ficha)