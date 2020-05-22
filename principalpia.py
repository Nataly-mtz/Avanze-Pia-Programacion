# Acceso de datos a la clase Contacto

# Librería para la entrada de los datos de la clase Contacto
importar  re
# Se importa la clase Contacto
de  definirclase  import  Contacto

# Validador de expresiones regulares
def  RegEx ( _txt , _regex ):
    coincidencia = re . partido ( _regex , _txt )
    return  bool ( coincidencia )

# Expresiones regulares para cada campo.
telefonoRegEx = "^ [0-9] {10} $"
nombreRegEx = "^ [AZ] + (([',. -] [AZ])? [AZ] *) * $"
entidadValida = Verdadero

# Pregunta de teléfono.
_telefono = ""
telefono = 0
datoValido = False
mientras  cierto :
    _telefono = input ( "Teléfono:" )
    si  RegEx ( _telefono , telefonoRegEx ):
        telefono = int ( _telefono )
        datoValido = True
        rotura
    más :
        print ( "Se identificaron 10 dígitos como número" )
        datoValido = False
    entidadValida = ( entidadValida  y  datoValido )

# Preguntar nombre.
nombre = ""
datoValido = False
mientras  cierto :
    nombre = input ( "Nombre:" )
    si  RegEx ( nombre , telefonoRegEx ):
        datoValido = True
        rotura
    más :
        print ( "Se requiere nombre, apellido, no mayor a 30 catacteres." )
        datoValido = False
    entidadValida = ( entidadValida  y  datoValido )



# Módulo para poder ejecutar tareas directas en el sistema operativo.
importar  os
# Módulo para trabajar con expresión regular
importar  re

# Se establece una función para borrar pantalla.
# Se usa, expresión lambda, que es equivalente a:
# def clear ():
# os.system ('cls')
LimpiarPantalla  =  lambda : os . system ( 'cls' ) # en el sistema de Windows

# Validador de expresiones regulares
# _txt es el texto a vlidar.
# _regex es el patrón de expresión regular a validar.
# Retorna True si _txt cumple con el patrón definido en _regex
# Retrona False si no es así.
def  RegEx ( _txt , _regex ):
    coincidencia = re . partido ( _regex , _txt )
    return  bool ( coincidencia )

def  principal ():
    mientras que ( Verdadero ):
        LimpiarPantalla ()
        imprimir ( "LISTA DE COTACTOS" )
        imprimir ( "" )
        print ( "[1] Agregar un contacto." )
        print ( "[2] Buscar un contacto." )
        print ( "[3] Eliminar un contacto." )
        print ( "[4] Mostrar contactos." )
        print ( "[5] Serializar datos." )
        print ( "[0] Salir" )
        opcion_elegida  =  input ( "¿Qué deseas hacer?>" )
        si  RegEx ( opcion_elegida , "^ [123450] {1} $" ):
            si  opcion_elegida == "0" :
                imprimir ( "GRACIAS POR UTILIZAR EL PROGRAMA" )
                rotura
            si  opcion_elegida == "1" :
                imprimir ( "Llamar procedimiento para la acción" )
            si  opcion_elegida == "2" :
                imprimir ( "Llamar procedimiento para la acción" )
            si  opcion_elegida == "3" :
                imprimir ( "Llamar procedimiento para la acción" )
            si  opcion_elegida == "4" :
                imprimir ( "Llamar procedimiento para la acción" )
            si  opcion_elegida == "5" :
                imprimir ( "Llamar procedimiento para la acción" )

            input ( "Pulsa enter para contunuar ..." )
        más :
            print ( "Esa respuesta no es válida" )
            input ( "Pulsa enter para contunuar ..." )

principal ()




# Retorna falso o verdadero, dependndiendo su se encontró
# o no.
imprimir ( BuscarTelefono ( 1234567890 ))
imprimir ( BuscarTelefono ( 9999999999 ))

# Búsqueda de objeto y retorno de índice, usando función de
# búsqueda.
imprimir ( BuscarContacto ( 1234567890 ))
imprimir ( BuscarContacto ( 9999999999 ))
# Uso del índice recuperado
indice_obtenido = BuscarContacto ( 1234567890 )
si  indice_obtenido == - 1 :
    print ( "No se encontró el objeto" )
más :
    print ( Contactos [ indice_obtenido ]. telefono )
    print ( Contactos [ indice_obtenido ]. nombre )
    print ( Contactos [ indice_obtenido ]. correo )
