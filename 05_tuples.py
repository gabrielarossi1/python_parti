#Tuplas, son inmutables

my_tuple = tuple() #consturctor
my_other_tuple = () #tupla, conjunto de valores

my_tuple = (28, 1.62, 'Gabriela', 'Rossi')
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) error
#print(my_tuple[-6]) error

#tiene operaciones limitadas
print(my_tuple.count('Rossi')) #busca el valor, si esta, da 1
print(my_tuple.index('Rossi')) #da el indice de Rossi
print(my_tuple.index('Gabriela'))

#my_tuple[1] = 1.70 #da error porque no se pueden modificar los datos de las tuplas, son inmutables
#print(my_tuple)

#print(my_tuple + my_other_tuple) # se las puede sumar

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) #mi tupla ahora es una lista
print(type(my_tuple)) #

#my_tuple[4] = 'Pepas'
my_tuple.insert(1, 'Rosa')
#print(tuple(my_tuple)) 
my_tuple = tuple(my_tuple) #la vuelvo tupla de nuevo
print(my_tuple)
print(type(my_tuple))

#del my_tuple #borro toda la tupla, pero como es inmutable, no deberia borrarse, pero se borra
#print(my_tuple) #borra la variable, da no definida