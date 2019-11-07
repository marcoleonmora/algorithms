#/**********************************************************
# Programa que toma un número entero y lo presente en 
# binario, octal o hexadecimal, según la base escogida 
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
# Lee el numero a convertir
# PARAMETROS:   
# RETORNA: entero num
# EXCEPCION: 
#*********************************************************/
def leerNumero():
    num = 0
    print()
    while num < 1:
        try:             #Bloque para validar que el numero sea entero
            num =  int(input("ingrese un numero en decimal, mayor a cero: "))
        except ValueError:
            num = 0  #Caso de error, intenta de nuevo
    return num

#/**********************************************************
# Convierte un numero decimal a una base numerica distinta
# PARAMETROS: entero numero,  base  
# RETORNA: cadena valor
# EXCEPCION: 
#*********************************************************/
def convertirDecBase(numero, base):
    simbolo = "0123456789ABCDEF" #Simbolos a leer
    valor= ""       #Contendra caracteres del numero convertido,
    while numero > 0:
        aux = numero % base
        valor = simbolo[aux] + valor #Agrega el simbolo por la izquierda
        numero = numero // base
    return valor

#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
opcion = 1  # un valor inicial para entrar al while
baseNum = [0, 2, 8, 16]    # las bases segun opcion
while opcion in range(1, 4): # entre 1 y 3
    opcion = leerMenu()
    if opcion > 0:
        numDecimal = leerNumero()
        base = baseNum[opcion]
        convertido = convertirDecBase(numDecimal, base)
        print("El numero {} en base {} es {}".format(numDecimal, base, convertido))

#Fin del codigo ***********************************************




