# Programa que categorice las edades de una lista en mayores o menores de edad (mínimo 8 edades) e imprima una lista por cada caso.
# Nota: se crearían otras listas vacías para las edades de adultos y menores que se llenarían con los datos correspondientes (usando la instrucción para agregar) en la condición.
# (Commit: Programa 15 - for/if con lista de edades)
print("----------------------------------")
print("  Verificador y base de edades")
print("  favor de ingresar las edades a agregar")
print("            ૮ • ﻌ - ა")
print("----------------------------------")
Edades = []
n = int(input("Ingrese la cantidad de edades a agregar a una lista (mínimo 8): "))

while n < 8:
    print("----------------------------------")
    n = int(input("Por favor, ingrese al menos 8 edades: "))


edadMayor = []
edadMenor = []

for i in range(n):
    print("----------------------------------")
    edad = int(input(f"Ingrese la edad {i + 1}: "))
    Edades.append(edad)
    if edad >= 18:
        edadMayor.append(edad)
    else:
        edadMenor.append(edad)


print("----------------------------------")
print("Las edades Mayores son:(>᎑<๑)/ ♡", edadMayor)
print("----------------------------------")
print("Las edades Menores son:(>᎑<๑)/ ♡", edadMenor)
print("----------------------------------")
