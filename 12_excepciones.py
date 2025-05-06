#exception handling
#manejo de errores

numberOne, numberTwo = 5, 1
numberTwo = '1'

#try except
#try:
    #print(numberOne + numberTwo)
    #print('No se ha producido un error')
#except:
    #print('Se ha producido un error')

#try except else finally. try excep siempre, los otros 2 son opcionales
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except:
    print('Se ha producido un error')
else: #se ejecuta solo si no entra en el except
    print('La ejecucion continua correctamente')
finally: #se ejecuta SIEMPRE pase lo que pase
    print('La ejecucion continua')


#captura de excepciones por tipo
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError: #solo se ejecuta si se produce errores value, por eso se rompe
    print('Se ha producido un ValueError')
except TypeError: 
    print('Se ha producido un TypeError')#solo se ejecuta si se produce type error


#captura de la informacion de la excepcion
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError as error: #error porque e un error pero puedo poner cualquier cosa
    print(error)
except Exception as error: #error generico, error es una variable
    print(error)

