def fator(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c>1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

f1 = fator(5)

print(fator(5, show=True))

