from datetime import datetime
nome = str(input('Nome: '))
ano = int(input('Ano de Nasccimento [XXXX]'))
hoje = datetime.today()
anoa = hoje.year
idade = anoa - ano
ctps = int(input('Carteira de Trabalho: (0) = Não tenho '))
if ctps == 0:
    ficha = {'Nome': nome, 'Idade': idade, 'CTPS': ctps}
    for k, v in ficha.items():
        print({f'{k}: {v}'})
elif ctps != 0:
    anoc = int(input('Ano de Contratação: [XXXX} '))
    sal = int(input('Salário: R$ '))
    aposen = 65 - idade
    aposentem = anoc +30
    ficha = {'Nome': nome, 'Idade': idade, 'CTPS': ctps,
         'Contratação': anoc, 'Sálario': f'R${sal},00',
         'Aposentadoria por idade': f'Faltam  {aposen} anos', 'Ano de Aposentadoria por Tempo de Serviço:':aposentem}
    for k, v in ficha.items():
        print(f'{k}: {v}')