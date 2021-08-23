matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
listp = list()
soma = 0
soma3=0
maior = 0
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
        if matriz[l][c] % 2 == 0:
            listp.append(matriz[l][c])
            soma = soma + matriz[l][c]
print('='*30)
for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range (0,3):
    soma3 = soma3 + matriz[l][2]
for c in range (0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[2][c] > maior:
        maior = matriz[1][c]

print(f'Os números pares são {listp}, e sua soma é {soma}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')



