#escribe un programa que escriba la tabla de multiplicar del 5
#commit "Programa 12 - Tabla de 5"
Numero = 5

print("-----------------------")
print("Tabla de multiplicar de 5")
print("-----------------------")
for Tabla in range(1,11):
    multi = Numero*Tabla
    print(f"{Tabla} x {Numero} = {multi}") 
    
print("-----------------------")