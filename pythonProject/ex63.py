n = 0
f = 0
cont =0
num = int(input('Entre com um valor inteiro: '))
while num != cont:
  print(f, end=' - ')
  f = f + n
  n = f - n
  cont += 1
  if f ==0:
    f = f +1
print('Over')

  # O valor 3 é o resultado da soma do valor 1 e 2