lista = []
while True:
    n = int(input('Valor: '))
    lista.append(n)
    stop = str(input('Continuar? [S/N}]'))
    if stop in 'Nn':
        break
qto = len(lista)
lista.sort(reverse=True)
print(f'O tamanho da lista é de {qto} valores')
print(lista)
if 5 in lista:
    print(f'O número 5 está na lista na posição {lista.index(5)+1}')
else:
    print(f'Não há número 5 na lista')
