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
print(ficha)