#crear un programa que realice las funciones de una base de datos con la terminal commit "Programa-30 realizar una base de datos"

import mysql.connector

# Función para conectar a la base de datos
def conectar():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bdescolares"
    )
    return connection

# Función para crear una tabla
def crear_tabla():
    connection = conectar()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            edad INT,
            direccion VARCHAR(255),
            id_maestro INT
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()
    print("Tabla creada exitosamente.")

# Función para mostrar los datos de la tabla
def mostrar_base():
    connection = conectar()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM alumnos")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    cursor.close()
    connection.close()

# Función para insertar datos en la tabla
def registrar_alumno():
    connection = conectar()
    cursor = connection.cursor()
    nombre = input("Ingrese su Nombre: ")
    edad = int(input("Ingrese su Edad: "))
    direccion = input("Ingrese su Dirección: ")
    id_maestro = int(input("Ingrese el ID del Maestro: "))
    cursor.execute(
        "INSERT INTO alumnos (nombre, edad, direccion, id_maestro) VALUES (%s, %s, %s, %s)",
        (nombre, edad, direccion, id_maestro)
    )
    connection.commit()
    cursor.close()
    connection.close()
    print("Alumno registrado exitosamente.")

# Función para eliminar datos de la tabla
def eliminar_alumno():
    connection = conectar()
    cursor = connection.cursor()
    borrar = input("Ingrese el ID del usuario que quiere borrar: ")
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (borrar,))
    if cursor.rowcount > 0:
        print(f"Usuario con ID {borrar} borrado exitosamente.")
    else:
        print(f"No se encontró ningún usuario con ID {borrar}.")
    connection.commit()
    cursor.close()
    connection.close()

# Menú principal
def menu():
    while True:
        print("\nOpciones:")
        print("1. Crear tabla")
        print("2. Mostrar base de datos")
        print("3. Registrar alumno")
        print("4. Eliminar alumno")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_tabla()
        elif opcion == "2":
            mostrar_base()
        elif opcion == "3":
            registrar_alumno()
        elif opcion == "4":
            eliminar_alumno()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


menu()