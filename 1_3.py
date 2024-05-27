lista = [ 12, 14 ,16, 7, 8, 9, 18, 20, 22, 27, 28]

infancia = []
adolecencia = []
jovenes= []
adultos = []

for lista in lista:
    if lista <= 11:
        infancia.append(lista)
    elif lista >= 12 and lista <= 17:
        adolecencia.append(lista)
    elif lista >= 18 and lista <=26 :
        jovenes.append(lista)
    elif lista <= 27:
        adultos.append(lista)

print("Infancia:", infancia)
print("Adolecencia", adolecencia)
print("Jovenes:", jovenes)
print("Adultos", adultos)