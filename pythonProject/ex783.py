lista = list()
while True:
    num = int(input('Valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Número já está na lista')
        continue
    stop = str(input('Continuar? [S/N]'))
    if stop in 'Nn':
        print('Programa encerrado')
        break
lista.sort()
print(lista)

