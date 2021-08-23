s = 0
cont = 0
while True:
    n = int(input('Entre com um valor: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Você digitou \033[35m{cont}\033[m valores e a soma dos valores é \033[34m{s}')
