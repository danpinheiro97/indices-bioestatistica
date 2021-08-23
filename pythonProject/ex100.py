from random import randint

def sorteia(banana, bananap): #No () eu defino a variavel q vai entrar na função
    print(f'Os números gerados foram: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        banana.append(n)
        print(f'{n} ', end='')
    print()
    for valor in banana:
      if valor % 2 ==0:
          bananap.append(valor)
    print(f'Os números pares dentro da lista de números gerados é {bananap}')


def soma(banana):
    soma = 0
    for i, v in enumerate(banana):
        if v % 2 == 0:
            soma += v
    print(f'A soma dos números pares em {banana} é {soma}')


numeros = list()
numerosp = list()
sorteia(numeros, numerosp)
soma(numerosp)
