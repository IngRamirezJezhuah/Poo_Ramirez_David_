#crear un programa que realice las funciones de una base de datos con la terminal commit "Programa-30 realizar una base de datos"

import mysql.connector
#SI FUNCIONA !!NO LE MUEVAS!!
#Conexion con la BD de MySQL
conecction=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestion_de_presos"
)
cursor = conecction.cursor()
#Edgar lo que vas a hacer es encargarte de hacer las funciones de registrar
class Preso:
    def __init__(self):
        self.presos = "presos"
        
    def secuencia_menu(self):
        while True:
            x = self.menu()#esta es una variable que abre nuestro menu y segun lo que escojas es lo que se va a ejecutar
            match x:#parecido al while true lo que hace es que segun el valor de x te va a escojer una opcion y la va a ejecutar
                case "1":
                    self.registrar()
                case "2":
                    self.editar()
                case "3":
                    self.eliminar()
                case "4":
                    self.consulta()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):#SI FUNCIONA !!NO LE MUEVAS!!
        print("_________________________________________")
        print(f"|{self.presos.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Editar                               |")
        print("|3)eliminar                             |")
        print("|4)consultar                            |")
        print("|5)salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?")

    def registrar(self):
        Nombre= input("inserte el nombre del preso: ")
        Años_carcel= input("ingrese el tiempo de la condena: ")
        Zona_Celda= input("ingrese la area asignada del preso: ")
        Crimen= input("ingrese el crimen del preso: ")
        query = "INSERT INTO preso (Nombre,Años_Carcel,Zona_Celda,Crimen) VALUES (%s,%s,%s,%s)"
        cursor.execute(query, (Nombre,Años_carcel,Zona_Celda,Crimen))
        conecction.commit()
        print("se relaizo correctamente el registro...")

    def editar(self):
        self.consulta()
        id = input("Ingrese id del preso a editar:")
        cursor.execute("SELECT * FROM `preso` WHERE id = %s;",(id,))
        resultado = cursor.fetchall()

        print(f"id del preso {resultado[0][0]}")
        print(f"Nombre del preso {resultado[0][1]}")
        Nombre = input("Ingrese el Nombre del preso: ")
        print(f"Años de carcel{resultado[0][2]}")
        Años_carcel = input("Ingrese los años de carcel: ")
        print(f"zona de la celda {resultado[0][3]}")
        Zona_Celda = input("Ingrese la Zona nueva: ")
        print(f"Crimen del preso {resultado[0][4]}")
        Crimen = input("Ingrese el Crimen cometido: ")
        comando = "UPDATE preso SET id=%s,Nombre=%s,Años_Carcel=%s,Zona_Celda=%s,Crimen=%s WHERE id =%s"
        cursor.execute(comando, (Nombre,Años_carcel,Zona_Celda,Crimen))
        conecction.commit()
        print("------------------------------------")
        print("edicion completada")
        

    def eliminar(self):
        self.consulta()
        id = input("ingresar el id del preso a eliminar:")
        borrar = f"DELETE FROM preso WHERE id = {id}"
        cursor.execute(borrar)
        conecction.commit()
        print("Preso eliminado correctamente")

    def consulta(self):
        cursor.execute("SELECT * FROM preso")
        Mostrar = cursor.fetchall()
        print("---------------------------------------")
        if Mostrar:
            for fila in Mostrar:
                print(f"id del preso {fila[0]}")
                print(f"Nombre del preso: {fila[1]}")
                print(f"Años de carcel: {fila[2]}")
                print(f"Zona celda: {fila[3]}")
                print(f"Crimen cometido: {fila[4]}")
                print("--------------------------------------------------------")
        else:
            print("no hay datos disponibles")