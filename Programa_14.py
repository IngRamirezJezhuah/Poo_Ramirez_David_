#Escribe un programa que sume todos los elementos de una lista y muestre el resultado.
#(Commit: Programa 14 - for operación)
#suma    +=        numero
#  variable   variable que se iran tomando con el ciclo
#suma = suma + numero
print("----------------------------------")
print("  Sumador de Numeros")
print("  favor de ingresar los numeros a agregar")
print("            ૮ • ﻌ - ა")
print("----------------------------------")
numeros = []  # Create an empty list
n = int(input("Ingrese la cantidad de numeros a sumar de una lista: "))

for i in range(n):
    print("----------------------------------")
    numero = int(input("Dame un numero:◝(ᵔᵕᵔ)◜ "))
    numeros.append(numero)  # Add the number to the list

suma = sum(numeros)  # Sum up all numbers in the list
print("----------------------------------")
print("✧⁺⸜(  •‿•  )⸝⁺✧La suma es: ", suma)