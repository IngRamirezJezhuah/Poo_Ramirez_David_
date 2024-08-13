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
                    tienda.distribuidor_tienda()
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
        nombre = input("Escribir el nuevo nombre de la tienda: ")
        print(f"Dirección de la tienda: {resultados[0][2]}")
        direccion = input("Escribir la nuevadirección de la tienda: ")
        print(f"id del distribuidor de la tienda: {resultados[0][3]}")
        v = input("Deseas ver los distribuidores, para conocer su id? (Y/N): ")
        if v =="y" or v =="Y":
            distribuidor.consultar()
        id_distribuidor = input("Escribir el id del distribuidor de la tienda: ")
        
        comando = "UPDATE tienda SET NombreMiselanea=%s,Direccion=%s ,id_distribuidor=%s WHERE id = %s"
        cursor.execute(comando, (nombre,direccion,id_distribuidor,id,))
        connection.commit()
        print("Tienda editada exitosamente")
        print("--------------------------------------------------------")

    def consultar(self):
        cursor.execute("SELECT * FROM tienda")
        resultados = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in resultados:
            print(f"id de la tienda {fila[0]}")
            print(f"Nombre de la tienda: {fila[1]}")
            print(f"Direccion de la tienda: {fila[2]}")
            print(f"id del distribuidor de la tienda: {fila[3]}")
            print("--------------------------------------------------------")

    def distribuidor_tienda(self):
        tienda.consultar()
        id = input("ingresar el id de la tienda a consultar el provedor:")
        
        cursor.execute("SELECT * FROM tienda WHERE id=%s",(id,))
        resultado = cursor.fetchone()
        if resultado:
            print("Datos de la tienda")
            print(f"id de la tienda: {resultado[0]}")
            print(f"Nombre de la tienda: {resultado[1]}")
            print(f"Direccion de la tienda: {resultado[2]}")
            print(f"id del distribuidor de la tienda: {resultado[3]}")
            print("/////")
            print(f"Datos del distribuidor de la tienda:")
            cursor.execute("SELECT * FROM distribuidora WHERE id=%s",(resultado[3],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id de la distribuidora: {fila[0]}")
                    print(f"Nombre de la compañia: {fila[1]}")
                    print(f"Marca: {fila[2]}")
                    print(f"Producto: {fila[3]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontró ninguna tienda con el id proporcionado.")
            print("-----------")
        print("--------------------------------------------------------")

class Distribuidora(Tienda):
    def __init__(self):
        self.tabla = "distribuidor"
        self.consulta_especial = "Tienda a distribuir"

    def secuencia_menu(self):
        print(23456)
        while True:
            b = distribuidor.menu()
            match b:
                case "a":
                    distribuidor.registrar()
                case "b":
                    distribuidor.consultar()
                case "c":
                    distribuidor.editar()
                case "d":
                    distribuidor.borrar()
                case "e":
                    distribuidor.distribuidor_tienda()
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
        distribuidor.consultar()
        id = input("ingresar el id de la tienda a borrar:")
        comando = "DELETE FROM distribuidora WHERE id = %s"
        cursor.execute(comando, (id,))
        connection.commit()
        print("Distribuidora eliminada exitosamente")

    def editar(self):
        distribuidor.consultar()
        id = input("ingresar el id del distribuidor a editar:")
        cursor.execute("SELECT * FROM distribuidora WHERE id = %s", (id,))
        resultados = cursor.fetchall()

        print(f"id de la distribuidora {resultados[0][0]}")
        print(f"Nombre de la distribuidora: {resultados[0][1]}")
        Nombre = input("Ingresar el nombre del distribuidor:")
        print(f"Marca de la distribuidora: {resultados[0][2]}")
        Marca = input("Ingresar la nueva marca del distribuidor: ")
        print(f"Tipo de producto: {resultados[0][3]}")
        tipo_producto = input("Ingresar el nuevo tipo de producto:")
        print("--------------------------------------------------------")

        comando = "UPDATE distribuidora SET NombreCompañia=%s,Marca=%s,Producto=%s WHERE id = %s"
        cursor.execute(comando, (Nombre,Marca,tipo_producto,id,))
        connection.commit()
        print("Distribuidora editada exitosamente")

    def consultar(self):
        cursor.execute("SELECT * FROM distribuidora")
        resultados = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in resultados:
            print(f"id de la distribuidora: {fila[0]}")
            print(f"Nombre de la compañia: {fila[1]}")
            print(f"Marca: {fila[2]}")
            print(f"Producto: {fila[3]}")
            print("--------------------------------------------------------")

    def distribuidor_tienda(self):
        super().distribuidor_tienda()

class Cliente(Tienda):
    def __init__(self):
        self.tabla = "cliente"
        self.consulta_especial = "Cliente Producto"
    
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
                    self.producto()
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
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"ID del cliente: {resultados[0][0]}")
            print(f"Nombre del Cliente: {resultados[0][1]}")
            NombreCliente = input("Ingresa el nombre del cliente: ")
            
            print(f"Teléfono del Cliente: {resultados[0][2]}")
            Telefono = input("Ingresa el teléfono del cliente: ")
            
            print(f"Correo del Cliente: {resultados[0][3]}")
            Correo = input("Ingresa el correo electrónico: ")
            
            comando = "UPDATE cliente SET Nombre = %s, Telefono = %s, Correo = %s WHERE id = %s"
            cursor.execute(comando, (NombreCliente, Telefono, Correo, id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
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
    
    def producto(self):  
        cliente.consultar()
        id = input("Ingrese el id del cliente a consultar: ")
        cursor.execute("SELECT * FROM cliente WHERE id=%s",(id,))
        Mostrar = cursor.fetchone()
        if Mostrar:
            print("Datos de cliente")
            print(f"id del cliente: {Mostrar[0]}")
            print(f"Nombre del cliente: {Mostrar[1]}")
            print(f"Numero del cliente: {Mostrar[2]}")
            print(f"Correo del cliente: {Mostrar[3]}")
            print("-----------------")
            print(f"Datos del Producto comprado:")
            cursor.execute("SELECT * FROM productos WHERE id_cliente=%s",(Mostrar[0],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id dels Producto: {fila[0]}")
                    print(f"Tipo de Producto: {fila[1]}")
                    print(f"Marca: {fila[2]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontro ningun producto en la tineda con el id proporcionado.")
            print("---------")
            print("--------------------------------------------------------")

class Producto(Tienda):
    def __init__(self):
        self.tabla = "productos"
        self.consulta_especial = "producto tienda"

    def secuencencia_menu(self):
        while True:
            x = productos.menu()
            print(x)
            match x:
                case "a":
                    productos.registrar()
                case "b":
                    productos.consultar()
                case "c":
                    productos.editar()
                case "d":
                    productos.borrar()
                case "e":
                    productos.compra()
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        return super().menu()
    
    def registrar(self):
        TipoProducto = input("Ingrese el Producto a Añadir: ")
        Marca = input("Ingrese la Marca a agregar: ")
        query = "INSERT INTO `productos`(`Tipo Producto`, `Marca`) VALUES (%s, %s)"
        cursor.execute(query, (TipoProducto, Marca))
        connection.commit()
        print("Producto Registrado")


    def borrar(self):
        productos.consultar()
        id = int(input("Ingrese el id del Producto a borrar:"))
        borrar = f"DELETE FROM productos WHERE id ={id}"
        cursor.execute(borrar)
        connection.commit()
        print("Producto eliminado correctamente")

    def editar(self):
        productos.consultar()
        id = int(input("Ingrese el ID del Producto a Editar: "))
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        
        if resultados:
            print(f"ID del Producto: {resultados[0][0]}")
            print(f"Tipo de Producto: {resultados[0][1]}")
            TipoProducto = input("Ingrese el nuevo tipo de producto: ")

            print(f"Marca del Producto: {resultados[0][2]}")
            Marca = input("Ingrese la nueva marca: ")
            
            comando = "UPDATE productos SET `Tipo Producto` = %s, Marca = %s WHERE id = %s"
            cursor.execute(comando, (TipoProducto, Marca, id))
            connection.commit()
            
            print("--------------------------------------------------------")
            print("Actualización exitosa")
        else:
            print("No se encontró un producto con ese ID.")

        
    def consultar(self):
        cursor.execute("SELECT * FROM productos")
        Mostar = cursor.fetchall()
        for fila in Mostar:
            print("-------------------------------------------")
            print(f"id del Producto {fila[0]}")
            print(f"Tipo de Producto:{fila[1]}")
            print(f"Marca del Producto: {fila[2]}")
        print("--------------------------------------------------------")

    def compra(self):
        cliente.consultar()
        id = input("Ingrese el id del cliente a consultar: ")
        cursor.execute("SELECT * FROM cliente WHERE id=%s",(id,))
        Mostrar = cursor.fetchone()
        if Mostrar:
            print("Datos de cliente")
            print(f"id del cliente: {Mostrar[0]}")
            print(f"Nombre del cliente: {Mostrar[1]}")
            print(f"Numero del cliente: {Mostrar[2]}")
            print(f"Correo del cliente: {Mostrar[3]}")
            print("-----------------")
            print(f"Datos del Producto comprado:")
            cursor.execute("SELECT * FROM productos WHERE id_cliente=%s",(Mostrar[0],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id dels Producto: {fila[0]}")
                    print(f"Tipo de Producto: {fila[1]}")
                    print(f"Marca: {fila[2]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontro ningun producto en la tineda con el id proporcionado.")
            print("---------")
            print("--------------------------------------------------------")


###########################################################################
tienda = Tienda()
distribuidor = Distribuidora()
cliente = Cliente()
productos = Producto()
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
            distribuidor.secuencia_menu()
        case "b":
            tienda.secuencia_menu()
        case "c":
            cliente.secuencencia_menu()
        case "d":
            productos.secuencencia_menu()
        case "e":
            break
        case _:
            print("Favor de escribir una opcion valida")

###################################################################################

if connection.is_connected():
    connection.close()
    print("Conexión cerrada")
    print("Adios bye bye ૮₍´｡ᵔ ꈊ ᵔ｡`₎ა ")