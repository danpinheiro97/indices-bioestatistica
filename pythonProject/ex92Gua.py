from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nasccimento [XXXX]'))
dados['Idade'] = datetime.now().year - ano
dados['CTPS'] = int(input('Carteira de Trabalho: (0) = Não tenho '))
if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: [XXXX} '))
    dados['Salário'] = int(input('Salário R$ '))
    dados['Aposentadoria'] = 65 - dados['Idade']
    dados['Aposentadoria Tempo de Serviço'] = (dados['Ano de Contratação'] +35) - datetime.now().year
for k, v in dados.items():
    print(f'{k}: {v}')