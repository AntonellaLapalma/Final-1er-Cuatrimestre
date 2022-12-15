import os
#################################################################   MENU   #######################################################################

def menu():   ###  DA LA BIENVENIDA Y PIDE QUE INGRESE INF 
    print("=====================================================")
    print("                 >>> BIENVENIDO <<<                  ")
    print("=====================================================\n")
    print("> 0. PELÍCULAS DISPONIBLES \n")
    print("> 1. ALQUILAR PELÍCULA \n")
    print("> 2. GESTIÓN DE CLIENTE \n")
    print("> 3. GESTIÓN DE PELÍCULA \n")
    print("> 4. SALIR")
    print("\n=====================================================")
    opcion = input("> Elegir opción: ")
    print("=====================================================\n\n")
        
    if opcion == ("0"):   ### Busca las peliculas e imprime su estado
        print("=====================================================")
        print("           >>> PELÍCULAS DISPONIBLES <<<             ")
        print("=====================================================\n")
        mostrarpeliculas()
        return menu()

    elif opcion == ("1"): ### Alquiler de pelicula
        alquilerpeliculas()
        return 

    elif opcion == ("2"): ### Gestion de cliente
        submenu2()
        return menu()

    elif opcion == ("3"): ### Gestion pelicula
        submenu3()
        return menu()

    elif opcion == ("4"): ### Salir 
        print("                   >>> ADIÓS <<<\n\n")
        exit()
        

    else:
        print("-----------------------------------------------------")
        print("> La opción ingresada es incorrecta.")
        print("-----------------------------------------------------\n\n")
        return menu()

##################################################################################################################################################

##########################################################   PELICULAS DISPONIBLES   ################################################################

def mostrarpeliculas():
    with open("peliculas.txt", "r") as p:
        linea = p.readline()
        print("-----------------------------------------------------")
        print("{0:^15} {1:^21} {2:^15}".format("CÓDIGO","TÍTULO", "GÉNERO",)) 
        print("-----------------------------------------------------")
        while linea != "":
            renglon = linea.split(',')
            if renglon [3] == ("N"):
                print ("{0:^15} {1:^21} {2:^15}".format(renglon[0] , renglon[1] , renglon[2]))
            linea = p.readline()
        print("-----------------------------------------------------")
        print("\n=====================================================\n\n")
        p.close()

##################################################################################################################################################

##########################################################   ALQUILER PELICULAS   ################################################################

def alquilerpeliculas():
    print("=====================================================")
    print("             >>> ALQUILAR PELÍCULA <<<               ")
    print("=====================================================\n")
    print("> 0. CONSULTAR DISPONIBILIDAD DE PELÍCULA \n")
    print("> 1. ALQUILAR PELÍCULA \n")
    print("> 2. DEVOLVER PELÍCULA \n")
    print("> 3. ATRÁS")
    print("\n=====================================================")
    opcion = input("> Elegir opción: ")
    print("=====================================================\n\n")
    opcionesalquiler(opcion)

def opcionesalquiler(opcion):  
    if opcion == ("0"):   ### Mostrar peliculas disponibles
        print("=====================================================")
        print("        >>> INGRESE EL CÓDIGO DE BARRA <<<           ")
        print("=====================================================\n")
        ingreso = validarlistapeliculas()
        validarestadopelicula(ingreso)
        buscarpelicula(ingreso)
        print("\n=====================================================\n\n")
        return alquilerpeliculas()

    elif opcion == ("1"): ### Registrar prestamo
        print("=====================================================")
        print("            >>> ALQUILAR PELÍCULA <<<                ")
        print("=====================================================\n")
        dni = validarlistadoclientes()
        validarestadocliente(dni)
        opcionalquiler(dni)
        copiararchivoclientes()
        copiararchivopeliculas()
        return alquilerpeliculas() 

    elif opcion == ("2"): ### Devolver pelicula
        print("=====================================================")
        print("            >>> DEVOLVER PELÍCULA <<<         ")
        print("=====================================================\n")
        dni = validarlistadoclientes()
        opciondevolver(dni)
        copiararchivoclientes()
        copiararchivopeliculas()
        return alquilerpeliculas()

    elif opcion == ("3"): ### Atras
        return menu()

    else:                 ### Se ingresaron mal los datos
        print("-----------------------------------------------------")
        print("> La opción ingresada es incorrecta.")
        print("-----------------------------------------------------\n\n")
        return alquilerpeliculas()

