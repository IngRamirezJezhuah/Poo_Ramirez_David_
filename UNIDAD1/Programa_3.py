#Programa qe pida al usuario su peso (kg) y estatura(m) y calcule el imc y lo almacene en una variable y muestre por pantalla el resultado
print("-------------------------")
print("Medidor del IMC")
print("-------------------------")

Peso = float(input("me podrias ofrecer tu peso:"))
altura = float(input("me podrias dar tu altura:"))

imc = round(Peso /  altura ** 2)

print("-------------------------")
print("Tu IMC es:", imc)
print("-------------------------")