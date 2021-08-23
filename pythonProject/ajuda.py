def contador(i, f, p):
    """
A função contador utiliza 3 parâmetros e joga eles dentro de um laço de repetição com limitador de
alcance.
for c = abre a função na variável (c), ou seja, c vai conter os números do contador
(i, f, p)
    :param i: Inicio
    :param f: Fim
    :param p: Passo
    :return:
    """
    for c in range(i, f+1, p):
        print(c, end=' ')


contador(100, -1, -1)
help(contador)

def soma(a=0, b=0, c=0):
    s = a+b+c
    print(s)


soma(1,2,3)
soma(5,5)
soma(11)
soma()