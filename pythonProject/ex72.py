stop = ''
while stop != 'N':
    ext = 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
    num = int(input('Entre com um valor entre 1 e 20: '))
    if num > 20 or num < 1:
        continue
    print(ext[num - 1])
    stop = str(input('Você deseja continuar? [S/N] ')).upper().strip()
