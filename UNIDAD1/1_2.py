
while True:
    print("---------------------------------------------")
    print("|    Calculador de Áreas                     |")
    print("| Las figuras disponibles son                |")
    print("|  1.-rectangulo  2-cuadrado  3-triángulo    |")
    print("|--------------------------------------------")
    print("|  Ingrese el área a resolver  ⸜(｡˃ ᵕ ˂ )⸝♡  |")
    print("---------------------------------------------")
    print("|--------------------------------------------")
    print("|  Si deseas salir ingresa '4'  ⸜(｡˃ ᵕ ˂ )⸝♡  |")
    print("---------------------------------------------")

    figura = int(input("(੭ ˊ^ˋ)੭ingrese que desea hacer:"))
    if figura == 1:
        base = float(input("Dame una base: "))
        altura = float(input("Dame la altura: "))
        area = base * altura
        print("tu area es:", area)
    elif figura == 3:
        base = float(input("Dame una base: "))
        altura = float(input("Dame la altura: "))
        area = base * altura / 2
        print("Tu área es igual a:", area)
    elif figura == 2:
        lado = float(input("Dame el lado del cuadrado: "))
        area = lado * lado
        print("Tu área es igual a:", area)
    elif figura == 4:
        print("Adios (>᎑<๑)/ ♡!")
        break