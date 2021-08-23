sexo = ''
while sexo != 'M' or sexo != 'F':
    sexo = str(input('Qual é o seu sexo? (M/F) ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        print('Seu sexo é {}'.format(sexo))
        break

