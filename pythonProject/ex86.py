list1 = [[], [], []]
list2 = [[], [], []]
list3 = [[], [], []]

list1[0].append(int(input('Entre com um valor para [0,0] ')))
list1[1].append(int(input('Entre com um valor para [0,1] ')))
list1[2].append(int(input('Entre com um valor para [0,2] ')))
list2[0].append(int(input('Entre com um valor para [1,0] ')))
list2[1].append(int(input('Entre com um valor para [1,1] ')))
list2[2].append(int(input('Entre com um valor para [1,2] ')))
list3[0].append(int(input('Entre com um valor para [2,0] ')))
list3[1].append(int(input('Entre com um valor para [2,1] ')))
list3[2].append(int(input('Entre com um valor para [2,2] ')))

print(list1[0], end='')
print(list1[1], end='')
print(list1[2])
print(list2[0], end='')
print(list2[1], end='')
print(list2[2])
print(list3[0], end='')
print(list3[1], end='')
print(list3[2])
listac = list()
listac.append(list1[:])
listac.append(list2[:])
listac.append(list3[:])
print(listac)


