pessoas = {'nome': 'Daniel', 'Idade': 23, 'Sexo': 'M'}
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')
for k in pessoas.keys(): #Laço para verificar as keys
    print(k)
for v in pessoas.values(): #Laço para verificar os valores
    print(v)
for k, v in pessoas.items(): #Laço para verificar as keys e os valores
    print(f'{k} = {v}')
del pessoas['Sexo']
print(pessoas)
pessoas['nome'] = 'Leandro'
print(pessoas)
pessoas['peso'] = 55
print(pessoas)

brasil = []
estado1 = {'UF': 'Mato Grosso', 'Sigla':'MT'}
estado2 = {'UF': 'Mato Grosso do Sul', 'Sigla': 'MS'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(f' {brasil[1]["UF"]}')

estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) #Faz o fatiamento e copia o dicionário para dentro da lista
for e in brasil:
    print(e) #Printa o dicionário dentro de Brasil
    for k, v in e.items(): #Analisa as Keys e os valores dentro do (e) aberto acima
        print(f'O campo {k} tem o valor {v}') #Printa as chaves e os valores dentro de (e) estados acima