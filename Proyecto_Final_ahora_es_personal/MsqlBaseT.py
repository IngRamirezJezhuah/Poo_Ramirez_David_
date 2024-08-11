import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tiendita"
)
cursor = connection.cursor()

class Tienda():
    def __init__(self):
        self.tabla = "tienda"
        self.consulta_especial = "Distribuidor de tienda"
        
    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "a":
                    tienda.registrar()
                case "b":
                    tienda.consultar()
                case "c":
                    tienda.editar()
                case "d":
                    tienda.borrar()
                case "e":
                    None
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|a)Registrar                            |")
        print("|b)Consultar                            |")
        print("|c)Editar                               |")
        print("|d)Borrar                               |")
        print(f"|e){self.consulta_especial.ljust(37)}|")
        print("|f)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?")
        
    def registrar(self):
        Nombre = input("Ingresa el nombre de la tienda: ")
        Direccion = input("Ingresar la dirección de la tienda: ")
        id_distribuidor = int(input("ingresar el id del distribuidor: "))
        #Falta trabajar el id del tistribuidor
        query = "INSERT INTO tienda (NombreMiselanea, Direccion, id_distribuidor) VALUES (%s, %s, %s)"
        cursor.execute(query, (Nombre, Direccion, id_distribuidor))
        connection.commit()
        print("Tienda registrado exitosamente")


    def borrar(self):
        tienda.consultar()
        id = input("ingresar el id a borrar:")
        comando = "DELETE FROM tienda WHERE id = %s"
        cursor.execute(comando, (id,))
        connection.commit()
        print("Tienda eliminada exitosamente")

    def editar(self):
        tienda.consultar()
        id = input("ingresar el id a editar:")
        cursor.execute("SELECT * FROM tienda WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        print(f"id de la tienda {resultados[0][0]}")
        print(f"Nombre de la tienda: {resultados[0][1]}")
        print(f"Direccion de la tienda: {resultados[0][2]}")
        print(f"id del distribuidor de la tienda: {resultados[0][3]}")
        print("-------------------------------------------------------------")


    def consultar(self):
        cursor.execute("SELECT * FROM tienda")
        resultados = cursor.fetchall()
        print("//////////////////////////////////////////////////////////")
        for fila in resultados:
            #print(fila)
            print(f"id de la tienda {fila[0]}")
            print(f"Nombre de la tienda: {fila[1]}")
            print(f"Direccion de la tienda: {fila[2]}")
            print(f"id del distribuidor de la tienda: {fila[3]}")
            print("//////////////////////////////////////////////////////////")

    def distribuidor():
        None

class Distribuidora(Tienda):
    def __init__(self):
        self.tabla = "distribuidor"
        self.consulta_especial = "Tienda a distribuir"

    def secuencia_menu(self):
        while True:
            x = distribuidor.menu()
            print(x)
            match x:
                case "a":
                    distribuidor.registrar()
                case "b":
                    distribuidor.consultar()
                case "c":
                    #distribuidor.editar()
                    None
                case "d":
                    tienda.borrar()
                case "e":
                    None
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        return super().menu()

    def registrar(self):
        Nombre = input("Ingresa el nombre de la compañia: ")
        Marca = input("Ingresar la marca: ")
        Producto = input("ingresar el tipo de producto: ")
        query = "INSERT INTO distribuidora (NombreCompañia, Marca, Producto) VALUES (%s, %s, %s)"
        cursor.execute(query, (Nombre, Marca, Producto))
        connection.commit()
        print("Distribuidor registrado exitosamente")
    
    def borrar(self):
        None

    def editar(self):
        None

    def consultar(self):
        cursor.execute("SELECT * FROM distribuidora")
        resultados = cursor.fetchall()
        print("//////////////////////////////////////////////////////////")
        for fila in resultados:
            print(f"id de la distribuidora: {fila[0]}")
            print(f"Nombre de la compañia: {fila[1]}")
            print(f"Marca: {fila[2]}")
            print(f"Producto: {fila[3]}")
            print("//////////////////////////////////////////////////////////")

###########################################################################

class Cliente(Tienda):
    def __init__(self):
        self.tabla = "cliente"
        self.consulta_especial = "cliente de Tienda"
    
    def secuencencia_menu(self):
        while True:
            x = cliente.menu()
            print(x)
            match x:
                case "a":
                    self.registrar()
                case "b":
                    self.consultar()
                case "c":
                    self.editar()
                case "d":
                    self.borrar()
                case "e":
                    None
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")
    def menu(self):
        return super().menu()
    
    def registrar(self):
        NombreCliente = input("ingresa el nombre del usuario: ")
        Telefono = input("ingrese el telefono del usuario: ")
        Correo = input("Ingrese el correo electronico: ")
        query = "INSERT INTO cliente (Nombre,Telefono,Correo) VALUES (%s,%s,%s)"
        cursor.execute(query, (NombreCliente,Telefono,Correo))
        connection.commit()
        print("Cliente Registrado")

    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id del cliente a borrar: ")
        borrar = f"DELETE FROM cliente WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
    

    def editar(self):
        cliente.consultar()
        id = int(input("ingrese el id del clinete a editar:"))
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id))
        resultados = cursor.fetchall()
        print(f"id del clinete {resultados[0][0]}")
        print(f"Nombre de el Clinete: {resultados[0][1]}")
        print(f"Telefono del usuario: {resultados[0][2]}")
        print(f"Correo Del usuario: {resultados[0][3]}")
        print("-------------------------------------------------------")

    def consultar(self):
        cursor.execute("SELECT * FROM cliente")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in Mostrar:
            print(f"id del Cliente {fila[0]}")
            print(f"Nombre del cliente: {fila[1]}")
            print(f"Telefono del cliente: {fila[2]}")
            print(f"Correo del cliente: {fila[3]}")
            print("--------------------------------------------------------")
    def distribuidora():
        None