##################################################################################################################################################

########################################################   FUNCIONES ALQUILER   ##################################################################

def buscarpelicula (codigo):          ### Busca si la pelicula esta alquilada 
    with open("peliculas.txt", "r") as p:
        linea = p.readline()
        while linea != "": 
            renglon = linea.split(',')
            if (str(codigo)) == renglon[0] and renglon [3] == ("P"):
                p.close()
                return print ("> La pelicula está alquilada por el cliente " + renglon[4])
            linea = p.readline()
            return print("> La película está disponible.")
        p.close()
    return 

def opcionalquiler(dni):              ### Pide la pelicula
    pelicula = validarlistapeliculas()
    validarestadopelicula(pelicula)
    alquilarpelicula(pelicula,dni)
    return
    
def alquilarpelicula(pelicula,dni):   ### Registra la pelicula en el txt de peliculas
    with open("peliculas.txt", "r") as rp:
        with open("peliculascopia.txt", "w") as wp:
            linea = rp.readline()
            while linea != "":
                renglon = linea.split(',')
                if pelicula == renglon[0]:
                    wp.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + "P" + "," + dni + "," + "\n")               
                    print("\n=====================================================")
                    print("> La película se alquiló correctamente.")
                    print("=====================================================\n\n")
                else:
                    wp.write(linea)
                linea = rp.readline()
            wp.close()
        rp.close()
        return registraralquiler(pelicula,dni) 

def registraralquiler(pelicula,dni):  ### Registra la pelicula en el txt de clientes
    with open("clientes.txt", "r") as rc:
        with open("clientescopia.txt", "w") as wc:
            linea = rc.readline()
            while linea != "":
                renglon = linea.split(',')
                if dni == renglon[0]:
                    wc.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + renglon[3] + "," + "O" + "," + pelicula + "," + "\n")
                else:
                    wc.write(linea)
                linea = rc.readline()
            wc.close()
        rc.close()
        return

##################################################################################################################################################

########################################################   FUNCIONES DEVOLUCION   ##################################################################

def opciondevolver(dni):                  ### Pide la pelicula
    registrardevolucion(dni)
    return
    
def devolverpelicula(pelicula):       ### Registra la devolucion en el txt de peliculas
    with open("peliculas.txt", "r") as rp:
        with open("peliculascopia.txt", "w") as wp:
            linea = rp.readline()
            while linea != "":
                renglon = linea.split(',')
                if pelicula == renglon[0]:
                    wp.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + "N" + "," + "N" + "," + "\n")              
                    print("=====================================================")
                    print("> La película se devolvió correctamente.")
                    print("=====================================================\n\n")
                else:
                    wp.write(linea)
                linea = rp.readline()
            wp.close()
        rp.close()
        return 

def registrardevolucion(dni):             ### Registra la devolucion en el txt de clientes
    with open("clientes.txt", "r") as rc:
        with open("clientescopia.txt", "w") as wc:
            linea = rc.readline()
            while linea != "":
                renglon = linea.split(',')
                if str(dni) == renglon[0]:
                    pelicula = renglon[5]
                    wc.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + renglon[3] + "," + "N" + "," + "N" + "," + "\n")
                else:
                    wc.write(linea)
                linea = rc.readline()
            wc.close()
        rc.close()
        return devolverpelicula(pelicula)

##################################################################################################################################################

##############################################################   SUBMENU 2   ##################################################################### 

