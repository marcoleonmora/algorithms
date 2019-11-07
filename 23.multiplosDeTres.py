#/**********************************************************
# registra en un arreglo de una dimensión, 20 números no repetidos
#  generados aleatoriamente y muestra los que sean múltiplos de  3.
# Programo: MLM
# Version: 1.0
# Fecha: 01/04/2019
# Cambios: 
#**********************************************************/
import random   #libreria para numeros aleatorios

#/**********************************************************
# Revisa si un numero se encuentra en una lista o array
# PARAMETROS: lista vector 
#             entero n  
# RETORNA: bool rep
# EXCEPCION: 
#*********************************************************/

def verificarRepetido(vector, n):
    rep = False
    for i in range(len(vector)):
        if n == vector[i]:
            rep = True
    return rep

#/**********************************************************
# PROGRAMA PRINCIPAL
#**********************************************************/
vectorA = []
tamVector = 20

print("")
print("------------ VECTOR DE 20 NUMEROS NO REPETIDOS ------------")

for i in range(tamVector):
    repetido = True         #Inicia con valor verdad para ingresar al while
    while repetido:
        numero = 0          #Inicia con valor 0 para ingresar al while
        while numero < 1 or numero > 100:
            try:             #Bloque para validar que el numero sea entero
                numero =  int(random.randrange(1, 100)) #Genera entero al azar entre 1 y 100
            except ValueError:
                numero = 0  #Caso de error, intenta de nuevo

        #cuando el numero esta en el rango 1 a 10, verifica que no este repetido
        repetido = verificarRepetido(vectorA, numero)
        if not repetido:
            vectorA.append(numero)  #Si no esta repetido, lo agrega al vector


# Mustra todo el vector 
print("El vector es: [", end="")
print(*vectorA, sep = ", ", end="")
print("]")
#Buscar los multiplos de tres
print("Los multiplos de 3 son:")
for i in range(tamVector):
    if vectorA[i] % 3 == 0:
        print(vectorA[i], end=", ")
print("")


