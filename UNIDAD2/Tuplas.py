#estructura de datos
#creacion de tuplas utilizando llaves
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

#//////////////////////////////////////////////////////////////////////////
#operaciones
#union de conjuntos
#union = conjunto1|conjunto conjunto 2
#union = conjunto.union(conjunto2)
union = conjunto| conjunto2
print("---------------------------------------------")
print("este es para juntar un valor mas a mi tupla con otra tupla")
union = conjunto.union(conjunto2)
print(union)
#//////////////////////////////////////////////////////////////////////////
#*Une los elementos iguales de dos conjuntos.
#interseccion= conjunto1& conjunto2
#interseccion= conjunto1.intersection(conjunto2)
interseccion= conjunto & conjunto2
interseccion= conjunto.intersection(conjunto2) 
print("---------------------------------------------")
print("este es para juntar un valor mas a mi tupla con otra tupla pero con un valor en especifico")
print(interseccion)
#//////////////////////////////////////////////////////////////////////////
#*Une los elementos que están en el primer conjunto pero no en el segundo.
#diferencia = conjunto1–conjunto2
#diferencia = conjunto1.difference(conjunto2)
diferencia = conjunto-conjunto2
diferencia= conjunto.difference(conjunto2)
print("---------------------------------------------")
print("este te imprime el valor que sea diferente a los otros")
print(diferencia)
#/////////////////////////Metodos comunes////////////////////////////////////////////
#numeros de elementos en el conjunto
#numero de elementos en el conjunto
#len conjunto1
#print(len(Conjunto))
print("---------------------------------------------")
print("este te dice cuantos elemento hay dentro de una tupla")
print(len(conjunto))
#//////////////////////////////////////////////////////////////////////////
#Verifica si un elemento esta en conjunto
#in
print("---------------------------------------------")
print("este es para verificar si hay un elemento en el conjunto")
print(2 in conjunto)

#//////////////////////////////////////////////////////////////////////////
#Elimina todo los elementos de un conjunto
#clear()
#conjuntos.clear()
print("---------------------------------------------")
print("este es para eliminar todos el contenido de un conjunto")
print(conjunto2.clear())
#//////////////////////////////////////////////////////////////////////////
#devuelve una  copia superficial del conjunto 
#copy
#conjunto.copy()
conjunto.copy()
print("---------------------------------------------")
print("este es para que devuelva una copia del conjunto")
print(conjunto)

#//////////////////////////Tuplas///////////////////////////

#creacion 
#utilizndo parentesis
tupla = (12, "DJ", "Caos")
print("---------------------------------------------")
print("este es para crear una tupla")
print(tupla)

#acceso a elementos
#utilizando indices con []
#tupla[indice]
tupla[1]
print("---------------------------------------------")
print("este es para indice de una tupla")
print(tupla)

#concanetacion de tuplas
#utilizando operador +
tupla2 = (25, "DJ", "Mayp")
tupla_concanetada = tupla + tupla2
print("---------------------------------------------")
print("este es para concanetar una tupla")
print(tupla_concanetada)

#Repeticion de tuplas
#utilizando operador *
#tupla_repetida = mi_tupla * 2
tupla_repetida = tupla *2
print("---------------------------------------------")
print("este es para multiplicar una tupla")
print(tupla_repetida)

#Desempaquetado de tuplas
#Asignar elementos de una tupla a diferentes variables
#tupla = (1,2,3) a,b,c = tupla
tuplita = (1,2,3)
a,b,c = tuplita
b = tuplita
c = tuplita
print("---------------------------------------------")
print("este es para asignar elementos de una tupla")
print(tuplita)

#Funciones integradas con tuplas
#print(len(mi_tupla))
#print(max(mi_tupla))
#print(min(mi_tupla))
#print(sum(mi_tupla))
