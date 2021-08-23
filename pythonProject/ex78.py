valores = [int(input('Entre com um valor')), int(input('Entre com um valor')), int(input('Entre com um valor')), int(input('Entre com um valor')), int(input('Entre com um valor'))]
print(f'O maior valor é o {max(valores)} e está na posição {valores.index(max(valores)) +1}')
print(f'O menor valor é o {min(valores)} e está na posição {valores.index(min(valores)) +1}')