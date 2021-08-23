pt = int(input('Entre com o primeiro termo da PA: '))
raz = int(input('Entre com a razão da PA: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' - ')
        termo = termo + raz
        cont = cont+1
        print('Over')
        mais = int(input('Quantos termos você deseja ver a mais?'))
print('Over')


#PA 10 em razão 2 nos 10 primeiros t = 10 - 12 - 14 - 16 -  18 - 20 - 22 - 24 - 26 - 28