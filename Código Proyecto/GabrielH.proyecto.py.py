
import getpass

# Variable global para almacenar la información del usuario
usuario = {}
cargar_informacion = {}
usuarios = {}

def autenticar_usuario():
    # Pedir información al usuario
    intentos = 0
    while True:
        cedula = input("Por favor, ingrese su número de cédula: ")
        if len(cedula) == 9 and cedula.isdigit():
            pin = input("Ingrese su PIN: ")
            # Leer archivo de usuarios y buscar la información correspondiente
            with open("usuarios.txt", "r") as archivo:
                for linea in archivo:
                    campos = linea.strip().split(",")
                    if campos[0] == cedula and campos[1] == pin:
                        print(f"Bienvenido {campos[2]} {campos[3]}!")
                        # Cargar la información del usuario y almacenarla en la variable global
                        global usuario
                        usuario["cedula"] = cedula
                        usuario["nombre"] = campos[2]
                        usuario["apellido"] = campos[3]
                        usuario["saldo"] = float(campos[4])
                        usuario["servicios"] = {}
                        informacion = cargar_informacion(cedula)
                        if informacion:
                            for linea in informacion:
                                campos = linea.strip().split(",")
                                usuario["servicios"][campos[0]] = float(campos[1])
                        return True
            # Si no se encontró al usuario, se aumenta el contador de intentos
            intentos += 1
            print("Cédula o PIN incorrectos. Por favor, inténtelo de nuevo.")
        else:
            intentos += 1
            print("Número de cédula inválido. Por favor, inténtelo de nuevo.")


def retirar_dinero(usuario1):
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= usuario["saldo"]:
        usuario["saldo"] -= monto
        print(f"Retiro exitoso. Saldo actual: {usuario['saldo']}")
    else:
        print("Saldo insuficiente.")


def depositar_dinero(usuario2):
    monto = float(input("Ingrese el monto a depositar: "))
    usuario["saldo"] += monto
    print(f"Deposito exitoso. Saldo actual: {usuario['saldo']}")


def ver_saldo(usuario3):
    print(f"Su saldo actual es: {usuario['saldo']}")


def pagar_servicio(usuario4):
    servicio = input("Ingrese el nombre del servicio a pagar: ")
    monto = float(input("Ingrese el monto a pagar: "))
    if monto <= usuario["saldo"]:
        usuario["saldo"] -= monto
        usuario["servicios"][servicio] = monto
        print(f"Pago de servicio exitoso. Saldo actual: {usuario['saldo']}")
    else:
        print("Saldo insuficiente.")


def compra_venta_divisas(usuario5):
    print("Funcion no implementada.")


def eliminar_usuario(usuario6):
    cedula = input("Ingrese la cedula del usuario a eliminar: ")
    if cedula in usuarios:
        del usuarios[cedula]
        print("Usuario eliminado exitosamente.")
    else:
        print("Usuario no encontrado.")

def salir(usuario7):
    print("selecciono salir,vuelva a cargar el programa")

while True:
    usuario =(int("Que opcion desea\n"))
if opcion == "1\n":
    retirar_dinero(usuario1)
elif opcion == "2\n":
    depositar_dinero(usuario2)
elif opcion == "3\n":
   ver_saldo(usuario3)
elif opcion == "4\n":
   pagar_servicio(usuario4)
elif opcion == "5\n":
   compra_venta_divisas(usuario5)
elif opcion == "6\n":
   eliminar_usuario(usuario6)
else:
    opcion == "7\n"
    salir(usuario7)


