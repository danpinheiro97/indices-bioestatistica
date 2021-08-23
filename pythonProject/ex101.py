def voto(ano):
    from datetime import datetime
    hoje = datetime.now().year
    idade = hoje - ano
    falt = 17 - idade
    falto = 18 - idade
    if idade >= 18 and idade < 65:
        return f'Você tem {idade} anos e portanto o voto é Obrigatório'
    if idade >=17 and idade < 18:
        return f'Você tem {idade} anos e portante o voto é opcional'
    if idade > 65:
        return f'Você tem {idade} anos e portanto o voto é opcional'
    if idade < 17:
        return f'Você tem {idade} anos e portanto não vota, faltam {falt} anos para o voto ser opcional e {falto} anos para o voto ser obrigatório '
while True:
    nasc = int(input('Ano de nascimento: '))
    print(voto(nasc))



#Quantos anos falta para a pessoa votar?
#Quantos anos para votar e quantos anos ela tem = 17 - idade