def submenu2 ():        ### Opciones de gestion cliente
    print("=====================================================")
    print("             >>> GESTION DE CLIENTE <<<              ")
    print("=====================================================\n")
    print("> 0. REGISTRAR CLIENTE NUEVO \n")
    print("> 1. CONSULTAR ESTADO DEL CLIENTE \n")
    print("> 2. MODIFICAR DATOS DEL CLIENTE \n")
    print("> 3. ELIMINAR CLIENTE \n")
    print("> 4. ATRÁS\n")
    print("=====================================================")
    opcion2 = input("> Elegir opción: ")
    print("=====================================================\n\n")

    if opcion2 == ("0"):   ### Registrar cliente nuevo
        print("=====================================================")
        print("             >>> REGISTRAR CLIENTE <<<               ")
        print("=====================================================\n")
        documento = validarexistenciaclientes()
        nombreapellido = input("> Nombre y Apellido: ")
        telefono = validartelefono()
        direccion = input("> Dirección: ")
        agregarcliente(documento, nombreapellido, telefono, direccion)
        print("\n=====================================================")
        print("> El cliente", (nombreapellido) ,"se registró correctamente.")
        print("=====================================================\n\n")
        return submenu2()

    elif opcion2 == ("1"): ### Consultar estado del cliente
        print("=====================================================")
        print("              >>> BUSCAR CLIENTE <<<                 ")
        print("=====================================================\n")
        cliente = validarlistadoclientes()
        buscarestadocliente(cliente) 
        print("=====================================================\n\n")
        return submenu2() 

    elif opcion2 == ("2"): ### Modificar datos del cliente
        print("=====================================================")
        print("          >>> INGRESE EL DNI DEL CLIENTE <<<         ")
        print("=====================================================\n")
        dni = validarlistadoclientes()
        print("\n=====================================================\n\n")
        opcionsub2(dni)
        return submenu2()

    elif opcion2 == ("3"): ### Eliminar cliente
        print("=====================================================")
        print("          >>> INGRESE EL DNI DEL CLIENTE <<<         ")
        print("=====================================================\n")
        dni = validarlistadoclientes()
        buscarclienteeliminar(dni)
        copiararchivoclientes()
        return submenu2()

    elif opcion2 == ("4"): ### Atras
        return menu()

    else:                  ### Se ingresaron mal los datos
        print("-----------------------------------------------------")
        print("> La opción ingresada es incorrecta.")
        print("-----------------------------------------------------\n\n")
        return submenu2()

def opcionsub2(dni):    ### Sub menu de opciones2 > modificar datos cliente
    print("=====================================================")
    print("           >>> QUE DATO VA A MODIFICAR <<<           ")
    print("=====================================================")
    print("> 0. MODIFICAR TELEFONO <  > 1. MODIFICAR DIRECCIÓN <")
    print("                   > 2. ATRÁS <")
    print("=====================================================\n")
    opcion = input("> ")
    print("\n=====================================================\n\n")
    if opcion == ("0"):    ### Modificar el telefono
        print("=====================================================")
        print("           >>> INGRESE EL NÚMERO NUEVO <<<           ")
        print("=====================================================\n")
        modificartel(dni)
        copiararchivoclientes()
        return opcionsub2(dni)

    elif opcion == ("1"):  ### Modificar la direccion
        print("=====================================================")
        print("          >>> INGRESE LA DIRECCIÓN NUEVA <<<         ")
        print("=====================================================\n")
        direccion = input("> ")
        modificardir(dni, direccion)
        copiararchivoclientes()
        return opcionsub2(dni)
            
    elif opcion == ("2"): ### Atras
        return submenu2()

    else:              ### Se ingresaron mal los datos
        print("-----------------------------------------------------")
        print("> Error, opción inválida.")
        print("-----------------------------------------------------\n\n")
        return opcionsub2(dni)


##################################################################################################################################################

##########################################################   FUNCIONES CLIENTES   ################################################################

def agregarcliente(documento, nombreapellido, telefono, direccion): ### guarda los datos en clientes.txt
	with open("clientes.txt", "a") as c:
		c.write (str(documento) + "," + str(nombreapellido) + "," + str(telefono) + "," + str(direccion) + "," + ("N") + "," + ("N") + "," + "\n")
		c.close()
     
def buscarestadocliente(cliente):     ### Busca si el cliente ingresado tiene peliculas alquiladas
    with open("clientes.txt", "r") as c:
        linea = c.readline()
        while linea != "": 
            renglon = linea.split(',')
            if cliente == renglon[0] and ("O") == renglon[4]:
                c.close()
                print("\n=====================================================")
                print("> El cliente debe la película: " + renglon[5])
                print("=====================================================\n\n")
                return 
            linea = c.readline()
        c.close()
        print("\n=====================================================")
        print("> El cliente no posee películas alquiladas.")
        print("=====================================================\n\n")
        return    
        
