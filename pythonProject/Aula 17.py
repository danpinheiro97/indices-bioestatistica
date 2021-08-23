#Aula listas
#Listas ao contrário de tuplas são mutáveis
#Para iniciar uma lista usar []

#Métodos em listas:

#lista = ['Sorvete', 'Maça', 'Banana', 'Categoria']
#Substituir = lista[posição] = valor
#Adicionar = lista.append('valor') - dessa forma ele adiciona no fim da lista
#Adicionar = lista.insert(posição, 'valor') - dessa forma ele adiciona na posição definida
#deletar = lista.pop(posição) or () - o pop sozinho elimina o ultimo valor, mas pode definir uma posição ()
#deletar = lista.remove(valor)]
#Classificar = list.sort() - Organiza a lista
#Classificar ao contrário = list.sort(reverse=True)
#Contar elementos = len(listas)

#usando os métodos com if
#if 'valor' in lista:
    #lista.remove('valor')

#Comando list() inicia uma lista a partir de sua entrada.
# valores = list(range(4,11))

num = [1,3,5,7,0,9,8,2]
print(num)
num[2] = 4
print(num)
num.append(56)
print(num)
num.insert(5, 'banana')
print(num)
num.pop()
print(num)
num.remove('banana')
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(len(num))