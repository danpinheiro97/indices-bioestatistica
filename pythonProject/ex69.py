keep = ''
conti = 0
contm = 0
contmi = 0
while keep != 'N':
    id = int(input('Qual é a sua idade? '))
    sex = str(input('Qual é o seu sexo? ')).strip().upper()
    if id >= 18:
        conti += 1
    if sex == 'M':
        contm += 1
    if sex == 'F' and id <= 20:
        contmi += 1
    keep = str(input('Você deseja continuar? [S/N]')).strip().upper()
    if keep == 'N':
        print(f'{conti} pessoas tem mais de 18 anos \n{contm} homens foram cadastrados\n{contmi} mulheres tem menos de 20 anos')
        break



