def linha():
    print('-'*80)
ficha = list()
alunos = dict()
while True:
    alunos['Nome'] = str(input('Nome: '))
    n1 = int(input('Nota 01: '))
    n2 = int(input('Nota 02: '))
    n3 = int(input('Nota 03: '))
    n4 = int(input('Nota 04: '))
    alunos['Notas'] = n1, n2, n3, n4
    stop = str(input('Continuar? [S/N]'))
    alunos['Media'] = sum(alunos['Notas'])/4
    if alunos['Media'] >= 7:
        alunos['Situação'] = 'APROVADO'
    if alunos['Media'] < 7:
        alunos['Situação'] = 'REPROVADO'
    ficha.append(alunos.copy())
    if stop in 'Nn':
        print('Programa Finalizado!')
        break
print(f'{"COD"}', end='')
for k in alunos.keys():
    print(f'{k:>16}', end='')
print()
linha()
for k, v in enumerate(ficha):
    print(f'{k+1}', end ='')
    for d in v.values():
        print(f'{str(d):>18}',end='')
    print()
