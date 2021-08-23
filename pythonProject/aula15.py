n = 0
s= 0
while True:
    n = int(input('Entre com um valor '))
    if n == 999:
        break
    s = s + n
print(f'\033[34mA soma dos seus valores é : \n{s}\033[36m')