import os

# Ruta de los archivos de texto plano
DatosDeUsuarios = "Usuarios_y_Pines.txt"
ArchivoConfig = "config.txt"


def comprobarExistencia():
    if not os.path.exists(ArchivoConfig):
        clave = open(ArchivoConfig, 'w')
        clave.write("x")
        clave.close()


def solicitar_pin_especial(matriz):
    comprobarExistencia()
    while True:
        pin = input("\nIngrese el PIN especial: ")
        clave = open(ArchivoConfig, 'r')
        config = clave.read()
        clave.close()
        if pin == str(config):
            print("\nBienvenido al modo especial")
            mostrar_menu(matriz)
            break
            # mostrar características adicionales
        else:
            print("Contraseña incorrecta.")
            break

def modificar_tipos_de_cambio():
    # código para modificar tipos de cambio
    pass

def mostrar_menu(matriz):
    while True:
        print("1. Eliminar usuario")
        print("2. Modificar tipos de cambio")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            eliminar_usuario(matriz)
        elif opcion == "2":
            modificar_tipos_de_cambio()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")
            mostrar_menu(matriz)


# Comprobar si los archivos de texto plano existen, y crearlos si no existen
if not os.path.exists(DatosDeUsuarios):
    datos = open(DatosDeUsuarios, 'w')
    datos.write("usuario1:contrasena1\nusuario2:contrasena2\n")
    datos.close()

def eliminar_usuario(matriz):
    print(matriz)
    cedula = input("Ingrese el número de cédula del usuario a eliminar: ")
    if os.path.exists(cedula):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if str(matriz[i][j]) == cedula:
                    del matriz[i]
                else:
                    print("La cédula no está registrada.")
        archivo = open(DatosDeUsuarios, "w")
        for i in range(len(matriz)):
            for j in range(3):
                archivo.write(matriz[i][j])
                archivo.write("\n")
        archivo.close()
        print(matriz)

                #reescribir en archivo
        #archivo.close()
        #os.remove(os.path)
        print("El usuario ha sido eliminado")
    else:
        print("El usuario no existe")