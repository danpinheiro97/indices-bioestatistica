n = 999
while n > -1:
    n = int(input('Entre com um valor '))
    #Tabuada
    for c in range (1, 11):
       tab = n * c
       print(f'{n} X {c} = {tab}')
    if n < -1:
        print('Programa encerrado')