###########################################################################

class Producto(Tienda):
    def __init__(self):
        self.tabla = "productos"
        self.consulta_especial = "Producto a comprar"
    def secuencencia_menu(self):
        while True:
            x = producto.menu()
            print(x)
            match x:
                case "a":
                    producto.menu()
                case "b":
                    producto.registrar()
                case "c":
                    producto.borrar()
                case "d":
                    producto.editar()
                case "e":
                    producto.consultar
                case "f":
                        break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        return super().menu()
    
    def registrar(self):
        TipoProducto = input("Ingrese el Producto a Añadir:")
        Marca = input("Ingrese la Marca a agregar:")
        query = input ("INSERT INTO productos (Tipo Producto, Marca) VALUES ($s,$s,)")
        cursor.execute(query, (TipoProducto,Marca))
        connection.commit()
        print("Producto Regisrtado")

    def borrar(self):
        producto.consultar()
        id = int(input("Ingrese el id del Producto a borrar:"))
        borrar = f"DELETE FROM productos WHERE id ={id}"
        cursor.execute(borrar)
        connection.commit()
        print("Producto eliminado correctamente")

    def editar(self):
        producto.consultar()
        id = int(input("Ingrese el id del Producto a Borrar:"))
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id))
        resultados = cursor.fetchall()
        print(f"id deñ Producto {resultados[0][0]}")
        print(f"Tipo de Producto:{resultados[0][1]}")
        print(f"Marca del Producto: {resultados[0][2]}")
        print("--------------------------------------------------------")
        
    def consultar(self):
        cursor.execute("SELECT * FROM productos")
        Mostar = cursor.fetchall()
        print("-------------------------------------------")
        for fila in Mostar:
            print(f"id deñ Producto {fila[0]}")
            print(f"Tipo de Producto:{fila[1]}")
            print(f"Marca del Producto: {fila[2]}")
        print("--------------------------------------------------------")
    def distribuidora():
        None


###########################################################################
tienda = Tienda()
distribuidor = Distribuidora()
cliente = Cliente()
producto = Producto()
while True:
    print("_________________________________________")
    print("|         Organizador de tienda         |")
    print("|                                       |")
    print("|Accion a realizar a la tabla:          |")
    print("|a)Distribuidor                         |")
    print("|b)Tienda                               |")
    print("|c)Cliente                              |")
    print("|d)Producto                             |")
    print("|e)Salir                                |")
    print("_________________________________________")
    x = input("¿Cual opcion deseas escojer?")
    match x:
        case "a":
            distribuidor.menu()
        case "b":
            tienda.secuencia_menu()
        case "c":
            cliente.secuencencia_menu()
        case "d":
            producto.secuencencia_menu()
        case "e":
            break
        case _:
            print("Favor de escribir una opcion valida")

###################################################################################

if connection.is_connected():
    connection.close()
    print("Conexión cerrada")

