# Biblioteca de la opción de Configuración Avanzada.
# Opción 3 del menú en programaPrincipal
# Solicita un pin especial que se crea y guarda en un archivo al iniciar el programa
# Permite eliminar un usuario y aleterar los tipos de cambio.

#Bibliotecas importadas
import comun

#***********************************************************************************************************************

# Solicita y valida el pin especial.
def solicitarPinEspecial(usuariosYPines, pinEspecial, tiposCambio):
    pin = input("\nIngrese el PIN especial: ")
    if pin == pinEspecial:
        mostrarMenu(usuariosYPines, tiposCambio)
    else:
        print("PIN incorrecto.")

#***********************************************************************************************************************

# Ciclo del menú de Configuración Avanzada.
def mostrarMenu(usuariosYPines, tiposCambio):
    while True:
        print("\nBienvenido al modo especial.")
        print("1. Eliminar usuario")
        print("2. Modificar tipos de cambio")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            eliminarUsuario(usuariosYPines)
        elif opcion == "2":
            modificarTiposCambio(tiposCambio)
        elif opcion == "3":
            return

#***********************************************************************************************************************

# Elimina un usuario de la matriz y de la estructura de archivos y actualiza el archivo de texto de usuarios y pines.
def eliminarUsuario(matriz):
    print("\nEliminando un usuario")
    cedula = comun.solicitaCedula()
    if cedula != "0":
        # Eliminar el usuario de la matriz y de la estructura de archivos.
        encontrada = comun.eliminaUsuario(cedula, matriz)
        if encontrada:
            # Sobrescribir el archivo de texto con la matriz actualizada.
            comun.guardaUsuariosYPines(matriz)
            print("El usuario ha sido eliminado")
        else:
            print("El usuario no existe")

#***********************************************************************************************************************

# Menú de los tipos de conversión.
def modificarTiposCambio(tiposCambio):
    #print("\n¿Qué tipo de cambio desea modificar?")
    #print("1. Compra de colones")
    #print("2. Venta de colones")
    #print("3. Compra de dólares")
    #print("4. Venta de dólares")
    #print("5. Compra de bitcoin")
    #print("6. Venta de bitcoin")
    #if opcion == "1":
    #    tiposCambio[0] = comun.campturaMonto("Ingrese el nuevo valor de compra de colones: ")
    #elif opcion == "2":
    #    tiposCambio[1] = comun.campturaMonto("Ingrese el nuevo valor de venta de colones: ")
    #elif opcion == "3":
    #    tiposCambio[2] = comun.campturaMonto("Ingrese el nuevo valor de compra de dólares: ")
    #elif opcion == "4":
    #    tiposCambio[3] = comun.campturaMonto("Ingrese el nuevo valor de venta de dólares: ")
    #elif opcion == "5":
    #    tiposCambio[4] = comun.campturaMonto("Ingrese el nuevo valor de compra de bitcoin: ")
    #elif opcion == "6":
    #    tiposCambio[5] = comun.campturaMonto("Ingrese el nuevo valor de venta de bitcoin: ")
    while True:
        print("\nTipos de conversión existentes:")
        print(" 1. De colon a bitcoin (venta de colones hacia cuenta bitcoin)")
        print(" 2. De colon a dólar (venta de colones hacia cuenta dólares)")
        print(" 3. De bitcoin a colones (venta de bitcoin hacia cuenta colones)")
        print(" 4. De bitcoin a dólar (venta de colones hacia cuenta dólares)")
        print(" 5. De dólares a colones (venta de dólares hacia cuenta colones)")
        print(" 6. De dólares a bitcoin (venta de dólares hacia cuenta bitcoin)")
        print(" 7. De colon a bitcoin (compra de colones desde cuenta bitcoin)")
        print(" 8. De colon a dólar (compra de colones desde cuenta dólares)")
        print(" 9. De bitcoin a colones (compra de bitcoin desde cuenta colones)")
        print("10. De bitcoin a dólar (compra de colones desde cuenta dólares)")
        print("11. De dólares a colones (compra de dólares desde cuenta colones)")
        print("12. De dólares a bitcoin (compra de dólares desde cuenta bitcoin)")
        print("13. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            tiposCambio[0] = comun.capturaMonto("Ingrese el el factor de colon a bitcoin (venta de colones hacia cuenta bitcoin): ", 0)
        elif opcion == "2":
            tiposCambio[1] = comun.capturaMonto("Ingrese el el factor de colon a dólar (venta de colones hacia cuenta dólares): ", 0)
        elif opcion == "3":
            tiposCambio[2] = comun.capturaMonto("Ingrese el el factor de bitcoin a colones (venta de bitcoin hacia cuenta colones): ", 0)
        elif opcion == "4":
            tiposCambio[3] = comun.capturaMonto("Ingrese el el factor de bitcoin a dólar (venta de colones hacia cuenta dólares): ", 0)
        elif opcion == "5":
            tiposCambio[4] = comun.capturaMonto("Ingrese el el factor de dólares a colones (venta de dólares hacia cuenta colones): ", 0)
        elif opcion == "6":
            tiposCambio[5] = comun.capturaMonto("Ingrese el el factor de dólares a bitcoin (venta de dólares hacia cuenta bitcoin): ", 0)
        elif opcion == "7":
            tiposCambio[6] = comun.capturaMonto("Ingrese el el factor de colon a bitcoin (compra de colones desde cuenta bitcoin): ", 0)
        elif opcion == "8":
            tiposCambio[7] = comun.capturaMonto("Ingrese el el factor de colon a bitcoin (compra de colones desde cuenta bitcoin): ", 0)
        elif opcion == "9":
            tiposCambio[8] = comun.capturaMonto("Ingrese el el factor de colon a dólar (compra de colones desde cuenta dólares): ", 0)
        elif opcion == "10":
            tiposCambio[9] = comun.capturaMonto("Ingrese el el factor de bitcoin a dólar (compra de colones desde cuenta dólares): ", 0)
        elif opcion == "11":
            tiposCambio[10] = comun.capturaMonto("Ingrese el el factor de dólares a colones (compra de dólares desde cuenta colones): ", 0)
        elif opcion == "12":
            tiposCambio[11] = comun.capturaMonto("Ingrese el el factor de dólares a bitcoin (compra de dólares desde cuenta bitcoin): ", 0)
        elif opcion == "13":
            # guardar cambios en el archivo.
            with open(comun.NombreArchivoTC, "w") as archivoTiposCambio:
                for i in range(len(tiposCambio)):
                    archivoTiposCambio.write(str(tiposCambio[i]) + "\n")
            break
        else:
            print("Opción inválida.")
