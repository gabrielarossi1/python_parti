#Listas, conjuntos de datos, tiene mas propiedades que los arrays
#tiene operaciones propias de las listas. El array no se puede modificar

#formas de listas
my_list = list() 
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [28, 1.62, 'Gabriela', 'Rossi'] #se pueden guardar datos de tipos diferentes

print(type(my_other_list)) #imprime que una lista

#acceso a la lista
print(my_other_list[0]) #el 0 es la primera posicion y muestra mi edad
print(my_other_list[-1]) #muestra el ultimo elemento de la lista
print(my_other_list[1])
print(my_other_list[-3])
print(my_other_list[-4])
#print(my_other_list[4]) #error
#print(my_other_list[-5]) #fuera de rango, es un error
print(my_other_list.count('Rossi')) #count retorna el numero de coincidencias de un valor
print(my_list.count(30)) #devuelve 2 porque hay dos numeros 30

#debo respetar la cantidad de elementos de la lista
age, height, name, surname = my_other_list #respeto el orden de la lista
print(name)

name, height, age, surname =my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name) 
print(age)


#suma de listas
print(my_list + my_other_list) #sumo 2 listas y queda como una sola en el orden con las que las concateno


#trabajar con los elementos de la lista, las listas son mutables
#operaciones con listas
my_other_list.append('Pepas') #agrega al final
print(my_other_list)

my_other_list.insert(1, 'Rosa') #agrega en la posicion indicada lo que quiero
print(my_other_list)

my_other_list.remove('Rosa')#borro rosa
print(my_other_list)

my_list.remove(30)
print(my_list) #solo elimina un numero 30

my_list.pop()
print(my_list) #elimina el ultimo elemento de la lista
#print(my_list.pop()) muestra lo que elimino

#my_list.pop(2) #elimina la segunda posicion
#print(my_list)
#print(my_list.pop(2))

#puedo guardar los elementos borrados en una variable
#my_pop_element = my_list.pop(2)
#print(my_pop_element)
#print(my_list)

del my_list[2] #elimino un elemento de la lista, elimina por indice
print(my_list)

my_list.clear
print(my_list) #borro todos los elementos de la lista

my_other_list.insert(1, 'Violeta') 
print(my_other_list)

my_new_list = my_list.copy() #la copio en una nueva variable
my_list.clear() #la limpio
print(my_list)
print(my_new_list)

my_new_list.reverse()#da vuelta los valores
print(my_new_list)

my_new_list.sort() #de mayor a menor, o orden alfabetico
print(my_new_list)

print(my_new_list[1:2]) #rebanadas de listas
print(my_new_list[1:3])

#tipos dinamicos
my_list = 'Hola Python' #deja de ser una lista y ahora es un string
print(my_list)
print(type(my_list)) #como es dinamico, van cambiando los datos de las variables

#si lo quiero como lista
#my_list = list('Hola Python') #con el constructor
#my_list = ['Hola Python'] #con los [ ] de las listas


