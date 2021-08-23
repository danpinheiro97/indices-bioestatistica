def mensagem(msg):
    print('=' *len(msg))
    print(msg)
    print('='* len(msg))


def linha():
    print('=' * 50)


from datetime import datetime
from math import log
resultadosshanon = list()
resultadosshanonf = list()
resultadosimpson = list ()
resultadosimpsonf = list()
simpson2 = 0

mensagem(f'Olá Biólogo, estou aqui para facilitar a sua vida.')

while True:
    print(f'''MENU DE OPÇÕES:
[  1  ]ÍNDICE DE SHANNON
[  2  ]ÍNDICE DE SIMPSON
[  3  ]ÍNDICE DE SHANNON E SIMPSON - SIMULTÂNEO
[  4  ]RESULTADOS
[  5  ]APRENDA A USAR O PROGRAMA!''')
    opc = int(input('Qual opção você deseja?'))
    if opc == 1:
        linha()
        print(f'Você escolheu a opção {opc} \nÍNDICE DE SHANNON')
        comunidades = list()
        shanon = list()
        shanon2 = list()
        cont = 0
        contp = 0
        maior = 0
        menor = 0
        nmaior = ''
        nmenor = ''
        while True:
            comunidade = dict()
            espec = list()
            comunidade['Comunidade'] = int(input('Identifique a Comunidade (nº): '))
            especies = int(input(f'Quantas espécies há na comunidade {comunidade["Comunidade"]}? '))
            comunidade['Total de Espécies'] = especies
            for c in range(0, especies):
                espec.append(int(input(f'Qual é o número de indivíduos (Ni) da espécie {c+1}: ')))
                cont += 1
            comunidade['Ni das espécies'] = espec[:]
            comunidade['Total de indivíduos'] = sum(espec)
            comunidades.append(comunidade.copy())
            stop = str(input('Continuar? [S/N]  '))
            if stop in 'Nn':
                break
        for c in range(0, len(comunidades)):
            somap = 0
            for d in range(0, len(comunidades[c]['Ni das espécies'])):
                if comunidades[c]['Ni das espécies'][d] > 0:
                    pi = (comunidades[c]['Ni das espécies'][d])/(comunidades[c]['Total de indivíduos'])
                    logi = log(pi)
                    pi2 = pi *log(pi)
                    somap += pi2
            shanon.append(-somap)
            shanon2.append(shanon[:])
            shanon.clear()
        linha()
        print(f'{"COMUNIDADE":<4}{"SHANNON":>20}')
        for i, v in enumerate(shanon2):
            print(f'{i+1:>5}',end ='')
            for d in v:
                print(f'{str(d):>36}')
        linha()
        for i, v in enumerate(shanon2):
            if i == 0:
                maior = v
                menor = v
                nmaior = i
                nmenor = i
            if v > maior:
                maior = v
                nmaior = i
            if v < menor:
                menor = v
                nmenor = i
        print(f'O maior Shannon é {maior} -> Comunidade {nmaior+1}...MAIOR DIVERSIDADE...')
        print(f'O menor Shannon é {menor} -> Comunidade {nmenor+1}...MENOR DIVERSIDADE...')
        resultadosshanon.append(f'Shannon: O maior Shannon é {maior} e pertence a comunidade {nmaior+1}')
        resultadosshanon.append(f'O menor Shannon é {menor} e pertence a comunidade {nmenor+1}')
        resultadosshanonf.append(resultadosshanon[:])
        resultadosshanon.clear()
    if opc == 2:
        scomunidades = list()
        simpson = list()
        simpson2 = list()
        cont = 0
        smaior = 0
        smenor = 999
        snmaior =''
        snmenor=''
        soman = 0
        while True:
            scomunidade = dict()
            sespec = list()
            scomunidade['Comunidade'] = int(input('Identifique a comunidade (nº)'))
            sespecies = int(input(f'Quantas espécies há na comunidade {scomunidade["Comunidade"]}? '))
            scomunidade['Total de espécies'] = sespecies
            for e in range(0, sespecies):
                sespec.append(int(input(f'Qual é o número de individuos (Ni) da espécie {e+1}? ')))
                cont +=1
            scomunidade['Ni das espécies'] = sespec[:]
            scomunidade['Total de indivíduos'] = sum(sespec)
            scomunidades.append(scomunidade.copy())
            stop = str(input('Continuar? [S/N] '))
            if stop in 'Nn':
                break
        for c in range (0, len(scomunidades)):
            ssomap = 0
            for d in range(0, len(scomunidades[c]['Ni das espécies'])):
                if scomunidades[c]['Ni das espécies'][d] > 0:
                  pi = scomunidades[c]['Ni das espécies'][d]/ scomunidades[c]['Total de indivíduos']
                  pi2 = pi**2
                  ssomap += pi2
                  simp = 1 - ssomap
                  simpf = simp
            simpson.append(simpf)
            simpson2.append(simpson[:])
            simpson.clear()
        linha()
        print(f'{"COMUNIDADE":<4}{"SIMPSON":>32}')
        for i, v in enumerate(simpson2):
            print(f'{i + 1:>5}', end='')
            for d in v:
                print(f'{str(d):>36}')
            print()
        linha()
        for i, v in enumerate(simpson2):
            if i == 0:
                smaior = v
                smenor = v
                snmaior = i
                snmenor = i
            if v > smaior:
                smaior = v
                snmaior = i
            if v < smenor:
                smenor = v
                snmenor = i
        print(f'O maior Simpson é {smaior} -> Comunidade {snmaior + 1}...MAIOR DIVERSIDADE...')
        print(f'O menor Simpson é {smenor} -> Comunidade {snmenor + 1}...MENOR DIVERSIDADE...')
        resultadosimpson.append(f'Simpson: O maior simpson é {smaior} e pertence a comunidade {snmaior+1}')
        resultadosimpson.append(f'Simpson: O menor simpson é {smenor} e pertence a comunidade {snmenor+1}')
        resultadosimpsonf.append(resultadosimpson[:])
        resultadosimpson.clear()
    if opc == 3:
        from math import log
        comunidades = list()
        shanon = list()
        shanon2 = list()
        cont = 0
        contp = 0
        maior = 0
        menor = 0
        nmaior = ''
        nmenor = ''
        while True:
            comunidade = dict()
            espec = list()
            comunidade['Comunidade'] = int(input('Identifique a Comunidade (nº): '))
            especies = int(input(f'Quantas espécies há na comunidade {comunidade["Comunidade"]}? '))
            comunidade['Total de Espécies'] = especies
            for c in range(0, especies):
                espec.append(int(input(f'Qual é o número de indivíduos (Ni) da espécie {c + 1}: ')))
                cont += 1
            comunidade['Ni das espécies'] = espec[:]
            comunidade['Total de indivíduos'] = sum(espec)
            comunidades.append(comunidade.copy())
            stop = str(input('Continuar? [S/N]  '))
            if stop in 'Nn':
                break
        for c in range(0, len(comunidades)):
            somap = 0
            for d in range(0, len(comunidades[c]['Ni das espécies'])):
                if comunidades[c]['Ni das espécies'][d] > 0:
                    pi = (comunidades[c]['Ni das espécies'][d]) / (comunidades[c]['Total de indivíduos'])
                    logi = log(pi)
                    pi2 = pi * log(pi)
                    somap += pi2
            shanon.append(-somap)
            shanon2.append(shanon[:])
            shanon.clear()
        linha()
        print(f'{"COMUNIDADE":<4}{"SHANNON":>20}')
        for i, v in enumerate(shanon2):
            print(f'{i + 1:>5}', end='')
            for d in v:
                print(f'{str(d):>36}')
        linha()
        for i, v in enumerate(shanon2):
            if i == 0:
                maior = v
                menor = v
                nmaior = i
                nmenor = i
            if v > maior:
                maior = v
                nmaior = i
            if v < menor:
                menor = v
                nmenor = i
        print(f'O maior Shannon é {maior} -> Comunidade {nmaior + 1}...MAIOR DIVERSIDADE...')
        print(f'O menor Shannon é {menor} -> Comunidade {nmenor + 1}...MENOR DIVERSIDADE...')
        resultadosshanon.append(f'Shannon: O maior Shannon é {maior} e pertence a comunidade {nmaior + 1}')
        resultadosshanon.append(f'O menor Shannon é {menor} e pertence a comunidade {nmenor + 1}')
        resultadosshanonf.append(resultadosshanon[:])
        resultadosshanon.clear()

        simpson = list()
        simpson2 = list()
        cont = 0
        smaior = 0
        smenor = 999
        snmaior = ''
        snmenor = ''
        soman = 0
        for c in range(0, len(comunidades)):
            ssomap = 0
            for d in range(0, len(comunidades[c]['Ni das espécies'])):
                if comunidades[c]['Ni das espécies'][d] > 0:
                    pi = comunidades[c]['Ni das espécies'][d] / comunidades[c]['Total de indivíduos']
                    pi2 = pi ** 2
                    ssomap += pi2
                    simp = 1 - ssomap
                    simpf = simp
            simpson.append(simpf)
            simpson2.append(simpson[:])
            simpson.clear()
        linha()
        print(f'{"COMUNIDADE":<4}{"SIMPSON":>32}')
        for i, v in enumerate(simpson2):
            print(f'{i + 1:>5}', end='')
            for d in v:
                print(f'{str(d):>36}')
            print()
        linha()
        for i, v in enumerate(simpson2):
            if i == 0:
                smaior = v
                smenor = v
                snmaior = i
                snmenor = i
            if v > smaior:
                smaior = v
                snmaior = i
            if v < smenor:
                smenor = v
                snmenor = i
        print(f'O maior Simpson é {smaior} -> Comunidade {snmaior + 1}...MAIOR DIVERSIDADE...')
        print(f'O menor Simpson é {smenor} -> Comunidade {snmenor + 1}...MENOR DIVERSIDADE...')
        resultadosimpson.append(f'Simpson: O maior simpson é {smaior} e pertence a comunidade {snmaior + 1}')
        resultadosimpson.append(f'Simpson: O menor simpson é {smenor} e pertence a comunidade {snmenor + 1}')
        resultadosimpsonf.append(resultadosimpson[:])
        resultadosimpson.clear()
    if opc == 4:
        for k, v in enumerate(resultadosimpsonf):
            print(f'{v}')
        for k, v in enumerate(resultadosshanonf):
            print(f'{v}')
    if opc ==5:
        hoje = datetime.now()
        print(f'Olá, hoje é {hoje}, meu nome é Daniel Pinheiro, e estou aqui para sanar suas dúvidas!')
        print('''MENU DE OPCÕES
[  1  ] O QUE É INDICE DE SHANNON?
[  2  ] O QUE É ÍNDICE DE SIMPSON?
[  3  ] VOLTAR AO MENU PRINCIPAL''')
        while True:
            opc2 = int(input('Qual opção você deseja? '))
            if opc2 == 1:
                mensagem('ÍNDICE DE SHANNON')
                print('''O índice de Shannon é um dos diversos índices da diversidade usados para medir a diversidade em dados categóricos.
A vantagem deste índice é que ele leva em consideração o número das espécies e as espécies dominantes''')
            if opc2 ==2:
                mensagem('ÍNDICE DE SIMPSON')
                print('''''')
            if opc2 ==3:
                break
