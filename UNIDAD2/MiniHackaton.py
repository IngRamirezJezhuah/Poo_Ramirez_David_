lista= []

while True:
    print(" (๑>؂•̀๑)  1.-Ingresar un nuevo alumno ")
    print("          2.-Revisar lista               (๑>؂•̀๑)")
    print("          2.-Salir                    (๑>؂•̀๑)")
    print("--------------------------------------------")
    print("si quieres salir ingresa n")
    opcion = int( input("que quieres hacer:"))
    if opcion == 1:
        nobres= input("ingrese un nombre:")
        lista.append(nobres)
    elif opcion == 2:
        print(lista)
    elif opcion == 3:
        break

