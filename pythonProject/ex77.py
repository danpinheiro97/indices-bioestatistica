vogais = ('a', 'e', 'i', 'o' , 'u') #Fonte de onde sai as Vogais
palavras = 'amor', 'cuidado', 'jantar', 'menina', 'girl' #Palavras para serem retiradas as consoantes
for pos in range(0, len(palavras)): # Para pos no tamanho da tupla palavras, ou seja, pos vai de 0 até 4
    print(f'Na palavra {palavras[pos]}: ', end='') # Pega os valores da tupla, end para pular linha
    for letra in palavras[pos]: # Vai criar uma função de leitura de letras nas palavras da posição do for acima
        if letra in vogais: #Se alguma letra das palavras estiver na fonte de onde sai as vogais
            print(letra, end=' ') #Printa as letras, ou seja, vogais na palavra
    print('') #Final para o end do print acima não desconfigurar tudo
