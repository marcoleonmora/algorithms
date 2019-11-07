#/**********************************************************
#  programa que usa matrices para visualice un número
#  de cuatro dígitos, en forma vertical en pantalla. 
# Programo: MLM
# Version: 2.0
# Fecha: 01/04/2019
# Cambios: 
#**********************************************************/

#/**********************************************************
# Carga los símbolos para representar numeros verticales
# PARAMETROS: lista mat, por referencia 
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def poblarMatriz(Mat):
    #digito 0:
    Mat[0][0] = "╔═════╗"
    Mat[0][1] = "╚═════╝"
 
    #digito 1:
    Mat[1][0] = "╔══════"
    Mat[1][1] = "       "

    #digito 2:
    Mat[2][0] = "╔══╗  ╗"
    Mat[2][1] = "╚  ╚══╝"
 
    #digito 3:
    Mat[3][0] = "╔══╦══╗"
    Mat[3][1] = "╚     ╝"
 
    #digito 4:
    Mat[4][0] = "═══╦═══"
    Mat[4][1] = "═══╝   "
 
    #digito 5:
    Mat[5][0] = "╔  ╔══╗"
    Mat[5][1] = "╚══╝  ╝"

    #digito 6:
    Mat[6][0] = "   ╔══╗"
    Mat[6][1] = "╚══╩══╝"

    #digito 7:
    Mat[7][0] = "╔══╦═══"
    Mat[7][1] = "╚      "

    #digito 8:
    Mat[8][0] = "╔══╦══╗"
    Mat[8][1] = "╚══╩══╝"

    #digito 9:
    Mat[9][0] = "╔══╦══╗"
    Mat[9][1] = "╚══╝   "
 
#/**********************************************************
# Lee un numero de cuatro digitos y devuelve un array
# con los digitos separados
# PARAMETROS:   
# RETORNA: list numero[4]
# EXCEPCION: 
#*********************************************************/
def leerNumero():
    numero =[0,0,0,0]  #inicia en ceros
    num = -1
    print("")
    while num < 0 or num > 9999:
        try:             #Bloque para validar que el numero sea entero
            num =  int(input("ingrese un entero: "))
        except ValueError:
            num = -1  #Caso de error, intenta de nuevo
    # Separa los digitos
    numero[0] = num // 1000
    num = num % 1000
    numero[1] = num // 100
    num = num % 100
    numero[2] = num // 10
    num = num % 10
    numero[3] = num
    return numero

#/**********************************************************
# Muestra el numero en la pantalla
# # PARAMETROS: list num, digito  
# RETORNA: 
# EXCEPCION: 
#*********************************************************/
def mostrarNumero(num, digito):
#    print("")
    for d in range(3, -1, -1):  #para cada digito, desde el ultimo
        for c in range(2):      #Para cada columna de un digito
            print(digito[num[d]][c])
#        print("")


#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
digito = [[" " for col in range(2)]for row in range(10)]
#Genera la matriz, inicialmente con ceros
poblarMatriz(digito)
#lee el numero en un array con los 4 digitos
numero = leerNumero()
#Despliega el numero en la pantalla
mostrarNumero(numero, digito)



