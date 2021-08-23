def ficha(nome ='Desconhecido', gol = ''):
    print(f'O nome do jogador é {nome} e ele fez {gol} gols')


nome = str(input('Nome do Jogador: '))
gol = str(input('Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)


