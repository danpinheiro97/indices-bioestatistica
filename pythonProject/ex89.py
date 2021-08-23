lista = list()
cont = 0
while True:
    nome = str(input('Nome: '))
    not1 = int(input('Nota 1: '))
    not2 = int(input('Nota 2: '))
    media = (not1 + not2)/ 2
    lista.append([nome, [not1, not2], media])
    stop = str(input('Deseja continuar? [S/N]'))
    if stop in 'Nn':
        break
print('-='*15)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' *15)
for c, i in enumerate(lista):
    print(f'{c:<4}{i[0]:<10}{i[2]:>8.1f}')
while True:
    alu = int(input('Você deseja ver a nota de algum aluno? [Nº] ou 999 para parar '))
    if alu == 999:
        print('Volte Sempre!!!')
        break
    if alu <= len(lista):
        print(f'As notas do aluno {lista[alu][0]} são {lista[alu][1]}')





    #[[Nome [5,0], [6,8]], Nome ]