def mensagem(msg):
    print('-' *len(msg))
    print(msg)
    print('-'*len(msg))

while True:
    mensagem(str(input('Entre com sua mensagem: ')))