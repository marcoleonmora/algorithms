#/**********************************************************
# Llena una lista de  20 enteros con números aleatorios 
# y muestra el contenido.
# Despues ordena la lista de menor a mayor
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
        entero.append(int(random.randrange(-100, 100))) 
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
# PROGRAMA PRINCIPAL
#**********************************************************/
print()
print("------ ORDENAR UNA LISTA ------")
vector = generarNumeros()
print()
print("Contenido del vector inicial:")
print(vector)
vector = ordenarBurbuja(vector)
print()
print("Contenido del vector ordenado:")
print(vector)

#Fin del codigo ***********************************************




