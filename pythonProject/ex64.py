num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Entre com um valor inteiro'))
    if num != 999:
       soma += num
       cont += 1
print('Foi digitado {} valores e a soma dos valores é {}'.format(cont, soma))
