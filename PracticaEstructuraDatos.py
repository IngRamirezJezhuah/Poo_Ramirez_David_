#Actividad 4: Información de Contactos
#Crea una lista de tuplas donde cada tupla contiene el nombre, número de
#teléfono y correo electrónico de un contacto.
#Almacena esta lista en un diccionario donde la clave es el nombre del
#contacto.
#Crear un menú que permita al usuario agregar nuevos contactos, buscar un
#contacto por nombre, mostrar todos los contactos o salir.
#commit “Práctica de estructuras de datos”
InfoContac = {}

tuplita =("dj",6188230409,"david.jezhuha@gmail.com")
nombre,numTelf,correo = tuplita

while True:
    print("-------------------------------------------------")
    print("Hola buenvenido a la base de estudiantes")
    print("                ( ˶ˆ꒳ˆ˵ )")
    print("Favor de sellecionar lo que desee hacer")
    print(" (๑>؂•̀๑)  1.-Ingresar un nuevo alumno ")
    print("          2.-Revisar lista               (๑>؂•̀๑)")
    print("          2.-Salir                    (๑>؂•̀๑)")
    print("--------------------------------------------")
    print("       asi le salen los datos (｡- .•)")
    print("nombre:",nombre,"numerotelf:",numTelf,"correo:",correo)
    print("--------------------------------------------")
    op= int(input("Que deseas hacer"))

    if op == 1:
        print("(੭ ˊ^ˋ)੭recuerda el nombre con mayuscula la primera")
        IngrNombre = str(input("me podrias dar el nombre:"))
        print("(੭ ˊ^ˋ)੭ejemplo 111 111 111")
        IngrNum = int(input("me podrias dar el numero:"))
        print("(੭ ˊ^ˋ)੭recuerda usar el @gmail.com")
        IngrCorreo = str(input("me podrias dar el Correo elcetronico:"))
        InfoContac[IngrNombre] = (IngrNum,IngrCorreo)
        print(InfoContac)
    elif op == 2 :
            print(InfoContac)
    elif op == 3 :
        print("bye bye ૮ • ﻌ - ა ✩‧ ")
        break