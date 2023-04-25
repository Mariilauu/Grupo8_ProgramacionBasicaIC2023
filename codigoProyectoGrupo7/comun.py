# Biblioteca de objetos compartidos
# tilizados en algunas partes del código

#Bibliotecas importadas
import os

#***********************************************************************************************************************

# Nombres de los archivos
NombreArchivoUsuarios = "UsuariosYPines.txt"
NombreArchivoConfig = "config.txt"
NombreArchivoTC = "tiposDeCambio.txt"

#***********************************************************************************************************************

# Se solicita un número de cédula válido y que exista.  En caso contrario retorna 0
def solicitaCedula ():
    cedula = input("Ingrese el número de cédula (debe ser de 9 dígitos): ")
    if os.path.exists(cedula):
        if cedula.isdigit() and len(cedula) == 9:
            return cedula
        else:
            print("El valor ingresado no corresponde a 9 digitos.")
            return "0"
    else:
        print("La cédula no se encuentra registrada.")
        return "0"

#***********************************************************************************************************************

# Elimina un usuario de la matriz y de la estructura de archivos.  Retorna si la cédula fue encontrada en la matriz.
def eliminaUsuario(cedula, matriz):
    encontrada = False
    for i in range(len(matriz)):
        if matriz[i][0] == cedula:
            del matriz[i]
            encontrada = True
            # Eliminar carpeta con la cédula del usuario si existe
            carpetaUsuario = cedula
            if os.path.exists(carpetaUsuario):
                contenido = os.listdir(carpetaUsuario)
                for archivo in contenido:
                    rutaArchivo = os.path.join(carpetaUsuario, archivo)
                    os.remove(rutaArchivo)
                os.rmdir(carpetaUsuario)
            break
    return encontrada

#***********************************************************************************************************************

# Guarda la matriz de usuarios en el archivo txt
def guardaUsuariosYPines(matriz):
    try:
        archivo = open(NombreArchivoUsuarios, "w")
        for k in range(len(matriz)):
            for j in range(len(matriz[k])):
                archivo.write(matriz[k][j])
                archivo.write("\n")
        archivo.close()
    except:
        print(f"\n*** No se pudo guardar en el archivo {NombreArchivoUsuarios}")

#***********************************************************************************************************************

# Lee un monto positivo del usuario.  Se retorna como texto para los casos de tipos de cambio como 0.00001234 no se conviertan en 1.234e-05
def capturaMonto(mensaje, intentos):
    i = intentos
    while intentos == 0 or i > 0:
        try:
            texto = input(mensaje)
            monto = float(texto)
            if monto > 0:
                return texto
            else:
                print("El valor digitado debe ser mayor a cero, intente nuevamente.")
        except:
            print("El valor digitado no es correcto, intente nuevamente.")
        i -= 1
    return "0"
