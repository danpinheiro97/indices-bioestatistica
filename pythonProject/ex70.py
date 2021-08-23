keep = ''
soma = 0
cpc = 0
contp = 0
nomemenor = ''
nomemaior = ''
while keep != 'N':
    nm = str(input('Nome do Produto: ')).upper().strip()
    pc = int(input('Preço do produto R$: '))
    if keep != 'N':
        soma += pc
        contp += 1
    if pc >= 1000:
        cpc += 1
    if contp == 1:
        maior = pc
        menor = pc
        nomemaior = nm
    if contp > 1:
        if pc > maior:
            maior = pc
            nomemaior = nm
        if pc < menor:
          menor = pc
          nomemenor = nm
    keep = str(input('Você deseja continuar? [S/N] ')).upper().strip()
    if keep == 'N':
        print(f'O total gasto na compra foi R${soma},00\n{cpc} produtos custam mais de R$1.000,00\nO produto mais barato é {nomemenor} e custa R${menor},00')
        break



