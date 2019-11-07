#/**********************************************************
# Busca un número en un vector ordenado, 
# indica si se encuentra y en qué posición
# Programo: MLM
# Version: 1.0
# Fecha: 15/05/2019
# Cambios: 
#**********************************************************/
import random   #libreria para numeros aleatorios

#/**********************************************************
# Genera 20 numeros aleatorios entre 0 y 100 y los guarda
# en una lista
# PARAMETROS:  lista entero  
# RETORNA: lista entero
# EXCEPCION: 
#*********************************************************/
def generarNumeros():
    entero = []
    for i in range(0, 20):
        #Genera entero al azar entre 0 y 100
        entero.append(int(random.randrange(0, 100))) 
    return entero

#/**********************************************************
# Ordena los elementos de una lista 
# utilizando el metodo de burbuja.
# PARAMETROS:  lista vector  
# RETORNA: lista vector
# EXCEPCION: 
#*********************************************************/
def ordenarBurbuja(vector):

    for i in range(0, len(vector)-1):
        for j in range(i+1, len(vector)):
            if vector[i] > vector[j]:
               aux = vector[j]
               vector[j] = vector[i]
               vector[i] = aux

    return vector

#/**********************************************************
# Lee un numero entero mayor a cero, validando
# PARAMETROS:   cadena msj
# RETORNA: entero num
# EXCEPCION: 
#*********************************************************/
def leerNumero(msj):
    num = -1
    print()
    while num < 0:
        try:             #Bloque para validar que el numero sea entero
            num =  int(input(msj))
        except ValueError:
            num = -1  #Caso de error, intenta de nuevo
    return num


#/**********************************************************
# busca un numero en una lista y devuelve su posicion, 
# si no se encuentra devueve -1
# PARAMETROS:   lista vector
#               entero num
# RETORNA: entero pos
# EXCEPCION: 
#*********************************************************/
def buscarBinario(vector, num):
    inf = 0
    sup = len(vector)
    while inf <= sup:
        pos = (inf + sup)//2
        if vector[pos] == num:
            return pos
        elif num < vector[pos]:
            sup = pos -1
        else:
            inf = pos + 1
            if inf == len(vector):
                break
    return -1

#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
print()
print("------ BUSQUEDA BINARIA ------")
vector = ordenarBurbuja(generarNumeros())
print()
print("Contenido del vector ordenado:")
print(vector)
num = leerNumero("Ingrese un numero entero positivo: ")

posNum = buscarBinario(vector, num)

if(posNum > -1):
    print("El numero {} se encuentra en la posicion {}.".format(num, posNum))
else:
    print("El numero {} no se encuentra en el vector.".format(num))

#Fin del codigo ***********************************************




