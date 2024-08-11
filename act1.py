tiendita = {
    "cokeycola": 30,
    "spuerk": 16,
    "dorilokos": 19,
    "machuran": 21,
    "trodents": 6,
}
print("--------------------------------------")
print("  ٩(ˊᗜˋ*)و   Tinedita perrona")
print("    1.   Cokeycola  = $30 ")
print("    2.    Spuerk  = $16")
print("    3.   Dorilokos  = $19")
print("    4.    Machuran  = $21")
print("    5.   Trodents  = $6")
print("--------------------------------------")

opciones = {
    1: "cokeycola",
    2: "spuerk",
    3: "dorilokos",
    4: "machuran",
    5: "trodents",
}

compra = int(input("Qué quieres comprar (1-5): "))
if compra in opciones:
    producto = opciones[compra]
    precio_original = tiendita[producto]
    print("--------------------------------------")
    print(f"Lo que llevaste es: {producto} por ${precio_original}")

    descuento = int(input("Ingrese la cantidad a  descontar : "))
    precio_con_descuento = precio_original * (1 - descuento / 100)
    print("--------------------------------------")
    print(f"El precio con descuento es: ${precio_con_descuento:.2f}")

    del tiendita[producto]
    print(f"{producto} eliminado de la tienda.")
    print("--------------------------------------")
    print("Productos restantes en la tienda:")
    for nombre, precio in tiendita.items():
        print(f"{nombre}: ${precio}")
else:
    print("Selección inválida. Por favor, elige una opción válida.")
    print("--------------------------------------")
