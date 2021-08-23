lista = list()
listap = list()
listai = list()
while True:
    n = int(input('Entre com um valor: '))
    lista.append(n)
    stop = str(input('Deseja Continuar? [S/N] ')).upper().strip()
    if n % 2 == 0:
        listap.append(n)
    if n % 2 != 0:
        listai.append(n)
    if stop == 'N':
        break
print(f'A lista completa é {sorted(lista)}')
print(f'A lista de pares é {sorted(listap)}')
print(f'A lista de impares é {sorted(listai)}')