# Clases
#debe tener logica al objeto que hace referencia
#las clases se escriben con CamelCase

class MyEmptyPerson:
    pass

#las clases pueden ir con () o sin
print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):  #siempre def init self porque es un constructor de clase
        #el alias se lo deje por defecto, si no se lo paso, no pasa nada
        #self.name = name
        #self.surname = surname
        
        #self.name = 'Gabriela'
        #self.surname = 'Rossi' 
        #con esto anda y no necesito pasarle parametros a person abajo porque ya lo defini aqui
        
        self.full_name = f'{name} {surname} ({alias})'
        #otra forma de hacer/usar. Pinto alias con () pero puedo ponerle * si quiero

    def walk (self): #funcion dentro de la clase
        print(f'{self.full_name} Está caminando')


my_person = Person('Gabriela', 'Rossi')
#print(my_person.name)  #muestra gabriela
#print(f'{my_person.name} {my_person.surname}') #muestra gabriela rossi

#dejo la variable con los valores para lo del full_name
#print(my_person.full_name) y me muestra los datos
print(my_person.full_name)
my_person.walk()

my_other_person = Person('Pepe', 'Lopez', 'Pepito')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Hector de Leon (El loco de los perros)'
print(my_other_person.full_name)
