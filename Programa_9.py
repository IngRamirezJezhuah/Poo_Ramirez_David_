#escribe un codigo que solicite al usuario que ingrese una contraseña hasta que ingrese la contraseña correcta (POO123)
#programa 9- Contraseñas

print("Inicio de sesion")
contraseña = str(input("ingrese la contraseña:"))

while True:
    if contraseña == "POO123":
        print("Sesion inicada")
    else: 
        contraseña == False
        print("Incorrecto vuelva a ingresar")
    break