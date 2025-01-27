#consultar el tipo de dato
print(type('Hola Mundo!')) #type para saber el tipo de dato
#el tipo es str (string)
print(type(5)) #entero
print(type(2.5)) #flotante
print(type(True)) #booleano
print(type(1 + 2j)) #numero complejo


#variables
#minusculas y con _ de separacion
my_string_varible = 'My String Variable'
print(my_string_varible)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#concatenacion de variables en un print
#imprimir todo junto, con comas entre las variables
print(my_string_varible, my_int_variable, my_bool_variable)

#funcion del sistema, de las reservadas de python y estan pre cargadas
print(len(my_string_varible))
#cuenta el largo de este string

#los prints pueden recibir parametros
print('Este es el valor de: ', my_bool_variable)

#variables en una sola linea
name, surname, alias, age = 'Gabriela', 'Rossi', 'Gabu', 28
print('Me llamo: ', name, surname,'Mi edad es:', age, 'Mi alias es:', alias)

#input
#firts_name = input('What is your name? :')
#print(firts_name)

#las variables pueden cambiar su tipo de datos
name = 28
age = 'Gabriela'
print(name)
print(age)
#como no es de tipado fuerte, se puede hacer esto

#forzamos el tipo? No
adress: str = 'Mi direccion'
adress: int = 32
print(type(adress))

#En python no hay muchos tipos de datos