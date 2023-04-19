import os


# Ruta de los archivos de texto plano
DatosDeUsuarios = "Usuarios_y_Pines.txt"
ArchivoConfig = "config.txt"
PinEspecial = "1234" 



def solicitar_pin_especial(matriz):
    while True:
        pin = input("Ingrese el PIN especial: ")
        if pin == PinEspecial:
            print("\nBienvenido al modo especial")
            mostrar_menu(matriz)
            break
        else:
            print("PIN incorrecto. Vuelva a intentarlo.")

def modificar_tipos_de_cambio():
    # matriz con los tipos de cambio
    tipos_cambio = [
        ["1. Compra de colones", 0.5],
        ["2. Venta de colones", 0.6],
        ["3. Compra de dólares", 8.0],
        ["4. Venta de dólares", 8.5],
        ["5. Compra de bitcoin", 5000],
        ["6. Venta de bitcoin", 5500]
    ]

    while True:
        print("¿Qué tipo de cambio desea modificar?")
        print("1. Compra de colones")
        print("2. Venta de colones")
        print("3. Compra de dólares")
        print("4. Venta de dólares")
        print("5. Compra de bitcoin")
        print("6. Venta de bitcoin")
        print("7. Salir")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            tipos_cambio[0][1] = float(input("Ingrese el nuevo valor de compra de colones: "))
        elif opcion == "2":
            tipos_cambio[1][1] = float(input("Ingrese el nuevo valor de venta de colones: "))
        elif opcion == "3":
            tipos_cambio[2][1] = float(input("Ingrese el nuevo valor de compra de dólares: "))
        elif opcion == "4":
            tipos_cambio[3][1] = float(input("Ingrese el nuevo valor de venta de dólares: "))
        elif opcion == "5":
            tipos_cambio[4][1] = float(input("Ingrese el nuevo valor de compra de bitcoin: "))
        elif opcion == "6":
            tipos_cambio[5][1] = float(input("Ingrese el nuevo valor de venta de bitcoin: "))
        elif opcion == "7":
            # guardar cambios en archivo
            with open("tiposDeCambio.txt", "w") as archivo_tipos_cambio:
                for i in range(len(tipos_cambio)):
                    archivo_tipos_cambio.write(str(tipos_cambio[i][0]) + ":" + str(tipos_cambio[i][1]) + "\n")
            break
        else:
            print("Opción inválida")

def mostrar_menu(matriz):
    comprobarSiExistenUsuarios()
    while True:
        print("1. Eliminar usuario")
        print("2. Modificar tipos de cambio")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            eliminar_usuario(matriz)
        elif opcion == "2":
            modificar_tipos_de_cambio()
        else:
            return


# Comprobar si los archivos de texto plano existen, y crearlos si no existen
def comprobarSiExistenUsuarios():
    if not os.path.exists(DatosDeUsuarios):
        print("No hay usuarios registrados.")


def eliminar_usuario(matriz):
    cedula = input("Ingrese el número de cédula del usuario a eliminar: ")
    encontrado = False
    for i in range(len(matriz)):
        if matriz[i][0] != cedula:
            matriz.append(matriz[i])
        else:
            encontrado = True
            # Eliminar carpeta con la cédula del usuario si existe
            carpeta_usuario = cedula
            if os.path.exists(carpeta_usuario):
                contenido = os.listdir(carpeta_usuario)
                for archivo in contenido:
                    ruta_archivo = os.path.join(carpeta_usuario, archivo)
                    if os.path.isfile(ruta_archivo):
                        os.remove(ruta_archivo)
                    elif os.path.isdir(ruta_archivo):
                        os.rmdir(ruta_archivo)
                os.rmdir(carpeta_usuario)
    if encontrado:
        # Sobrescribir el archivo de texto con la matriz actualizada
        archivo = open(DatosDeUsuarios, "r+")
        archivo.truncate(0) # borrar todo el contenido del archivo
        for k in range(len(matriz)):
            for j in range(len(matriz[k])):
                archivo.write(matriz[k][j])
                archivo.write("\n")
        archivo.close()
        print("El usuario ha sido eliminado")
    else:
        print("El usuario no existe")
    # Reemplazar la matriz actual con la matriz actualizada
    matriz.clear()
    matriz.extend(matriz)





