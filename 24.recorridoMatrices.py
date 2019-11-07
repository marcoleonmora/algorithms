#/**********************************************************
#  Genera una matriz de 7 x 7 , con números aleatorios no repetidos
# Ofrece los siguientes recorridos:
# a.	Recorrer la diagonal principal
# b.	Recorrer la diagonal inversa
# c.	Recorrer la diagonal superior derecha (sin diagonal principal)
# d.	Recorrer la diagonal superior derecha con diagonal principal
# e.	Recorrer la diagonal inferior izquierda
# f.	Recorrer la diagonal superior izquierda
# g.	Recorrer  la diagonal inferior derecha.
#
# Programo: MLM
# Version: 1.0
# Fecha: 01/04/2019
# Cambios: 
#**********************************************************/
import random   #libreria para numeros aleatorios

#/**********************************************************
# En una matriz dimension: tam x tam,  
# la carga con numeros al azar entre 10 y 99
# PARAMETROS: lista matriz 
#             entero tam  
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def cargarMatriz(vector, tam):
    for i in range(tam):
        for j in range(tam):
            vector[i][j] = int(random.randrange(10, 100))

#/**********************************************************
# Muestra todos los elementos de una matriz
# PARAMETROS: lista matriz 
#             entero tam  
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def mostrarMatrizCompleta(Mat, tam):
    print("")
    print("MATRIZ COMPLETA:")
    print("")
    for i in range(tam):
        print("[", end="")
        print(*Mat[i], sep = ", ", end="") #Toda la fila
        print("]")

#/**********************************************************
# Muestra todos los elementos de la diagonal principal
# PARAMETROS: lista matriz 
#             entero tam  
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def mostrarDiagPpal(Mat, tam):
    print("")
    print("DIAGONAL PRINCIPAL:")
    print("")
    for i in range(tam):
        print("[", end="")
        for j in range(i):
            print("  ", end=",")
        print(Mat[i][i], end=",")
        for j in range(i+1, tam):
            print("  ", end=",")
        print("]")


#/**********************************************************
# Muestra todos los elementos de la diagonal Inversa
# PARAMETROS: lista matriz 
#             entero tam  
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def mostrarDiagInv(Mat, tam):
    print("")
    print("DIAGONAL INVERSA:")
    print("")
    for i in range(tam):
        print("[", end="")
        for j in range(tam-i-1):
            print("  ", end=",")
        print(Mat[i][tam-i-1], end=",")
        for j in range(tam-i, tam):
            print("  ", end=",")
        print("]")

#/**********************************************************
# Muestra todos los elementos de la matriz superior derecha
# sin la diagonal principal
# PARAMETROS: lista matriz 
#             entero tam  
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def mostrarMatSupDerSin(Mat, tam):
    print("")
    print("MATRIZ SUPERIOR DERECHA:")
    print("")
    for i in range(tam):
        print("[", end="")
        for j in range(i+1):
            print("  ", end=",")
        for j in range(i+1, tam):
            print(Mat[i][j], end=",")
        print("]")

#/**********************************************************
# Muestra todos los elementos de la matriz superior derecha
# Con la diagonal principal
# PARAMETROS: lista matriz 
#             entero tam  
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def mostrarMatSupDerCon(Mat, tam):
    print("")
    print("MATRIZ SUPERIOR DERECHA:")
    print("")
    for i in range(tam):
        print("[", end="")
        for j in range(i):
            print("  ", end=",")
        for j in range(i, tam):
            print(Mat[i][j], end=",")
        print("]")


#/**********************************************************
# Muestra todos los elementos de la matriz superior izquierda
# PARAMETROS: lista matriz 
#             entero tam  
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def mostrarMatSupIzq(Mat, tam):
    print("")
    print("MATRIZ SUPERIOR IZQUIERDA:")
    print("")
    for i in range(tam):
        print("[", end="")
        for j in range(tam - i):
            print(Mat[i][j], end=",")
        for j in range(tam - i, tam):
            print("  ", end=",")
        print("]")

#/**********************************************************
# Muestra todos los elementos de la matriz inferior izquierda
# PARAMETROS: lista matriz 
#             entero tam  
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def mostrarMatInfIzq(Mat, tam):
    print("")
    print("MATRIZ INFERIOR IZQUIERDA:")
    print("")
    for i in range(tam):
        print("[", end="")
        for j in range(i+1):
            print(Mat[i][j], end=",")
        for j in range(i+1, tam):
            print("  ", end=",")
        print("]")

#/**********************************************************
# Muestra todos los elementos de la matriz inferior derecha
# PARAMETROS: lista matriz 
#             entero tam  
# RETORNA:
# EXCEPCION: 
#*********************************************************/
def mostrarMatInfDer(Mat, tam):
    print("")
    print("MATRIZ INFERIOR DERECHA:")
    print("")
    for i in range(tam):
        print("[", end="")
        for j in range(tam - i - 1):
            print("  ", end=",")
        for j in range(tam - i - 1, tam):
            print(Mat[i][j], end=",")
        print("]")

#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
tamMatriz = 7
#Genera la matriz, inicialmente con ceros
matriz = [[0] * tamMatriz for i in range(tamMatriz)]

cargarMatriz(matriz, tamMatriz)
mostrarMatrizCompleta(matriz, tamMatriz)

mostrarDiagPpal(matriz, tamMatriz)
mostrarDiagInv(matriz, tamMatriz)
mostrarMatSupDerSin(matriz, tamMatriz)
mostrarMatSupDerCon(matriz, tamMatriz)
mostrarMatSupIzq(matriz, tamMatriz)
mostrarMatInfIzq(matriz, tamMatriz)
mostrarMatInfDer(matriz, tamMatriz)

