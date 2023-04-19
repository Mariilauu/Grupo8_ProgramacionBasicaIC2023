import registro_nuevo_usuario
import configuracion_avanzada
import usuariso_registrados
#import Proyecto

#creo que aquí hay un error
try:
    archivo = open("Usuarios_y_Pines.txt", "r")
    arreglo = archivo.readlines()
    archivo.close()
    todoEnUno = [n.rstrip() for n in arreglo]
    usuariosYPines = [todoEnUno[i:i + 3] for i in range(0, len(todoEnUno), 3)]
except FileNotFoundError:
    archivo = open("Usuarios_y_Pines.txt", "w")
    archivo.close()
    usuariosYPines = []



while True:
    # Menú Principal
    # Presentará las opciones que se pueden realizar en el cajero.
    print("\nBienvenido.\nMenú Principal")
    print("Por favor digite el número de acuerdo a la opción que aparece en pantalla.")
    opcionMenuPrincipal = input("1. Registrar nuevo usuario\n2. Usuario Registrado\n3. Configuración Avanzada\n4. Salir\nDigite su opción aquí: ")
    if opcionMenuPrincipal == "1":
        registro_nuevo_usuario.registroNuevoUsuario(usuariosYPines)
    elif opcionMenuPrincipal == "2":
        usuariso_registrados.autenticarUsuario(usuariosYPines)
    elif opcionMenuPrincipal == "3":
        configuracion_avanzada.solicitar_pin_especial(usuariosYPines)
    elif opcionMenuPrincipal == "4":
        break
    else:
        print("El valor ingresado no corresponde a ninguna de las opciones anteriores.")
