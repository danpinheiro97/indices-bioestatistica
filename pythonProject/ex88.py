from random import randint
lista = list()
jogo = list()
print('-='* 15)
print(f'{"JOGOS DA MEGASENA":^30}')
print('-='*15)
qtd = int(input('Quantos jogos você deseja? '))
print('-='*15)
tot = 1
while tot <= qtd:
    cont= 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {qtd} jogos', '-='*3)
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}: {l}')