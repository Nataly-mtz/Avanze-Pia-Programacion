import  datetime   
# se importa un módulo de datatime que se usara en la linea 8
txt =  str ( input ( "inserta una cadena:" ))   # a continuacion se piden los datos con los que trabaremos
entero =  int ( input ( "inserta un entero:" ))
dfloat =  float ( input ( "inserta un numero decimal:" ))
dtime = ( input ( "ingresa una fecha aaaa / mm / dd:" ))
# se define una función para calcular los tipos de datos
def  calcular ( txt , entero , dfloat , dtime ):
    a ñ o  =  dtime [ 0 : 4 ]
    mes  = dtime [ 5 : 7 ]
    dia =  dtime [ - 2 :]
    fecha =  fecha y hora . datetime ( int ( a ñ o ), int ( mes ), int ( mes ))
    resultado = { txt : type ( txt ), entero : type ( entero ), dfloat : type ( dfloat ), fecha : type ( fecha )}
    devolver  resultado
    # en la linea anterior se guardan el dato intreducido con su perspectivo tipo de dato en un diccionario
def  imprimir (): # se define una función para imprimir
    resultado =  calcular ( txt , entero , dfloat , dtime )   # se llama a la función calcular
    para  x  en  resultado . items ():   # se registra el dicc resultado y se imprime
        imprimir ( x )
imprimir ()
