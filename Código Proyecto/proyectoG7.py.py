
usuarios = []

# Solicitamos al usuario que ingrese su nombre
nombre = input("Por favor, ingrese su nombre: ")

# Agregamos la información del usuario a la lista
usuarios.append({"nombre": nombre})

# Mostramos un mensaje de confirmación
print("¡Hola, {}! Tu información ha sido guardada correctamente.".format(nombre))

# Para cargar la información de los usuarios desde el arreglo
def cargar_usuarios():
    return usuarios
# Después de cargar los usuarios
usuarios = cargar_usuarios()

if len(usuarios) == 0:
    print("No hay usuarios registrados")
    # Volver al menú principal
    # Continuar con la autenticación de usuarios
# Después de verificar que hay usuarios registrados
intentos_cedula = 3
intentos_pin = 3

while intentos_cedula > 0:
    cedula = input("Ingrese su número de cédula: ")
    # Validar que la cédula sea un número y que esté registrada
    for usuario in usuarios:
        if usuario.cedula == cedula:
            while intentos_pin > 0:
                pin = input("Ingrese su PIN: ")
                # Validar que el PIN sea correcto
                if usuario.validar_pin(pin):
                    # Continuar con las opciones del menú
                    break
                else:
                    intentos_pin -= 1
                    if intentos_pin == 0:
                        print("Se excedió el máximo de intentos para ingresar su PIN, volviendo al menú principal")
                        # Volver al menú principal
                    else:
                        print("PIN incorrecto, le quedan", intentos_pin, "intentos")
            break
    else:
        intentos_cedula -= 1
        if intentos_cedula == 0:
            print("Se excedió el máximo de intentos para ingresar su cédula, volviendo al menú principal")
            # Volver al menú principal
        else:
            print("Cédula no registrada, le quedan", intentos_cedula, "intentos")

#Hacer el sub menu indicado
def autenticar_usuario():
    cedula = input("Ingrese su cedula: ")
    if cedula in usuarios:
        usuario = usuarios[cedula]
        intentos_pin = 3
        while intentos_pin > 0:
            pin = input("Ingrese su PIN: ")
            if pin == usuario["pin"]:
                print(f"Bienvenido {usuario['nombre']}!")
                return usuario
            else:
                intentos_pin -= 1
                print("PIN incorrecto. Intente de nuevo.")
        print("Se excedió el máximo de intentos para ingresar su PIN. Volviendo al menú principal.")
        return None
    else:
        print("Cedula invalida. Volviendo al menú principal.")
        return None

def retirar_dinero(usuario):
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= usuario["saldo"]:
        usuario["saldo"] -= monto
        print(f"Retiro exitoso. Saldo actual: {usuario['saldo']}")
    else:
        print("Saldo insuficiente.")

def depositar_dinero(usuario):
    monto = float(input("Ingrese el monto a depositar: "))
    usuario["saldo"] += monto
    print(f"Deposito exitoso. Saldo actual: {usuario['saldo']}")

def ver_saldo(usuario):
    print(f"Su saldo actual es: {usuario['saldo']}")

def pagar_servicio(usuario):
    servicio = input("Ingrese el nombre del servicio a pagar: ")
    if servicio in usuario["servicios"]:
        monto = usuario["servicios"][servicio]
        if monto <= usuario["saldo"]:
            usuario["saldo"] -= monto
            del usuario["servicios"][servicio]
            print(f"Pago de servicio exitoso. Saldo actual: {usuario['saldo']}")
        else:
            print("Saldo insuficiente.")
    else:
        print("Servicio no encontrado.")

def compra_venta_divisas(usuario):
    print("Funcion no implementada.")

def eliminar_usuario():
    cedula = input("Ingrese la cedula del usuario a eliminar: ")
    if cedula in usuarios:
        del usuarios[cedula]
        print("Usuario eliminado exitosamente.")
    else:
        print("Usuario no encontrado.")

def menu():
    print("Bienvenido al sistema bancario.")
    while True:
        print("""
        1. Autenticación de usuario
        2. Retirar dinero
        3. Depositar dinero
        4. Ver saldo actual
        5. Pagar servicios
        6. Compra/Venta de Divisas
        7. Eliminar usuario
        8. Salir""")
