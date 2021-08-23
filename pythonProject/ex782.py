from random import randint
lista = list()
maior = 0
menor = 0
for c in range(0,5):
    num = randint(1,1000)
    lista.append(num)
    if c == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(lista)
print(f'O maior número é: {maior} ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'na posição: {i+1}')
print(f'O menor número é: {menor} ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'na posição {i+1}')
