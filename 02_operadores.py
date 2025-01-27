#Operadores

#Aritmeticos
#suma
print(3 + 4)

#resta
print(3 - 4)

#multiplicacion
print(3 * 4)

#division
print(3 / 4)

#modulo, es el resto de la division, para el multiplo de un numero
print(10 % 2)

#division pero aproximada a un numero entero, lo redondea
print(10 // 3)

#exponente
print(3 ** 2)

#el mas tambien concatena cadenas
print('Hola' + 'Python')

#esto da error
#print('Hola' + 2)
#pero este no, imprime Hola2 porque el numero esta en string
print('Hola' + str(2))

#prioridad en las operaciones
print(2 ** 3 + 3 - 7 / 1 // 4) #da 10

#con * se multiplica el String la cantidad de veces que dice el numero
print('Hola' * 2) #el numero debe ser entero, sino, no funciona


#Operadores Comparativos
#devuelven True o False
print(10 > 2) #mayor
print(10 < 2) #menor
print(10 >= 2) #mayor o igual
print(10 <= 2) #menor o igual
print(10 == 2) #igual igual
print(10 != 2) #Distinto
print(10 > 2 == 4) 

print('Hola' > 'Python') #False
print('Hola' < 'Python') #True, no es por los caracteres, compara la posicion de las letras, ordenamiento alfabetico
print('Hola' >= 'Python') #False
print('Hola' <= 'Python') #True
print('Hola' == 'Python') #False
print('Hola' != 'Python') #True


#Operadores Lógicos and, or y not. Se pueden concatenar todos los que necesite
print(3 > 4 and 'Hola' > 'Python')
print(3 > 4 or 'Hola' > 'Python')
print(3 < 4 and 'Hola' < 'Python')
print(3 < 4 or 'Hola' > 'Python')
print(not(3 > 4)) #niego toda la condición, el Falso se convierte en Verdadero y viceversa



