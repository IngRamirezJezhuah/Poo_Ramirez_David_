
#def saludar(nombre):#parametro adentro se pone el argumento que se llama
#    print("hola:",nombre)
#    saludar(str(input("dame tu nombre:")))
#saludar()

#def nombreFuncion(parametros):
#cuerpo de la funcion 
#nombreFUNCION(argumentos)


def sumar(a,b):
    suma = a+b
    return suma
    #aqui es el resultado en cualquier parte puedo llamar la funcion
    #sirve para administar los valores
resultado = sumar(5,3)#aqui se esta poniendo en una variable
print(resultado)#esta llama la definicion


#ef nombreFuncion(parametros=valor):
#resutado = operacionS
#return resultado

def sumarvar1(a=5,b=7):
    suma = a+b
    return suma
    #aqui es el resultado en cualquier parte puedo llamar la funcion
    #sirve para administar los valores
resultado = sumarvar1()#aqui se esta poniendo en una variable
print(resultado)#esta llama la definicion

#def nombreFuncion(parametros):
#resultado = operacion
#return resultado
def sumarvar2(a,b):
    suma = a +b
    return suma
    #aqui es el resultado en cualquier parte puedo llamar la funcion
    #sirve para administar los valores
resultado = sumarvar2(12,56)#aqui se esta poniendo en una variable
print(resultado)#esta llama la definicion
#sumarvar2()
#•¿Quéson y para quésirven las funciones?
#•Estructura básica de las funciones (definición y llamar)
#•Diferencias de printy return