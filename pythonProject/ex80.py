#Se c na primeira posição ou N for maior do que a ultima posição da lista[-1]
#Adiciona N na última posição
#Se não
#Abre um contador
 #Enquanto o valor do contador for menor do que o tamanho da lista
#Se o N for menor ou igual a lista[pos(contador]
#Inserir N na posição comparada acima
#Break
#Atualizar contador

lista = list()
for c in range (0, 5): #lAÇO DE REPETIÇÃO DE 5 VALORES
    n = int(input('Valor:')) #Input de entrada de valor
    if c == 0 or n > lista[-1]: #Se c na primeira posição ou n for maior que a ultima posição da lista
        lista.append(n) #Adiciona n na ultima posição
        print(f'Adicionado na última posição')
    else:
        cont = 0 #Abri um contador
        while cont < len(lista): #Enquanto o contador for menor do que o tamanho da lista
            if n <= lista[cont]: #Se o N for menor ou igual a posição cont da lista
                lista.insert(cont, n) #Inserir esse N na posição cont
                print(f'Adicionado na posição {cont}')
                break
            cont += 1
print(lista)
