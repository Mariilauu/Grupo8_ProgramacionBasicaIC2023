# Programa Principal
# Aquí está el menú principal
# #Aquí se corre el programa, se crean los archivos necesarios y se importan los archivos que se utilizaran.

# Bibliotecas importadas
import registroNuevoUsuario
import configuracionAvanzada
import usuarioRegistrado
import comun
import os

#***********************************************************************************************************************

# Se lee el archivo de usuarios y pines y se guarda en una matriz.
if os.path.exists(comun.NombreArchivoUsuarios):
    archivo = open(comun.NombreArchivoUsuarios, "r")
    arreglo = archivo.readlines()
    archivo.close()
    todoEnUno = [n.rstrip() for n in arreglo]
    usuariosYPines = [todoEnUno[i:i + 3] for i in range(0, len(todoEnUno), 3)]
else:
    archivo = open(comun.NombreArchivoUsuarios, "w")
    archivo.close()
    usuariosYPines = []
#print(usuariosYPines)

#***********************************************************************************************************************

# Se lee el archivo con el pin especial y se guarda en una variable
if os.path.exists(comun.NombreArchivoConfig):
    archivo = open(comun.NombreArchivoConfig, "r")
    arreglo = archivo.readlines()
    pinEspecial = arreglo[0].rstrip()
    archivo.close()
else:
    archivo = open(comun.NombreArchivoConfig, "w")
    pinEspecial = "1234"
    archivo.write(pinEspecial)
    archivo.close()
#print(pinEspecial)

#***********************************************************************************************************************

# Se lee el archivo de tipos de cambio y se guarda en una lista.
if os.path.exists(comun.NombreArchivoTC):
    archivo = open(comun.NombreArchivoTC, "r")
    arreglo = archivo.readlines()
    archivo.close()
    tiposCambio = [n.rstrip() for n in arreglo]
else:
    tiposCambio = ["13313112.14", "560", "13313112.14", "23662.60", "550", "0.0000428859", "13313112.14", "560", "13313112.14", "23662.60", "550", "0.0000428859"]
    archivo = open(comun.NombreArchivoTC, "w")
    for i in range(len(tiposCambio)):
        archivo.write(str(tiposCambio[i]) + "\n")
    archivo.close()
#print(tiposCambio)

#***********************************************************************************************************************

# Ciclo del menú principal
while True:
    # Menú Principal
    # Presentará las opciones que se pueden realizar en el cajero.
    print("\nBienvenido.\nMenú Principal")
    print("Por favor digite el número de acuerdo a la opción que aparece en pantalla.")
    opcionMenuPrincipal = input("1. Registrar nuevo usuario\n2. Usuario Registrado\n3. Configuración Avanzada\n4. Salir\nDigite su opción aquí: ")
    if opcionMenuPrincipal == "1":
        registroNuevoUsuario.registroNuevoUsuario(usuariosYPines, tiposCambio)
    elif opcionMenuPrincipal == "2":
        usuarioRegistrado.autenticarUsuario(usuariosYPines, tiposCambio)
    elif opcionMenuPrincipal == "3":
        configuracionAvanzada.solicitarPinEspecial(usuariosYPines, pinEspecial, tiposCambio)
    elif opcionMenuPrincipal == "4":
        break
    else:
        print("El valor ingresado no corresponde a ninguna de las opciones anteriores.")
