diccionario ={
    "nombre": "Ana",
    "edad": 23,
    "grupo": "A"
}
print("---------------------٩(ˊᗜˋ*)و -----------------------------")
print("☆✧˖°⋆.˚ ☆✧˖°⋆.˚ ☆✧˖°⋆.˚")
#otra variable seria usar "dic"
dic_dicionario = dict(nombre="Ana",edad=23,grupo="A")

print("---------------------٩(ˊᗜˋ*)و -----------------------------")
print("☆✧˖°⋆.˚ ☆✧˖°⋆.˚ ☆✧˖°⋆.˚")
print("Este es un dicionario normal",diccionario)
print("este es diccionario con dict",dic_dicionario)
print(" ")
print("---------------------٩(ˊᗜˋ*)و -----------------------------")
print("☆✧˖°⋆.˚ ☆✧˖°⋆.˚ ☆✧˖°⋆.˚")
#Este es para jalar un valor del diccionario
print("Aqui es para jalar un valor de un diccionario:",diccionario["edad"])
print(" ")
print("---------------------٩(ˊᗜˋ*)و -----------------------------")
print("☆✧˖°⋆.˚ ☆✧˖°⋆.˚ ☆✧˖°⋆.˚")
#Esta es para definir una llave de una lista y ponerla en una variable
nombre = diccionario["nombre"]
print("Esto es para sacar la llave pero con una variable:",nombre)
print(" ")
print("---------------------٩(ˊᗜˋ*)و -----------------------------")
#Este es para cambiar el valor de una llave de una lista
print("☆✧˖°⋆.˚ ☆✧˖°⋆.˚ ☆✧˖°⋆.˚")
diccionario["nombre"] = "laura"
print(diccionario)
print(" ")
print("---------------------٩(ˊᗜˋ*)و -----------------------------")
print("☆✧˖°⋆.˚ ☆✧˖°⋆.˚ ☆✧˖°⋆.˚")
#Dicionario["nuevo valor"]= "valornuevo"
diccionario["carrera"] = "Ti"
print(diccionario)
print(" ")
print("---------------------٩(ˊᗜˋ*)و -----------------------------")
print("☆✧˖°⋆.˚ ☆✧˖°⋆.˚ ☆✧˖°⋆.˚")
#elimina una llave de un diccionario
del diccionario["grupo"]
print(diccionario)
print(" ")
print("---------------------٩(ˊᗜˋ*)و -----------------------------")
print("☆✧˖°⋆.˚ ☆✧˖°⋆.˚ ☆✧˖°⋆.˚")
#devuelve las claves del diccionario
#diciconario.key
keys = diccionario.keys()
print(keys)
print(" ")
print("---------------------٩(ˊᗜˋ*)و -----------------------------")
print("☆✧˖°⋆.˚ ☆✧˖°⋆.˚ ☆✧˖°⋆.˚")
#en este caso seria lo contrario en vez de decirme las llaves me da los valres que pertenecen a esta
values = diccionario.values()
print(values)
print(" ")
print("---------------------٩(ˊᗜˋ*)و -----------------------------")
print("☆✧˖°⋆.˚ ☆✧˖°⋆.˚ ☆✧˖°⋆.˚")
#esta es para imprimir los valores igual pero ahora de manera distinta o mas organizada
items = diccionario.items()
print(items)