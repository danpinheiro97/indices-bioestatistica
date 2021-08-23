num = int(input('Entre com um número inteiro: '))
fat = num
fator = 1
print('{}! = '.format(num), end='')
while fat > 0:
    print('{}'.format(fat), end='')
    print((' x ' if fat > 1 else ' = '), end='')
    fator = fator * fat
    fat = fat - 1 # Contador do fat para ativar o while
     #Calcula o número * fat (num -1)
#num passa a compreender o valor de fator e retorna para fator² como resultado do fator 1
print('{}'.format(fator))
    #Fator é 5*3 = 15 *4 = 60


