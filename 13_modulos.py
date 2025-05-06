#modules
#un modulo es un codigo externo, en otro fichero
#basicamente evitamos replicar codigo

#para acceder a otros ficheros
#import module
#from module import sum
#from module import printValue
from module import sumValue, printValue

#from 10_functions import sum_two_values da error porque esta nomemclatura no es valida para los modulos
#no pueden estar encabezados por un numero, los _ si son validos
#aparte de importarlo, uso module. las funciones que quiero
#module.sum(3, 2, 5) #de esta forma si importo el modulo entero

#module.printValue('Hola python') #solo traigo esta funcion

sumValue(2, 3, 5) #de esta forma si hago from
printValue('Hola Python')

import math
print(math.pi)
print(math.pow(2,8))

from math import pi as PI_VALUE #le cambio el nombre a pi
#print(pi) #error porque lo renombre
print(PI_VALUE)