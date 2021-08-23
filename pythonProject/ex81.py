lista = list()
while True:
    n = int(input('Entre com um valor: '))
    stop = str(input('Você deseja continuar? [S/N]')).upper().strip()
    lista.append(n)
    if stop == 'N':
        break
print(f'Foram inseridos na lista: {len(lista)} números')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'O valor 5 foi digitado na lista {lista.count(5)} vezes')
else:
    print(f'Não há o valor 5 na lista')