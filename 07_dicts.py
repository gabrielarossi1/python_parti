#diccionarios almacena datos del tipo clave-valor
#tiene par clave-valor

my_dict = dict() #constructor
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Nombre':'Gabriela', 'Apellido': 'Rossi', 'Edad':28, 1:'Python'}
my_dict = {
    'Nombre':'Gabriela', 
    'Apellido': 'Rossi', 
    'Edad':28, 
    'Lenguajes':{'Python', 'Swift', 'Kotlin'},
    1 : 1.62
    }

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))#4 claves a sus valores
print(len(my_dict))#5 elementos porque hay 5 pares clave-valor, cuenta las claves, por mas que tenga muchos valores adentro

print(my_dict['Nombre']) #muestra el valor de la clave que le pasamos
#son de facil acceso
my_dict['Nombre'] = 'Pedro' #cambio el nombre
print(my_dict['Nombre'])

my_dict['Calle'] = 'Roque Peña' #le agrego otra clave-valor
print(my_dict['Calle']) 

#no tiene remove asique implementamos del
del my_dict['Calle']
print(my_dict) #borro la calle y muestra todo menos eso

print('Rossi' in my_dict) #False, se busca por cable, no por valor
print('Gabriela' in my_dict) #False, idem

print('Apellido' in my_dict) #True porque esta la clave apellido
print('Hola' in my_dict) #no da error, da false, porque no esta la clave Hola

#operaciones
print(my_dict.items()) #muestra todo el diccionario
print(my_dict.keys()) #muestra las claves, en formato lista
print(my_dict.values()) #muestra los valores, en formato lista
print(my_dict.fromkeys(('Nombre', 1))) #da none porque las claves no tiene valor
print(my_other_dict.fromkeys(('Nombre', 1))) #da none, las claves no tienen valor

my_new_dict = my_other_dict.fromkeys(('Nombre', 1, 'Piso')) #se crea un diccionario nuevo sin valores
print(my_new_dict)#sique dando none porque esta vacio el diccionario

my_list = ['Nombre', 1, 'Calle'] #creo una lista
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict= dict.fromkeys((('Nombre', 1, 'Piso'))) #lo hago diccionario
print(my_new_dict)

my_new_dict= dict.fromkeys(my_dict) #Copia del diccionario pero solo con las claves
print(my_new_dict) #los valores vienen vacions, None

my_new_dict= dict.fromkeys(my_dict, ('Gabriela', 'Rossi')) #le metemos estos valores a todas las claves
print(my_new_dict)
my_new_dict= dict.fromkeys(my_dict, my_dict) #cada elemento ahora tiene el diccionario completo, cada clave tiene como valor todo el diccionario
print(my_new_dict)
my_new_dict= dict.fromkeys(my_dict, ['Gabriela', 'Rossi']) #ahora le paso una lista 
print(my_new_dict) #pero sigue estando esta lista como valor de cada clave
#no se puede agregar un valor a una clave en particular, salvo que se acceda a esa clave, como se hizo al principio
#de esta forma solo mete los valores que paso a todas las claves

print(list(my_new_dict)) #lo transformo en una lista pero solo trae las claves
print(tuple(my_new_dict)) #tupla solo trae las claves
print(set(my_new_dict)) #set trae las claves desordenadas

my_values = my_new_dict
print(type(my_values)) #retorna dict

