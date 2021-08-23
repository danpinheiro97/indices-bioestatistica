bra = 'Brasileirão SÉRIE A', 'Flamengo', 'Internacional', 'Atlético - MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Atlético - PR'
bra1 = 'Bragantino', 'Ceará', 'Corinthians', 'Atlético - GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco'
bra2 = 'Goiás', 'Coritiba', 'Botafogo'
brasileirao = bra + bra1 + bra2
print(f'O TOP 4 do brasileirão é: {brasileirao[1:5]}')
print(f'Os 5 últimos colocados são: {brasileirao[16:21]}')
print('Coritibá está na posição {}'.format(brasileirao.index('Coritiba')))
for cont, time in enumerate (brasileirao):
    print(f' {cont} - {time}')
#for cont, time in enumerate(brasileirao):
