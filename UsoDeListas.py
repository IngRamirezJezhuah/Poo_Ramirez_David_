lista = [1, 2, 3, "ANA"]
#print(lista[2])#devueelve el elemento que se esta en la posicion i de la lista
#print(lista[-1])#la pide de atras a adelante
#print(lista["ANA"]) este codigo no funciona

#lista[2]= "hola" #en este caso se puede modificar el valor dentro de una lista definiendo que posicion quieres modificar
#print(lista[2])

#lista.apend(elemento) añade elemento al final de la lista
#lista.append("Ana")

#lista.insert(i,elemento)
#lista.insert(0,0)#dice posicion y que quiere agregar
#print(lista)

#lista inster(i, elemento)
#inserta elementos en la posision i

#Lista extend su funcion es implementar a una lista los elementos de otra lista 
#lista2 =  [4,5,6]
#lista.extend(lista2)# le manda mas valores con los ya existentes y solo los junta
#print(lista)

#Lista.remove(cosa a eliminar) se usa esta para eliminar un elemento de la lista que no deseamos
#lista.remove("ANA")
#print(lista)


#lista.pop(i) este se usa igual un eliminar pero, primero lo agrega y luego lo borra
elemento = lista.pop(3)
print(elemento)
print(lista)
