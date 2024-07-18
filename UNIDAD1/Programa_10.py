#escribe un programa que pida al ususario dos numeros y calcule su suma, el programa debe repetir hasta que el usuario ingrese n para detenerse

print("-----------------------")
print("Ingrese los numeros a sumar")
print("-----------------------")
salida = "n"
while True:
    numero_1 = int(input("Deme un numero:"))
    numero_2= int(input("Deme un numero:"))
    suma_numeros = numero_1 + numero_2
    print("Tu total es", suma_numeros)
    
    print("Para Salir escriba: n ")
    salida = str(input("Desea salir:"))
    if salida == "n":
        print("adios")
        break
    else:
        print("-----------------------")
        print("Ingrese los numeros a sumar")
        print("-----------------------")