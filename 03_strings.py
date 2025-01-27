#Strings
my_string = 'Mi String'
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

#concatenar
print(my_string + ' ' + my_other_string)

#pueden llevar ciertos caracteres
my_new_line_string = 'Este es un String \ncon salto de linea'
print(my_new_line_string)

#con tabulacion
my_tab_string = '\tEste es un String con tabulacion'
print(my_tab_string)

my_scape_string = '\tEste es un String \n escapado'
print(my_scape_string)


#Formatear strings
name, surname, age = 'Gabriela', 'Rossi', 28
print('Mi nombre es Gabriela Rossi')
print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age)) #para que imprima tal cual
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age)) #s para string y d para numeros, aca el dato esta formateado

#inferencia de datos
print(f'Mi nombre es {name} {surname} y mi edad es {age}') #la mejor para imprimir datos tal cual
#la f formatea y va inferiendo los valores de las variables

#desempaquetado de caracteres
lenguaje = 'Python'
a, b, c, d, e, f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


#Division
lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice) #muestra y t

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice) #muestra ython

lenguaje_slice = lenguaje[-2]
print(lenguaje_slice) #muestra o

lenguaje_slice = lenguaje[1:2:4]
print(lenguaje_slice) #muestra la y

lenguaje_slice = lenguaje[0:6:2] #evita caracteres, no los muestra
print(lenguaje_slice) #muestra pto caracter 0, 2 y 4, un rango y me quedo solo con lo importante

#Reverse
reversed_lenguaje = lenguaje[::-1]
print(reversed_lenguaje) #lo imprime al reves nohtyP

#metodos o funciones del sistema
print(lenguaje.capitalize()) #pone la primer letra en mayuscula
print(lenguaje.upper()) #todas las letras en mayus
print(lenguaje.count('t')) #cuenta cuantas t
print(lenguaje.isnumeric()) #False
print('1'.isnumeric())#True
print(lenguaje.lower()) #todas a minusculas
print(lenguaje.upper().isupper()) #de mayusculas todas y verifico si estan en mayus con el is upper
print(lenguaje.startswith('Py')) #python empieza con py? True