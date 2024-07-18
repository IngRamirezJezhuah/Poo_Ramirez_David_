#Programa que pregunte al usuario qué tipo de conversión de temperatura quiere realizar (de Celsius a Fahrenheit o de Fahrenheit a Celsius) y repite el proceso hasta que el usuario decida salir.
#Notas: imprime el menú con las opciones cuantas veces sea necesarias (while) y hacer la operación necesaria según la opción ingresada (elif)
#(Commit: Programa 17 - conversión de temperaturas)

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("-----------------------------------------")
    print("      Conversión de Temperatura")
    print("          ₊˚⊹⋆˙౨ৎ˚⟡˖ ࣪")
    print("1. Convertir de Celsius a Fahrenheit")
    print("          ₊˚⊹⋆˙౨ৎ˚⟡˖ ࣪")
    print("2. Convertir de Fahrenheit a Celsius")
    print("          ₊˚⊹⋆˙౨ৎ˚⟡˖ ࣪")
    print("              3. Salir")
    print("-----------------------------------------")
    
    opcion = input("⸜(｡˃ ᵕ ˂ )⸝♡Elige una opción (1, 2, 3): ")
    
    if opcion == '1':
        print("-----------------------------------------")
        celsius = float(input("Introduce la temperatura en Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print("Tu total convertido es de:")
        print("      ₍ᐢ.  ̫.ᐢ₎")
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
    elif opcion == '2':
        print("-----------------------------------------")
        fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print("Tu total convertido es de:")
        print("      ₍ᐢ.  ̫.ᐢ₎")
        print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
    elif opcion == '3':
        print("-----------------------------------------")
        print("Saliendo del programa. ¡Adiós!₍^ >ヮ<^₎ .ᐟ.ᐟ")
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
