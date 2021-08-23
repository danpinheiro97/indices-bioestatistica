lista = list()
for c in range(0, 5):
    n = int(input('Valor'))
    if c == 0 or n >= lista[-1]:
        lista.append(n)
        print(f'O valor foi adicionado na última posição')
    else:
        cont = 0
        while cont < len(lista):
            if n <= lista[cont]:
                lista.insert(cont, n)
                print(f'Valor inserido na posição {cont}')
                break
            cont +=1
print(lista)
