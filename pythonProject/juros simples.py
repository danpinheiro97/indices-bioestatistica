while True:
    val = int(input('Entre com o valor do empréstimo'))
    mes = int(input('Quantos meses até a quitação?'))
    print('Juros Simples: 10% a.m')
    for c in range(0, mes):
        juros = val * 0.10
        tot = val + (juros * mes)
    print(tot)
    cont = str(input('Você deseja continuar [S/N]?')).upper().strip()
    if cont == 'S':
        continue
    if cont == 'N':
        print('Programa encerrado')
        break

        # juro simples é acrescentar a taxa em cima do valor original