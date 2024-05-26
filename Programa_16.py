#*Pide al usuario que ingrese tres promedios y encuentra el mayor de ellos (elif)
#(Commit: Programa 16 - promedio mayor)
print("----------------------------------------")
print("   Calificaciones")
print("Favor de ingresar los datos solicitados")
print("           (>᎑<๑)/ ♡")
print("-----------------------------------------")

calificaciones = []

for i in range(3):
    calif = int(input(f"Dame la calificación {i + 1}: "))
    calificaciones.append(calif)

print("-------------------------")
print("Tus calificaciones son:")
print("˚₊‧꒰ა ☆ ໒꒱ ‧₊˚", calificaciones,"˚₊‧꒰ა ☆ ໒꒱ ‧₊˚")

calif_mayor = max(calificaciones)
print("-------------------------")
print("꒰ᐢ. .ᐢ꒱₊˚⊹ La calificación mayor es:", calif_mayor)

if calif_mayor > 50:
    print("Calificación alta")
    print("-------------------------")
elif calif_mayor == 50:
    print("Calificación media")
    print("-------------------------")
else:
    print("Calificación baja")
    print("-------------------------")


