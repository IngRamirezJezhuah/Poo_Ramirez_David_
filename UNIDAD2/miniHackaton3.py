def Sumar(a="a",b="b"):
    a = int(input("Dame numero:"))
    b = int(input("Dame numero:"))
    resultadoSuma = a + b
    print("")
    print("El resultado es:",resultadoSuma)
    return resultadoSuma

def Restar(a="a",b="b"):
    a = int(input("Dame numero:"))
    b = int(input("Dame numero:"))
    resultadoRest = a - b
    print("")
    print("El resultado es:",resultadoRest)
    return resultadoRest


def Dividir(a="a",b="b"):
    a = int(input("Dame numero:"))
    b = int(input("Dame numero:"))
    resultadoDiv = a / b
    print("")
    print("El resultado es:",resultadoDiv)
    return resultadoDiv


while True:
    print("---------------------------")
    print("        ଘ(੭ˊᵕˋ)੭* ੈ✩‧₊")
    print("    Calculadora basica")
    print("ଘ(∩^o^)⊃━☆゜1.-Suma")
    print("(｡- .•)2.-Resta")

    print("٩(ˊᗜˋ*)و4.- Divicion")
    print(" (๑>؂•̀๑) 5.-Salir")
    print("     ☆✧˖°⋆.˚☆✧˖°⋆.˚")
    print("---------------------------")
    opcion= int(input("Que desea hacer:"))
    if opcion == 1:
        Sumar()
    elif opcion== 2:
        Restar()
    elif opcion== 4:
        Dividir()
    elif opcion== 5:
        print("!chao chao! ૮ • ﻌ - ა ")
        break