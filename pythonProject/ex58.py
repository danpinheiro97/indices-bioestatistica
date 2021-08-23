from random import randint
com = randint(1, 10)
jog = int(input('Entre com um número: '))
cont = 1
while com != jog:
    print('Você escolheu {} e eu escolhi {}'.format(jog, com))
    jog = int(input('Errado, entre com um número novamente: '))
    com = randint(1, 10)
    cont = cont +1
    if com == jog:
        print('================================================')
        print('Você escolheu {} e eu escolhi {}'.format(jog, com))
        print('Parabéns, você escolheu o mesmo número que eu!!!')
        print('Você precisou de {} tentativas'.format(cont))
        print('================================================')




