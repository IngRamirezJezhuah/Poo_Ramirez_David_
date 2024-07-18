#programa que calcule el costo de envio basadp en el peso de un paquete ingresado por
#el usuario ("kg") las tarifas son las sig
# menos de 1 kg : $50
# de 1 kg a menos de 5 kg: $100
# de 1 kg a menos de 10 kg: $200
#10 kg o mas : $500 commit "Programa 7 - Costos Envios"
print("---------------------------")
print("Venta de Por Kilos")
print("---------------------------")

peso = int(input("Ofresca el peso de su producto: "))

if peso == 1:
    print("Tu total a pagar: $50")
elif peso <= 5:
    print("Tu total a pagar: $100")
elif peso <= 10:
    print("Tu total a pagar: $200")
elif peso >= 10:
    print("Tu total a pagar: $500")