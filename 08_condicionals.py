#Condicionales
#si se cumple una condicion, ejecuta lo que esta dentro de la condicion

my_condition = False #habia True

if my_condition: #if my_condition == True, es lo mismo pero redundante
    print('Se ejecuta la condición del if')#se ejecuta con T, con F no se imprime

print('La ejecucion continua')#esta tambien con T y con F

my_condition = 5 * 2

if my_condition == 11: #cuando le paso un valor, no se ejecuta
    print('Se ejecuta la condicion del segundo if') #se ejecuta si no tiene una igualdad arriba

print('La ejecucion continua')

#if my_condition == 10:
    #print('Se ejecuta el segundo if')

#print('La ejecucion continua')

#if my_condition > 10:
    #print('Se ejecuta el segundo if')

#print('La ejecucion continua')

#con if se ejecuta cuando es true

#si la ejecucion no se cumple..
if my_condition > 10:
    print('Es mayor que 10')
else: #si no se cumple lo de arriba, hace esto
    print('Es menor o igual que 10')

print('La ejecucion continua')

#mas de una condicion
my_condition = 5 * 5
if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20')
else:
    print('Es menor o igual que 10 o mayor igual que 20')


#elif, else if, necesita condicion al igual que if
my_condition = 1
if my_condition == 10:
    print('Se ejecuta la condicion del primer if, vale 10')
if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20')
elif my_condition == 1:
    print('Es 1')
else:
    print('Es menor o igual que 10 o meyor o igual que 20')

print('Continua la ejecucion')

my_string = ''
if my_string:
    print('Mi cadena de texto es vacia') #no imprime porque string vacio es como False

if not my_string:
    print('mi cadena de texto es vacia') #imprime porque la cadena esta vacia, porque comprueba que no este vacia, pero como tiene un not, comprueba que no tenga contenido


my_string = 'Mi cadena de texto'
if my_string: #sin igualdad porque comprueba que se cumpla my_string
    print('Tengo cadena de texto') #imprime

if my_string == 'Mi cadena de texto':
    print('Muestro porque coincide la cadena de texto') #imprime

if my_string == 'Mi cadena de textoooooooo':
    print('Esta cadena de texto coincide') #no imprime


