#Funciones
#se encapsula logica dentro de ella, resuelve un problema muy concreto que le indicamos, evitamos errores y no duplicamos codigo

def my_function(): #centralizo la operacion aqui
    print('Esto es una funcion')

my_function() #llamo la funcion definida y puedo llamarla las veces que necesite

#ademas puede devolver y recibir codigo

def sum_two_values(first_number, second_number): #en los () van parametros
    print(first_number + second_number)

sum_two_values(5, 7) #paso los argumentos
sum_two_values(54700, 37288)
sum_two_values('5', '7') #concatena las cadenas de texto
sum_two_values(1.4, 5.2)

#def sum_two_values_new(first_value, second_value):
    #print(first_value + second_value)

#sum_two_values_new(3, 55)

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f'{name} {surname}')

print_name('Gabriela', 'Rossi')
print_name(surname= 'Rossi', name='Gabriela') #cambio el orden
#print_name(surname='Rossi') #error, debo pasarle las dos

#parametros por defecto
def print_name_with_default(name, surname, alias = 'Sin alias'):
    print(f"{name} {surname} {alias}")

print_name_with_default('Gabriela', 'Rossi', 'Gabs')
print_name_with_default('Gabriela', 'Rossi')

def print_texts(*text): #el asterisco hace que puedas pasarle la cantidad de datos que quieras
    print(text)

print_texts('Hola', 'python', 'mundo')

def print_texts_new(*texts):
    for text in texts:
        print(text)

print_texts_new('Hola', 'python', 'mundo') #imprime como una lista de textos