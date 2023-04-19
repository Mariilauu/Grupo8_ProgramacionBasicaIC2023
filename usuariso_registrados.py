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
                    print("Muchas gracias")

        else:
            print("Aún no existen usuarios registrados.")
            break

def ingresarCedula(matriz):
    intentos = 3
    while intentos > 0:
        cedula = input("Ingrese su cedula: ")
        if cedula.isdigit() and len(cedula) == 9:
            for i in range(len(matriz)):
                if matriz[i][0] != cedula:
                    intentos -= 1
                    print("La cédula ingresada es incorrecta.")
                    cedula = 0
                else:
                    break
        else:
            intentos -= 1
            print("La cédula ingresada es incorrecta.")
            cedula = 0
    return cedula


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
            pin = 0
            return pin



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
    ruta_usuario = f"/ruta/a/carpeta/usuarios/{usuario['cedula']}"
    ruta_saldos = os.path.join(ruta_usuario, "saldos")
    
    with open(ruta_saldos, "r") as archivo_saldos:
        saldos = dict(linea.strip().split(":") for linea in archivo_saldos)
    
    while True:
        print("1. Dolares\n2. Colones\n3. Bitcoins")
        opcion = input("Por favor ingrese la cuenta de la que desea retirar dinero.\nOpción: ")
        if opcion == "1":
            print("Cuenta en Dolares")
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= float(saldos["dolares"]):
                saldos["dolares"] = str(float(saldos["dolares"]) - monto)
                with open(ruta_saldos, "w") as archivo_saldos:
                    archivo_saldos.write(f"dolares:{saldos['dolares']}\n")
                print(f"Retiro exitoso. Saldo actual: {saldos['dolares']}")
            else:
                print("Saldo insuficiente.")
        elif opcion == "2":
            print("Cuenta en Colones")
        elif opcion == "3":
            print("Cuenta en Bitcoins")
        else:
            print("La opción ingresada no corresponde a ninguna de las anteriores.")



def depositar_dinero(usuario):
    cedula = usuario["cedula"]
    carpeta_usuario = f"/ruta/a/la/carpeta/{cedula}"
    archivo_saldos = f"{carpeta_usuario}/saldos.txt"

    if os.path.exists(archivo_saldos):
        with open(archivo_saldos, "r") as f:
            saldo = float(f.readline().strip())
        saldo += monto
        with open(archivo_saldos, "w") as f:
            f.write(str(saldo))
    else:
        with open(archivo_saldos, "w") as f:
            f.write(str(monto))
        saldo = monto
    
    usuario["saldo"] = saldo
    print(f"Deposito exitoso. Saldo actual: {saldo}")


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
        archivo = open("DatosDeUsuarios.txt", "r+")
        archivo.truncate(0) # borrar todo el contenido del archivo
        for k in range(len(temp_matriz)):
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


        
        
        
        
