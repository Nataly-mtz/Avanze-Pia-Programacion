# Programar que lea los archivos CSV, y que cargue en un objeto, y almacena en una lista.

# Librería para acceder a archivos CSV
importar  csv
# Librería para manejar datos de tipo datetime
 fecha y hora de importación

# Clase para guardar los incidentes
clase   Incidente :
      def  __init__ ( self , FECHA , CASOS , MUERTES , PAIS ):
            auto . FECHA  =  FECHA
            auto . CASOS  =  CASOS
            auto . MUERTES  =  MUERTES
            auto . PAIS  =  PAIS

# Lectura secuencial del archivo
con  abierto ( 'AnálisisCOVID.csv' ) como  archivo_csv :
    lector_csv  =  csv . lector ( archivo_csv , delimitador = '|' )
    contador_lineas  =  0
    # Creando una lista vacía.
    lista_incidentes  = []
    # Lectura secuencial.
    para  linea_datos  en  lector_csv :
        si  contador_lineas  ==  0 :
            # Si es la primera línea, habitación los nombres de campo y no guardo nada
            # en la lista.
            print ( f'Los nombres de columna son { "," . join ( linea_datos ) } ' )
        más :
            # Si son datos (línea uno y posteriores) ...
            # Generar una instancia de la clase Incidente, y le proporcionamos al constructor
            # los valores leidos del archivo.
            # RETO: Aquí se convierte el primer valor a su equivalente fecha y hora
            objeto_temporal  =  Incidente ({ linea_datos [ 0 ]}, { linea_datos [ 1 ]}, { linea_datos [ 2 ]}, { linea_datos [ 3 ]})
            lista_incidentes . agregar ( objeto_temporal )

        # Se incrementa el número de líneas, pase lo que pase.
        contador_lineas  + =  1

    print ( f'Procesadas { len ( lista_incidentes ) } líneas. ' )


# Define una clase.

# En una aplicación de tipo Agenda personal, se tiene una entidad de datos
# llamada Contacto, será manejado a través de una clase. 
# La clase tiene las siguientes propiedades.
# telefono: Es el número telefónico del contacto, y actúa como PK.
# nombre: Es el nombre completo del Contacto.
# correo: es el correo electrónico del contacto.
# registro: es la fecha de registro en el contacto se seleccionado.



# Se declara una clase para el manejo del dato.
# Por lo pronto, solo maneja propiedades.
 Contacto de clase :
  # Se declara un procedimiento constructor.
  # Incluye todas las propiedades como argumentos.
  # La propiedad es opcional, porque toma la información de la
  # fecha del sistema al momento de la instancia de la clase.
  def  __init__ ( self , telefono , nombre , correo , registro = datetime . datetime . now (), UIValido = False ):
    auto . telefono = telefono
    auto . nombre = nombre
    auto . correo = correo
    auto . registro = registro
    auto . UIValido = UIValido
