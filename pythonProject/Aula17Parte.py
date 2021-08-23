teste = list() #Abre a função lista para a variável teste
teste.append('Daniel') #Adiona a string dentro da lista teste
teste.append(20) #Adiona a string dentro da lista teste
galera = list() #Abre a função lista para a variável galera
galera.append(teste[:]) #Faz uma cópia completa da lista teste dentro da lista galera
teste[0] = 'Maria'  #Adiona a string dentro da lista teste
teste[1] = 20  #Adiona a string dentro da lista teste
galera.append(teste[:]) #Faz uma cópia completa da lista teste dentro da lista galera
teste[0] = 'Luana'
teste[1] = 24
galera.append(teste[:]) #Faz uma cópia completa da lista teste dentro da lista galera
teste[0] = 'Joice'
teste[1] = 24
galera.append(teste[:]) #Faz uma cópia completa da lista teste dentro da lista galera
print(galera[3])
for pessoa in galera: #Para cada pessoa [Entrada 0] dentro da lista galera
    print(f' {pessoa[0]} tem {pessoa[1]} anos de idade') #Printa a posição 0 das listas com o nome da pessoa
    #e o valor [1] printa a idade da pessoa dentro das listas
#=====================================================================================================
gal = list()
dad = list()
totmai = totmen = 0

for c in range(0, 3):
    dad.append(str(input('Nome: ' )))
    dad.append(int(input('Idade: ')))
    gal.append(dad[:])
    dad.clear()
print(gal)

for pessoa in gal:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade')
        totmai += 1
    if pessoa[1] < 18:
        print(f'{pessoa[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} pessoas maiores de idade')
print(f'Temos {totmen} pessoas menores de idade')



# [:] é uma cópia completa de todos os valores do teste