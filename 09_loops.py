#loops, bucles, ciclos
#sirve para iterar, intentar repetir algo, pasar por el mismo codigo varias veces

# while, hay que pasarle una condicion, mientras sea true que haga algo
#es como una especie de if
#se repite siempre que se cumple la condicion

my_condition = 0
#while my_condition < 10:
    #print(my_condition) #muestra infinitamente el 0 porque no sale nunca del bucle
    #hace tantas vueltas porque nunca sale

#si lo incremento en cada vuelta
while my_condition < 10:
    print(my_condition)
    my_condition += 1 #con cada vuelta incremento 1 en my_condition y no tengo un bucle infinito
    #muestra del 0 al 9 y sale del bucle

print('La ejecucion continua')
print('####################')

while my_condition < 10:
    print(my_condition)
    my_condition += 1 
#if my_condition == 10: esto no se puede
    #print('Mi condicion es igual a 10')
#elif my_condition == 10: #este tampoco cuenta, porque while es if
    #print('Mi condicion es 10')
else: #pero este pertenece al while porue while es como if
    print('Mi condicion es mayor o igual que 10') #puedo agregarle un else al while

print('####################')

while my_condition < 20:
    my_condition += 1
    if my_condition == 15: #esta se cumple
        print('Mi condicion es 15')
        #si quiero que el bucle se interrumpa..
        print('Se detiene la ejecucion')
        break #fuerza el cierre del loops

    print(my_condition)

print('La ejecucion continua')
print('####################')

#bucle for, se repite e itera un elemento, se repite tantas veces como elementos tengamos iterables
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element) #imprime los elementos de la lista, esta atado a los elementos que le estamos indicando en la posible iteracion, la lista en este caso
print('####################')

my_tuple = (35, 1.77, 'Gabriela', 'Rossi', 'Gabriela')
for element in my_tuple:
    print(element)
print('####################')

my_set = {'Gabriela', 'Rossi', 28}
for element in my_set:
    print(element)

print('####################')
my_dict = {'Nombre':'Gabriela', 'Apellido':'Rossi', 'Edad':28, 1:'Python'}
for element in my_dict:
    print(element) #imprime claves
print('####################')

#para que imprime valores
for element in my_dict.values(): #puede tener otro nombre ademas de element, eso lo elijo yo
    print(element) #imprime los valores de cada clave
print('####################')

#en este caso solo imprimimos pero obviamente se buscan datos

#al igual que el while, puede tener else
for element in my_dict:
    print(element)
else:
    print('El bucle for para el diccionario ha finalizado')
print('####################')

#se puede detener el bucle for
for element in my_dict:
    print(element)
    if element == 'Edad': #encontro la clave edad
        break #y se detiene el for
    print('Se ejecuta') #imprime hasta llevar a edad y se rompe el bucle y se deja de mostrar
#elif element == 1: esto no se puede, deberia esta tabulado abajo del if en la misma linea
    #print('element vale 1') #de igual forma no se puede
else:
    print('El bucle for para el diccionario ha finalizado')  
#con el break se sale completamente del for   
print('####################')   

#no se aconseja el continue, es como una mala practica
for element in my_dict:
    print(element)
    if element == 'Edad': #encontro la clave edad, este continue seria como un else a la misma altura que el if, pero este si te deja usarlo
        continue #sigue, pero puede ser una condicion, es una palabra reservada
    print('Se ejecuta') #pero luego de edad no imprime este print, ahi se rompe pero vuelve al for desde el princio, es una especie de break pero detiene la ejecucion en ese punto
else:
    print('El bucle for para el diccionario ha finalizado')  
#continua el ciclo
print('####################')
