#Dicionários
#Ao contrário das listas e das tuplas, os dicionários usam índices descritos por palavras e não números

#dados = dict() #Abre dicionário
dados = {'nome': 'Pedro', 'idade': 25} #O índice é 'nome' e 'idade'
print(dados['nome']) #printa o valor existente dentro do índice "nome"
print(dados['idade']) #printa o valor existente dentro do indice 'idade'
#Adicionar um novo elemento:
dados['sexo'] = 'M'
print(dados['sexo'])
#Remover elemento:
del dados['idade']
#Abrindo lista
filmes= {'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
filmes2= {'título': 'Staro Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

#Printar os valores dentro do dicionário
print(filmes.values()) #Pode utilizar nos laços
#printar os índices do dicionário
print(filmes.keys()) #pode utilizar nos laços
#Printar os valores e índices juntos:
print(filmes.items()) #pode utilizar nos laços
#Keys = Índice, Value = Valores dentro do índice
for k, v in filmes.items(): #Laço que vai pegar as keys e os valores dentro do método .items
    print(f'O {k} é {v}') #Printando K que são as Keys e o V que são os valores

locadora = list() #Abre a lista
locadora.append(filmes) #Acrescenta o dicionário dentro da lista
locadora.append(filmes2)
print(locadora[0]["ano"]) #Printa a lista na posição 0 e o valor da key: 'ano' dentro do dicionário
