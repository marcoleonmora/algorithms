#/**********************************************************
#  programa que usa matrices para visualice un número
#  de cuatro dígitos en pantalla. 
# Los dígitos ocuparan cada uno cinco filas y tres columnas
# Programo: MLM
# Version: 1.0
# Fecha: 01/04/2019
# Cambios: 
#**********************************************************/

#/**********************************************************
# Carga los asteriscos en
# PARAMETROS: lista mat 
#             entero tam  
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def poblarMatriz(Mat):
    #digito 0:
    Mat[0][0] = "*** "
    Mat[0][1] = "* * "
    Mat[0][2] = "* * "
    Mat[0][3] = "* * "
    Mat[0][4] = "*** "

    #digito 1:
    Mat[1][0] = " ** "
    Mat[1][1] = "  * "
    Mat[1][2] = "  * "
    Mat[1][3] = "  * "
    Mat[1][4] = "  * "

    #digito 2:
    Mat[2][0] = "*** "
    Mat[2][1] = "  * "
    Mat[2][2] = "*** "
    Mat[2][3] = "*   "
    Mat[2][4] = "*** "

    #digito 3:
    Mat[3][0] = "*** "
    Mat[3][1] = "  * "
    Mat[3][2] = "*** "
    Mat[3][3] = "  * "
    Mat[3][4] = "*** "

    #digito 4:
    Mat[4][0] = "* * "
    Mat[4][1] = "* * "
    Mat[4][2] = "*** "
    Mat[4][3] = "  * "
    Mat[4][4] = "  * "

    #digito 5:
    Mat[5][0] = "*** "
    Mat[5][1] = "*   "
    Mat[5][2] = "*** "
    Mat[5][3] = "  * "
    Mat[5][4] = "*** "

    #digito 6:
    Mat[6][0] = "**  "
    Mat[6][1] = "*   "
    Mat[6][2] = "*** "
    Mat[6][3] = "* * "
    Mat[6][4] = "*** "

    #digito 7:
    Mat[7][0] = "*** "
    Mat[7][1] = "  * "
    Mat[7][2] = " ** "
    Mat[7][3] = "  * "
    Mat[7][4] = "  * "

    #digito 8:
    Mat[8][0] = "*** "
    Mat[8][1] = "* * "
    Mat[8][2] = "*** "
    Mat[8][3] = "* * "
    Mat[8][4] = "*** "

    #digito 9:
    Mat[9][0] = "*** "
    Mat[9][1] = "* * "
    Mat[9][2] = "*** "
    Mat[9][3] = "  * "
    Mat[9][4] = " ** "

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
    print("")
    for i in range(5):
        print("   ", end="")
        for d in range(4):
            print(digito[num[d]][i], end="  ")
        print("")


#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
digito = [[" " for col in range(5)]for row in range(10)]
#Genera la matriz, inicialmente con ceros
poblarMatriz(digito)
#lee el numero en un array con los 4 digitos
numero = leerNumero()
#Despliega el numero en la pantalla
mostrarNumero(numero, digito)