def modificartel(dni):                ### Modifica el telefono del clietne
    telefono = validarnumero()
    with open("clientes.txt", "r") as rc:
        with open("clientescopia.txt", "w") as wc:
            linea = rc.readline()
            while linea != "":
                renglon = linea.split(',')
                if str(dni) == renglon[0]:
                    wc.writelines(renglon[0] + "," + renglon[1] + "," + telefono + "," + renglon[3] + "," + renglon [4] + "," + renglon [5] + "," + "\n")
                    print("\n=====================================================")
                    print("> Se han modificado los datos correctamente.")
                    print("=====================================================\n\n")
                else:
                    wc.write(linea)
                linea = rc.readline()
            wc.close()
        rc.close()
        return

def modificardir(dni, direccion):     ### Modifica la direccion del cliente
    with open("clientes.txt", "r") as rc:
        with open("clientescopia.txt", "w") as wc:
            linea = rc.readline()
            while linea != "":
                renglon = linea.split(',')
                if str(dni) == renglon[0]:
                    wc.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + direccion + "," + renglon [4] + "," + renglon [5] + "," + "\n" )
                    print("\n=====================================================")
                    print("> Se han modificado los datos correctamente.")
                    print("=====================================================\n\n")
                else:
                    wc.write(linea)
                linea = rc.readline()
            wc.close()
        rc.close()
        return

def eliminarcliente(dni):             ### Elimina el cliente y todos sus datos 
    with open("clientes.txt", "r") as rc:
        with open("clientescopia.txt", "w") as wc:
            linea = rc.readline()
            while linea != "":
                renglon = linea.split(',')
                if (str(dni)) != renglon[0]:
                    wc.write(linea)
                linea = rc.readline()    
            wc.close()
        rc.close()
        print("\n=====================================================")
        print("> El cliente fué eliminado.")
        print("=====================================================\n\n")
        return

def buscarclienteeliminar(cliente):   ### Busca el dni del cliente ingresado y revisa que no posea peliculas alquiladas antes de la eliminacion 
    with open("clientes.txt", "r") as c:
        linea = c.readline()
        while linea != "": 
            renglon = linea.split(',')
            if cliente == renglon[0] and renglon [4] == ("O"):
                c.close()
                print ("> " + renglon[1])
                print("\n=====================================================")
                print ("> No se puede eliminar, el cliente debe la pelicula " + (renglon[5]))
                print("=====================================================\n\n")
                return submenu2()       
            linea = c.readline()
        c.close()
    return eliminarcliente(cliente)       
           
def copiararchivoclientes():		  ### COPIA CLIENTES
	with open("clientescopia.txt", "r") as ccopia:
		with open("clientes.txt", "w") as coriginal:
			for registro in ccopia:
				coriginal.write(registro)
			ccopia.close()
		coriginal.close()

###############################################################   SUBMENU 3   ####################################################################

def submenu3 ():                            ### Opciones de gestion peliculas
    print("=====================================================")
    print("            >>> GESTION DE PELÍCULAS <<<             ")
    print("=====================================================\n")
    print("> 0. REGISTRAR PELÍCULA \n")
    print("> 1. CONSULTAR PELÍCULA \n")
    print("> 2. MODIFICAR DATOS DE LA PELÍCULA \n")
    print("> 3. ELIMINAR PELÍCULA \n")
    print("> 4. ATRÁS\n")
    print("=====================================================")
    opcion3 = input("> Elegir opción: ")
    print("=====================================================\n\n")

    if opcion3 == ("0"):   ### registrar una pelicula nueva
        print("=====================================================")
        print("             >>> REGISTRAR PELÍCULA <<<              ")
        print("=====================================================\n")
        codigo = validarexistenciapeliculas()
        titulo = input("\n> Título: ")
        genero = input("\n> Género: ")
        agregarpelicula(codigo, titulo, genero)
        print("\n=====================================================")
        print("> La película", (titulo) ,"se registró correctamente.")
        print("=====================================================\n\n")
        return submenu3()

    elif opcion3 == ("1"): ### consultar estado de pelicula
        print("=====================================================")
        print("              >>> BUSCAR PELÍCULAS <<<               ")
        print("=====================================================\n")
        pelicula = validarcodigo()
        consultarpeliculas(pelicula)
        return submenu3()

    elif opcion3 == ("2"): ### modificar datos de pelicula
        print("=====================================================")
        print("         >>> MODIFICAR DATOS DE PELÍCULA <<<         ")
        print("=====================================================\n")
        codigo = validarlistapeliculas()
        validarestadopeliculaeditar(codigo)
        opcionsub3(codigo)
        print("\n> Se han modificado los datos.")
        print("\n=====================================================\n\n")
        return submenu3()

    elif opcion3 == ("3"): ### eliminar pelicula
        print("=====================================================")
        print("         >>> INGRESE EL CODIGO DE BARRAS <<<         ")
        print("=====================================================\n")
        codigo = validarlistapeliculas()
        buscarpeliculaeliminar(codigo)
        copiararchivopeliculas()
        return submenu3()

    elif opcion3 == ("4"): ### Atras
        return menu()

    else:
        print("-----------------------------------------------------")
        print("> La opción ingresada es incorrecta.")
        print("-----------------------------------------------------\n\n")
        return submenu3()

