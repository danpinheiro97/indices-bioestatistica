from random import randint
# pa = n %2 = 0
# impar = n %2 != 0
com = 0
joge = ''
jogn = 0
situ = ''
cont = 0
nome = (str(input('Qual é o seu nome?')))
while situ != f'{nome} PERDEU':
    com = randint(1,11)
    print('=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=--=')
    joge = str(input('Escolha Par ou Ímpar: ')).upper().strip()
    jon = int(input('Escolha um número entre 1 e 10: '))
    print('=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=--=')
    soma = com +jon
    if soma % 2 == 0:
        somae = 'PAR'
    if soma % 2 != 0:
        somae = 'IMPAR'
    if joge =='PAR':
        come = 'IMPAR'
    elif joge =='IMPAR':
        come = 'PAR'
    print('=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=--=')
    print(f'COM escolheu {come} e escolheu o número {com}')
    print(f'{nome} escolheu {joge} e escolheu o número {jon}')
    print('=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=--=')
    if joge =='PAR' and soma % 2 == 0 or joge == 'IMPAR' and soma % 2 != 0:
        print('=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=--=')
        print(f'{nome} Venceu o COMPUTADOR, pois {soma} é um número {somae}')
        cont += 1
    if joge == 'PAR' and soma % 2 != 0 or joge == 'IMPAR' and soma % 2 == 0:
        situ = f'{nome} PERDEU, COMPUTADOR venceu pois {soma} é um número {somae} '
        print('=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=--=')
        print(situ)
        print(f'Você teve {cont} vitórias consecutivas')
        break






