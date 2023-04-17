import os
usuarios = {}
CarpetaUsuarios = "Usuarios_y_Pines.txt"


def autenticarUsuario(matriz):
    while True:
        if os.path.exists(CarpetaUsuarios):
            cedula = ingresarCedula(matriz)
            if cedula == 0:
                print("Ha execido el número de intentos máximos.")
                break
            else:
                pin = ingresarPin(matriz)
                if pin == 0:
                    print("Ha execido el número de intentos máximos.")
                    break

        else:
            print("Aún no existen usuarios registrados.")
            break

def ingresarCedula(matriz):
    intentos = 3
    while intentos > 0:
        cedula = input("Ingrese su cedula: ")
        if cedula.isdigit() and len(cedula) == 9:
            for i in range(len(matriz)):
                for j in range(3):
                    if matriz[i][j] == cedula:
                        break
                    else:
                        print("La cédula ingresada no está registrada.")
        else:
            intentos -= 1
            print("La cédula ingresada es incorrecta.")
            incorrecto = 0
            return incorrecto


def ingresarPin(matriz):
    intentos = 3
    while intentos > 0:
        pin = input("Ingrese su PIN: ")
        for i in range(len(matriz)):
            for j in range(3):
                if matriz[i][2] == pin:
                    nombre = [i][1]
                    cedula = [i][j]
                    print(f"¡Bienvenido {nombre}!")
                    submenu(cedula)
        else:
            intentos -= 1
            print("El PIN ingresado es incorrecto")
            incorrecto = 0
            return incorrecto



def submenu(usuario):
    while True:
        print("""
            1. Retirar dinero
            2. Depositar dinero
            3. Ver saldo actual
            4. Pagar servicios
            5. Compra/Venta de Divisas
            6. Eliminar usuario
            7. Salir""")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            retirar_dinero(usuario)
        elif opcion == "2":
            depositar_dinero(usuario)
        elif opcion == "3":
            ver_saldo(usuario)
        elif opcion == "4":
            pagar_servicio(usuario)
        elif opcion == "5":
            compra_venta_divisas(usuario)
        elif opcion == "6":
            eliminar_usuario(usuario)
        elif opcion == "7":
            break
        else:
            print("La opción ingresada no corresponde a ninguna de las anteriores.")


def retirar_dinero(usuario):
    while True:
        print("1. Dolares\n2. Colones\n3. Bitcoins")
        opcion= input("Por favor ingrese la cuenta de la que desea retirar dinero.\nOpción: ")
        if opcion == "1":
            print("Cuenta en Dolares")
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= usuario["saldo"]:
                usuario["saldo"] -= monto
                print(f"Retiro exitoso. Saldo actual: {usuario['saldo']}")
            else:
                print("Saldo insuficiente.")
        elif opcion == "2":
            print("Cuenta en Colones")
        elif opcion == "3":
            print("Cuenta en Bitcoins")
        else:
            print("La opción ingresada no corresponde a ninguna de las anteriores.")



def depositar_dinero(usuario):
    monto = float(input("Ingrese el monto a depositar: "))
    usuario["saldo"] += monto
    print(f"Deposito exitoso. Saldo actual: {usuario['saldo']}")


def ver_saldo(usuario):
    print(f"Su saldo actual es: {usuario['saldo']}")


def pagar_servicio(usuario):
    servicio = input("Ingrese el nombre del servicio a pagar: ")
    monto = float(input("Ingrese el monto a pagar: "))
    if monto <= usuario["saldo"]:
        usuario["saldo"] -= monto
        usuario["servicios"][servicio] = monto
        print(f"Pago de servicio exitoso. Saldo actual: {usuario['saldo']}")
    else:
        print("Saldo insuficiente.")


def compra_venta_divisas(usuario):
    print("Funcion no implementada.")


def eliminar_usuario():
    cedula = input("Ingrese la cedula del usuario a eliminar: ")
    if cedula in usuarios:
        del usuarios[cedula]
        print("Usuario eliminado exitosamente.")
    else:
        print("Usuario no encontrado.")

        
        
        
        