def opcionsub3(codigo):
    print("=====================================================")
    print("           >>> QUE DATO VA A MODIFICAR <<<           ")
    print("=====================================================\n")
    print("> 0. MODIFICAR CODIGO DE BARRA \n")
    print("> 1. MODIFICAR TÍTULO \n")
    print("> 2. MODIFICAR GÉNERO \n")
    print("> 3. ATRÁS\n")
    print("=====================================================")
    opcion = input("> ")
    print("=====================================================\n\n")
    
    if opcion == ("0"): ### Modificar codigo
        print("=====================================================")
        print("           >>> INGRESE EL CÓDIGO NUEVO <<<           ")
        print("=====================================================\n")
        codigon = validarcodigo()
        modificarcodigo(codigo, codigon)
        copiararchivopeliculas()
        return opcionsub3(codigo)
        
    elif opcion == ("1"):  #Modificar titulo
        print("=====================================================")
        print("           >>> INGRESE EL TÍTULO NUEVO <<<           ")
        print("=====================================================\n")
        titulo = input("> ")
        modificartitulo(codigo, titulo)
        copiararchivopeliculas()
        return opcionsub3(codigo)

    elif opcion == ("2"):  ###Modificar genero
        print("=====================================================")
        print("           >>> INGRESE EL GÉNERO NUEVO <<<           ")
        print("=====================================================\n")
        genero = input("> ")
        modificargenero(codigo, genero)
        copiararchivopeliculas()
        return opcionsub3(codigo)

    elif opcion == ("3"): ### Atras
        return submenu3()

    else:
        print("-----------------------------------------------------")
        print("> La opción ingresada es incorrecta.")
        print("-----------------------------------------------------\n\n")
        return opcionsub3(codigo)

##################################################################################################################################################

##########################################################   FUNCIONES PELICULAS   ###############################################################

def agregarpelicula(codigodebarra, titulo, genero):  ### Agregar pelicula
	with open("peliculas.txt", "a") as clientes:
		clientes.write(str(codigodebarra) + "," + str(titulo) + "," + str(genero) + "," + "N" + "," + "N" + "," + "\n")
		clientes.close()

def consultarpeliculas(pelicula):                    ### Buscar datos de una pelicula
    with open("peliculas.txt", "r") as p:
        linea = p.readline()
        while linea != "":
            renglon = linea.split(',')
            if pelicula == renglon[0] :
                p.close()
                return print (("> TÍTULO: ") + (renglon[1]) + ("\n") + ("> GÉNERO: ") + (renglon[2]) + ("\n") + ("> ESTADO: ") + (estadopel(renglon[3])) + ("\n") + ("> DNI: ") + (estadodni(renglon[4])))
            linea = p.readline()
        p.close()
        print("\n=====================================================")
        print("> La película no está registrada.")
        print("=====================================================\n\n")
        return 

def estadopel(estado):
    if estado == ("P"):
        return ("Alquilada")
    else:
        return ("Disponible")

def estadodni(estado):
    if estado == ("N"):
        return ("Ninguno")
    else:
        return estado

def modificarcodigo(codigo, codigon):                ### Modificar codigo de barras
    with open("peliculas.txt", "r") as rp:
        with open("peliculascopia.txt", "w") as wp:
            linea = rp.readline()
            while linea != "":
                renglon = linea.split(',')
                if str(codigo) == renglon[0] and renglon[3] == ("N"):
                    wp.writelines(str(codigon) + "," + renglon[1] + "," + renglon[2] + "," + renglon[3]+ "," + renglon[4] + "," + "\n")
                    print("\n=====================================================")
                    print("> Se han modificado los datos correctamente.")
                    print("=====================================================\n\n")
                    return
                else:
                    wp.write(linea)
                linea = rp.readline()
            wp.close()
        rp.close()
        return      
        
