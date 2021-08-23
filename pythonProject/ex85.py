lista= [[], []]
for num in range(0, 7):
    n = int(input('Entre com um valor'))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 != 0:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os números pares são {lista[0]}')
print(f'Os números impares são {lista[1]}')






