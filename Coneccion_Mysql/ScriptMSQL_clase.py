import mysql.connector

# Conexión a la base de datos
connection = mysql.connector.connect( #lo que hace es definir lo que es adentro
    host="localhost",#el servidor o la red en la que se esta ejecutando
    user="root",#aqui es el usuario que tenemos y como se llama nuestro usuario con el que ingresamos
    password="",#pues aqui va la contraseña
    database="bdescolares"
)

if connection.is_connected():
    print("Conexion Exitosa a la base de datos")

#////////////////Consultar la tabla
print("Consultar")
cursor = connection.cursor()
cursor.execute("SELECT * FROM alumnos")#codigo para mostrar el contenido con el comando de Lenguaje SQL Select
resultados = cursor.fetchall()#obtener datos
for fila in resultados:
    print(fila)



def Mostrar_Base():
    for fila in resultados:#aqui hicimos uuna funcion para realizarla muestra de los archivos
        print(fila)

Mostrar_Base()
#Esj =str(input("Para Mostar la fila presiona 1:"))
#if Esj == 1 :
#    Mostrar_Base
#else:pass
#////////////////////Registrar A la Base
def register():
    if cursor == 'POST':
        id = cursor.form['id']
        nombre = cursor.form['nombre']
        correo = cursor.form['correo']
        direccion = cursor.form['direccion']
        cursor.execute(
        "INSERT INTO alumnos (nombre, correo, direccion) VALUES (%s, %s, %s, %s)",
        (nombre,correo, direccion)
        )
        cursor.commit()
        

Nombre = str(input("ingrese su Nombre:"))
Correo = str(input("ingrese su Correo:"))
Direccion = str(input("ingrese su Direccion:"))
cursor.execute("INSERT INTO alumnos (nombre, correo, direccion) VALUES (%s, %s, %s, %s)",(Nombre,Correo, Direccion))#agregar un nuevo usuario
cursor.commit()


#connection.commit()#esta es una variable que confirma los cambios, es como el boton de guardado de los videojuegos
borrar = str(input("Que usuario quieres borrar:"))
# Ejecutar la consulta de eliminación usando un placeholder
cursor.execute("DELETE FROM `alumnos` WHERE alumnos.id = %s", (borrar))
if cursor.rowcount > 0:
    print(f"Usuario con ID {borrar} borrado exitosamente.")
else:
    print(f"No se encontró ningún usuario con ID {borrar}.")
connection.commit()
resultados= cursor.fetchall()
Mostrar_Base()
#cursor.close()#buenas practicas de programador cerrar el cursor para que termine de ejecutarse y no este en segundo plano
cursor.close
connection.close()#buenas practicas de programador cerrar la coneccion para que termine de conectarse