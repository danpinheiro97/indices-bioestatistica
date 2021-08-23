#Aula tupla

#lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#print(sorted(lanche)) #Organiza em ordem alfabetica

#for cont in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[cont]} na posição {cont}') #Maneira com contagem

#for c in lanche:
    #print(f'Eu vou comer {c}') #maneira simples sem contagem

#for pos, comida in enumerate (lanche):
    #print(f'Eu vou comer {comida} na posição {pos}') #Maneira com contagem

a = 2, 5, 4
b = 5, 8, 1, 2
c = a+ b
print(sorted(c)) #Organiza em ordem
print(len(c)) #Tamanho da tupla
print(c.count(5)) #Conta quantas vezes o valor digitado se repete na tupla
print(c.index(5)) #Em qual posição está o valor digitado? #Deslocamento (c.index(5, 1)
                  # dessa forma ele pula o primeiro que contou


