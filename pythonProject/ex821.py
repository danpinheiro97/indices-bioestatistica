lista = list()
listap = list()
listai = list()
while True:
    n = int(input('Valor: '))
    lista.append(n)
    if n  % 2 == 0:
        listap.append(n)
    elif n % 2 !=0:
        listai.append(n)
    stop = str(input('Continuar? [S/N]'))
    if stop in 'Nn':
        break
print(lista)
print(listap)
print(listai)