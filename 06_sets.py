#Sets
#tiene un array, no es una estructura ordenada, funciona como un diccionario
#y no admite repetidos
#ordena por un hash interno, no te asegura el orden en que se guarda

my_set = set() #creacion
print(type(my_set)) #aca dice que es un set

my_other_set = {}
print(type(my_other_set)) #aca dice que es un diccionario

my_other_set = {'Gabriela', 'Rossi', 28}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('Pepas')
print(my_other_set) #lo agrega al principio, por lo que no es una estructura ordenada

print('Rossi' in my_other_set) #realizar busquedas
print('Rossy' in my_other_set)

my_other_set.remove('Rossi') #elimino Rossi
print(my_other_set)

my_other_set.clear()
print(len(my_other_set)) #borre todos los elementos de mi set

del my_other_set #elimino la variable y no puedo printearla porque no esta definida

my_set = {'Gabriela', 'Rossi', 28}
my_list = list(my_set) #la creo como lista pero el set esta desordenada, asique mi lista va a quedar con ese orden
print(my_list)
print(my_list[0]) 

my_other_set = {'Kotlin', 'Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set)) #no muestra 12 elementos porque estan repetidos, no duplica elementos
print(my_new_set.union(my_new_set).union(my_set))

print(my_other_set.difference(my_set))