def modificartitulo(codigo, titulo):                 ### Modificar titulo
    with open("peliculas.txt", "r") as rp:
        with open("peliculascopia.txt", "w") as wp:
            linea = rp.readline()
            while linea != "":
                renglon = linea.split(',')
                if str(codigo) == renglon[0]:
                    wp.writelines(renglon[0] + "," + str(titulo) + "," + renglon[2] + "," + renglon [3]+ "," + renglon [4] + "," + "\n")
                    print("\n=====================================================")
                    print("> Se han modificado los datos correctamente.")
                    print("=====================================================\n\n")
                    return
                else:
                    wp.write(linea)
                linea = rp.readline()
            wp.close()
        rp.close()
        return
        
def modificargenero(codigo, genero):                 ### Modificar genero
    with open("peliculas.txt", "r") as rp:
        with open("peliculascopia.txt", "w") as wp:
            linea = rp.readline()
            while linea != "":
                renglon = linea.split(',')
                if str(codigo) == renglon[0]:
                    wp.writelines(renglon[0] + "," + renglon[1] + "," + str(genero) + "," + renglon [3]+ "," + renglon [4] + "," + "\n")
                    print("\n=====================================================")
                    print("> Se han modificado los datos correctamente.")
                    print("=====================================================\n\n")
                    return
                else:
                    wp.write(linea)
                linea = rp.readline()
            wp.close()
        rp.close()
        return
        
def eliminarpelicula(codigo):                        ### Eliminar pelicula
    with open("peliculas.txt", "r") as rp:
        with open("peliculascopia.txt", "w") as wp:
            linea = rp.readline()
            while linea != "":
                renglon = linea.split(',')
                if codigo != renglon[0]:
                    wp.write(linea)
                linea = rp.readline()
            wp.close()
        rp.close()
        print("\n=====================================================")
        print("> La película fué eliminada.")
        print("=====================================================\n\n")
        return 
		        
def buscarpeliculaeliminar(codigo):                  ### Busca si la pelicula esta alquilada 
    with open("peliculas.txt", "r") as p:
        linea = p.readline()
        while linea != "": 
            renglon = linea.split(',')
            if codigo == renglon[0] and renglon[3] == ("P"):
                p.close()
                print(("> " + renglon[1]))
                print("\n=====================================================")
                print ("> No se puede eliminar, la pelicula está alquilada por el cliente " + (renglon[4]))
                print("=====================================================\n\n")
                return submenu3()
            linea = p.readline()
        p.close()
    return eliminarpelicula(codigo)
        
def copiararchivopeliculas():	                     ### COPIA PELICULAS	
	with open("peliculascopia.txt", "r") as fcopia:
		with open("peliculas.txt", "w") as foriginal:
			for registro in fcopia:
				foriginal.write(registro)
			fcopia.close()
		foriginal.close()

##################################################################################################################################################

############################################################   VALIDACIONES   ####################################################################

def validartelefono():         ### Valida que se ingresen solo numeros
    tel = input("> Teléfono: ")
    while True:
        try:
            tel = int(tel) 
            return tel
        except ValueError:
            print("\n-----------------------------------------------------")
            print ("> Teléfono incorrecto, ingrese solo numeros." ) 
            print("-----------------------------------------------------\n")

            return validartelefono()

def validardni ():             ### Comprueba la longitud del DNI 
    dni = input("> DNI: ")
    while True:
        try:
            dni = int(dni) 
            longitud = (len(str(dni)))
            if longitud <= 8 and longitud >= 7 :
                return str(dni)
            else:
                print("\n-----------------------------------------------------")
                print("> El DNI es incorrecto.")
                print("-----------------------------------------------------\n")
                return validardni()
        except ValueError:
            print("\n-----------------------------------------------------")
            print("> DNI incorrecto, ingrese solo numeros." ) 
            print("-----------------------------------------------------\n")
            return validardni()
        
def validarnumero ():          ### Comprueba que se ingresen solo numeros
    telefono = input("> ")
    while True:
        try:
            int(telefono) 
            return telefono
        except ValueError:
            print("\n-----------------------------------------------------")
            print ("> Error, ingrese solo numeros." ) 
            print("-----------------------------------------------------\n")
            
            return validarnumero()

