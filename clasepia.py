#se indica la fecha y hora de importacion
fecha y hora de importación
#importación librearia para usar los datos tipo fechas
clase  CONTACTO :
     #se define la clase
    def  __init__ ( self , NickName , Nombre , Correo , Telefono , FechaNacimiento , Gasto , Registro = datetime . datetime . now ()):
        CONTACTO . NickName  =  NickName
        CONTACTO . Nombre =  Nombre
        CONTACTO . Correo  =  Correo
        CONTACTO . Telefono =  Telefono
        CONTACTO . FechaNacimiento  =  FechaNacimiento
        CONTACTO . Gasto =  Gasto
        CONTACTO . Registro =  Registro
