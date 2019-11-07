#/**********************************************************
# Carga un vector de  50 enteros con números aleatorios
#  Lo ordena de menor a mayor utilizando el método de inserción. 

# Programo: MLM
# Version: 1.0
# Fecha: 10/06/2019
# Cambios: 
#**********************************************************/
import random   #libreria para numeros aleatorios

#/**********************************************************
# Genera 50 numeros aleatorios entre 0 y 1000 y los guarda
# en una lista
# PARAMETROS:  lista entero  
# RETORNA: lista entero
# EXCEPCION: 
#*********************************************************/
def generarNumeros():
    entero = []
    for i in range(0, 50):
        #Genera entero al azar entre 0 y 1000
        entero.append(int(random.randrange(0, 1000))) 
    return entero

#/**********************************************************
# Ordena los elementos de una lista 
# utilizando el metodo de seleccion.
# PARAMETROS:  lista vector  
# RETORNA: lista vector
# EXCEPCION: 
#*********************************************************/
def ordenarInsercion(vector):
    for i in range(1, len(vector)):
        pivote = vector[i]
        p = i-1
        while p >= 0 and  pivote < vector[p]:
            vector[p+1] = vector[p]
            p -= 1 

        if p == -1:
            p = 0
        if pivote < vector[p]:
            vector[p] = pivote
        else:
            vector[p+1] = pivote
    return vector

#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
print()
print("------ ORDENAMIENTO POR INSERCION ------")

vector = generarNumeros()
print()
print("Contenido del vector sin ordenar:")
print(vector)

vector = ordenarInsercion(vector)
print()
print("Contenido del vector ordenado:")
print(vector)

#Fin del codigo ***********************************************




