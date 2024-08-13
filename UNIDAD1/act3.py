conjunto = {12, "DJ", "Junio"}
conjunto2 = {12, "DJ", "Mayp"}
print("---------------------------------------------")
print("este es la primera tupla la base mas comun")
print(conjunto)

#//////////////////////////////////////////////////////////////////////////
#para añadir elementos se usa el siguiente comando
#conjunto.add(valorNuevo)

conjunto.add("peritocles")
conjunto.add("kakattua")
print("---------------------------------------------")
print("este es para agregarle un valor mas a mi tupla")
print(conjunto)

#//////////////////////////////////////////////////////////////////////////
#eliminar elementos metodo remove
#conjjunto.discard(valor) este es para quitar un valor que no queremos
# conjunto.remove(valor)   
conjunto.discard("peritocles")#solo para que evite un error, si esta tal valor borrarlo por si acaso
conjunto.remove("kakattua")#este de a fuerzas es para quitar
print("---------------------------------------------")
print("este es para quitarle un valor mas a mi tupla")
print(conjunto)