#/**********************************************************
# Programa que toma un número binario, octal o hexadecimal, 
# según la base escogida  y lo convierte a Decimal
# Programo: MLM
# Version: 1.0
# Fecha: 07/05/2019
# Cambios: 
#**********************************************************/

#/**********************************************************
# Presenta el menu y toma una opcion valida
# PARAMETROS:   
# RETORNA: entero opc
# EXCEPCION: 
#*********************************************************/
def leerMenu():
    print()
    print("------ CONVERSION NUMERICA ------")
    print("1. BINARIO")
    print("2. OCTAL")
    print("3. HEXADECIMAL")
    print("0. Terminar")
    opc = -1
    while opc < 0 or opc > 3:
        try:             #Bloque para validar que el numero sea entero
            opc =  int(input("ingrese una opcion: "))
        except ValueError:
            opc = -1  #Caso de error, intenta de nuevo
    return opc

#/**********************************************************
# Lee el numero a convertir, 
# valida que sus digitos sean validos, segun la base
# PARAMETROS:  entero base 
# RETORNA: cadena num
# EXCEPCION: 
#*********************************************************/
def leerNumero(base):
    simbolo = "0123456789ABCDEF" #Simbolos a leer
    sBase = simbolo[:base]      #Toma la subcadena de digitos validos segun base
    num = ""
    print()
    ok = False                  #para obligar a entrar en el while
    while not ok:
        num =  input("ingrese un numero en base {}, mayor a cero: ".format(base))
        ok = True                   #inicialmente asume un numero correcto
        for i in range(len(num)):   #Revisa cada caracter del numero
            if num[i] not in sBase:
                ok = False
    return num

#/**********************************************************
# Convierte un numero decimal a una base numerica distinta
# PARAMETROS: cadena numero 
#               entero base  
# RETORNA: cadena valor
# EXCEPCION: 
#*********************************************************/
def convertirBaseDec(numero, base):
    simbolo = "0123456789ABCDEF" #Simbolos a leer
    resultado = 0
    pot = 1  
    l = len(numero) - 1         #indice del primer digito a la derecha         
    for i in range(l, -1, -1):  #recorre cada digito hacia la izquierda
        #toma el digito y encuentra su valor (posicion en la lista simbolo)
        digito = simbolo.index(numero[i])
        resultado += digito * pot
        pot *= base
    return resultado

#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
opcion = 1  # un valor inicial para entrar al while
baseNum = [0, 2, 8, 16]    # las bases segun opcion
while opcion in range(1, 4): # entre 1 y 3
    opcion = leerMenu()
    if opcion > 0:
        base = baseNum[opcion] #Base del numero a ingresar
        numConvertir = leerNumero(base) 
        convertido = convertirBaseDec(numConvertir, base)
        print()
        print("El numero {}(base {}), en decimal es {}".format(numConvertir, base, convertido))

#Fin del codigo ***********************************************




