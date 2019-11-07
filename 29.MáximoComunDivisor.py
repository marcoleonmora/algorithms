#/**********************************************************
# Algoritmo recursivo que muestra el Máximo Común Divisor (MCD)
#  de dos enteros dados
# Programo: MLM
# Version: 1.0
# Fecha: 15/05/2019
# Cambios: 
#**********************************************************/

#/**********************************************************
# Lee un numero entero mayor a cero, validando
# PARAMETROS:   
# RETORNA: entero num
# EXCEPCION: 
#*********************************************************/
def leerNumero():
    num = 0
    print()
    while num < 1:
        try:             #Bloque para validar que el numero sea entero
            num =  int(input("ingrese un numero entero, mayor a cero: "))
        except ValueError:
            num = 0  #Caso de error, intenta de nuevo
    return num

#/**********************************************************
# Encuentra el Maximo comun divisor entre dos numeros
# utiliza un algoritmo recursivo
# PARAMETROS:   entero a, b
# RETORNA: entero mcd
# EXCEPCION: 
#*********************************************************/
def encontrarMCD(a, b):
    mcd = 0
    
    if b == 0:
        mcd = a
    elif a == 0:
        mcd = b
    elif a > b:
        mcd = encontrarMCD(a-b, b)
    else:
        mcd = encontrarMCD(a, b-a)
    return mcd

#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
print()
print("------ MAXIMO COMUN DIVISOR ------")

numA = leerNumero()
numB = leerNumero()
maxComDiv = encontrarMCD(numA, numB)

print("El MCD entre {} y {} es {}".format(numA, numB, maxComDiv))

#Fin del codigo ***********************************************




