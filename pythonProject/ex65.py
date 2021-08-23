resp = 'S'
num = 0
soma = 0
cont = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Entre com um valor: '))
    soma = soma + num
    cont = cont +1
    media = soma/cont
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Você deseja continuar? [S/N]'))
print('A sua média é de {}'.format(media))
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))




