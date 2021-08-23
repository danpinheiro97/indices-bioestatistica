import heapq
maior1 = 0
maior2 = 0
id1 = 0
id2 = 0
print('='*30)
print(f'{"PEPITAGEM":^30}')
print('='*30)
for c in range(0, 6):
    peso = float(input('Peso: '))
    id = int(input('Identificação (nª): '))
    if c == 0:
        maior1 = peso
        maior2 = 0
        id1 = id
        id2 = id
    if peso > maior1:
        maior1 = peso
        id1 = id
    if peso > maior2 and peso < maior1:
        maior2 = peso
        id2 = id
print(f'O maior peso é {maior1} nºIdentificação {id1}')
print(f'O segundo maior peso é {maior2} nºIdentificação {id2}')