def validarcodigo ():          ### Comprueba la longitud del codigo y que sean solo numeros
    codigo = input("> Código: ")
    while True:
        try:
            codigo = int(codigo) 
            longitud = (len(str(codigo)))
            if longitud == 13:
                return str(codigo)
            else:
                print("\n-----------------------------------------------------")
                print ("> El codigo es incorrecto.")
                print("-----------------------------------------------------\n")
                return validarcodigo()
        except ValueError:
            print("\n-----------------------------------------------------")
            print ("> Codigo incorrecto, ingrese solo numeros." ) 
            print("-----------------------------------------------------\n")
            return validarcodigo()
        
def validarlistadoclientes(): ### Comprueba la existencia del cliente
    ingreso = validardni()
    with open("clientes.txt", "r") as c:
        linea = c.readline()
        while linea != "": 
            renglon = linea.split(',')
            if ingreso == renglon[0]:
                c.close()
                return ingreso
            linea = c.readline()
        c.close()
        print("\n-------------------------------------------------")
        print("> No se encontró el cliente.")
        print("-------------------------------------------------\n")      
        return validarlistadoclientes()

def validarlistapeliculas():  ### Comprueba la existencia de la pelicula
    ingreso = validarcodigo()
    with open("peliculas.txt", "r") as p:
        linea = p.readline()
        while linea != "": 
            renglon = linea.split(',')
            if ingreso == renglon[0]:
                p.close()
                return ingreso 
            linea = p.readline()
        p.close()
        print("\n-----------------------------------------------------")
        print ("> No se encontró la película.")
        print("-----------------------------------------------------\n")
        return validarlistapeliculas()

def validarestadocliente(ingreso):   ### Comprueba el estado del cliente
    with open("clientes.txt", "r") as c:
        linea = c.readline()
        while linea != "": 
            renglon = linea.split(',')
            if ingreso == renglon[0] and ("O") == renglon[4]:
                c.close()
                print("\n=====================================================")
                print("> El cliente debe la película: " + renglon[5])
                print("=====================================================\n\n")
                return alquilerpeliculas()
            linea = c.readline()
        c.close()
    return ingreso

def validarestadopelicula(ingreso):  ### Comprueba el estado de la pelicula
    with open("peliculas.txt", "r") as p:
        linea = p.readline()
        while linea != "": 
            renglon = linea.split(',')
            if ingreso == renglon[0] and ("P") == renglon[3]:
                p.close()
                print("\n=====================================================")
                print("> La película está alquilada por: " + (renglon[4]))
                print("=====================================================\n\n")
                return  alquilerpeliculas()
            linea = p.readline()
        p.close()
        print("")
    return ingreso

def validarestadopeliculaeditar(ingreso):  ### Comprueba el estado de la pelicula
    with open("peliculas.txt", "r") as p:
        linea = p.readline()
        while linea != "": 
            renglon = linea.split(',')
            if ingreso == renglon[0] and ("P") == renglon[3]:
                p.close()
                print("\n=====================================================")
                print("> La película no se puede modificar porque se encuentra en alquiler.")
                print("=====================================================\n\n")
                return  alquilerpeliculas()
            linea = p.readline()
        p.close()
        print("")
    return ingreso

def validarexistenciaclientes(): ### Comprueba la existencia del cliente
    ingreso = validardni()
    with open("clientes.txt", "r") as c:
        linea = c.readline()
        while linea != "": 
            renglon = linea.split(',')
            if ingreso == renglon[0]:
                c.close()
                print("\n=====================================================")
                print("> El cliente ya existe.")
                print("=====================================================\n\n")
                return submenu2()
            linea = c.readline()
        c.close()      
        return ingreso

def validarexistenciapeliculas():  ### Comprueba la existencia de la pelicula
    ingreso = validarcodigo()
    with open("peliculas.txt", "r") as p:
        linea = p.readline()
        while linea != "": 
            renglon = linea.split(',')
            if ingreso == renglon[0]:
                p.close()
                print("\n=====================================================")
                print ("> La película ya existe.")
                print("=====================================================\n\n")
                return submenu3() 
            linea = p.readline()
        p.close()
        return ingreso

##################################################################################################################################################

#################################################################   INICIO   #####################################################################

menu() ### Muestra las opciones 0,1,2,3
       ### Permite navegar en ellas 

##################################################################################################################################################

