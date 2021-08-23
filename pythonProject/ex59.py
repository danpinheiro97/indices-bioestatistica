opc = 0
val1 = int(input('Entre com um valor inteiro: '))
val2 = int(input('Entre com um segundo valor inteiro: '))
while opc !=5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opc = int(input('Qual operação você deseja realizar? '))
    if opc == 1:
        soma = val1 + val2
        print('A soma dos valores {} e {} é {}'.format(val1, val2, soma))
    if opc ==2:
        mult = val1 * val2
        print('A multiplicação dos valores {} e {} é {}'.format(val1, val2, mult))
    if opc ==3:
        if val1 > val2:
            print('O valor {} é maior do que o valor {}'.format(val1, val2))
        elif val1 == val2:
            print('Os valores {} e {} são iguais'.format(val1, val2))
        else:
            print('O valor {} é maior do que o valor {}'.format(val2, val1))
    if opc ==4:
        val1 = int(input('Entre com um valor inteiro: '))
        val2 = int(input('Entre com um segundo valor inteiro: '))
    if opc ==5:
        print('Programa finalizado')

