#Sets
#tiene un array, no es una estructura ordenada, funciona como un diccionario

my_set = set() #creacion
print(type(my_set)) #aca dice que es un set

my_other_set = {}
print(type(my_other_set)) #aca dice que es un diccionario

my_other_set = {'Gabriela', 'Rossi', 28}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('Pepas')
print(my_other_set) #lo agrega al principio, por lo que no es una estructura ordenada

