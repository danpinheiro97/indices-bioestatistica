matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
listp = list()
soma = 0
soma3=0
maior = 0
for l in range (0, 3): #Cria 3 linhas
    for c in range (0, 3): #Cria 3 colunas
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:')) #Entrada de valor na posição [x, y]
        if matriz[l][c] % 2 == 0: #Se a entrada da posição na matriz for par:
            listp.append(matriz[l][c]) #Adiciona na lista de pares
            soma = soma + matriz[l][c] #Soma dos numeros pares
print('='*30)
for l in range (0, 3): #Cria 3 linhas
    for c in range(0, 3): #Cria 3 colunas
        print(f'[{matriz[l][c]:^5}]', end='') #Acrescenta os valores digitados acima na matriz
    print() #Pula uma linha
for l in range (0,3): # Conta as 3 linhas
    soma3 = soma3 + matriz[l][2] #Soma os números da coluna 3
for c in range (0,3): #Conta 3 colunas
    if c == 0: #
        maior = matriz[1][c]
    elif matriz[2][c] > maior:
        maior = matriz[1][c]

print(f'Os números pares são {listp}, e sua soma é {soma}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')



