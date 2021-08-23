from time import sleep
def contador (*c):
    for c in range (0, (10+1),1):
        print(c, end=' ')
        # sleep(0.5)
    print()
    print('-' * 20)
    for c in range (0, 10+1, 2):
        print(c, end=' ')
        # sleep(1)
    print()
    print('-'*20)
    print('Agora é sua vez de personalizar o contador: ')
    ini = int(input('Início'))
    fim = int(input('Fim'))
    passo = int(input('Passo'))
    if passo == 0:
        passo = 1
    if ini > fim:
        for c in range(ini, fim-1, -passo):
            print(c, end=' ')
            # sleep(1)
    if ini < fim:
        for c in range(ini, fim+1, passo):
            print(c, end=' ')
        print()
        print('-'*20)


contador()