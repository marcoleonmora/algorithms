#/**********************************************************
# Llena una lista de  20 enteros con números aleatorios, 
# muestra el contenido y determina en qué posición de la 
# lista está el número mayor
# Programo: MLM
# Version: 2.0
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
# Busca la posicion del numero mas grande en una lista
# PARAMETROS:  lista vector  
# RETORNA: entero pos
# EXCEPCION: 
#*********************************************************/
def buscarMayor(vector):
    pos = 0
    mayor = -1
    for i in range(0, len(vector)):
        if(vector[i] > mayor):
            pos = i
            mayor = vector[i]
    return pos

#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
print()
print("------ BUSCA EL NUMERO MAYOR ------")
vector = generarNumeros()
posMayor = buscarMayor(vector)

print()
print("Contenido del vector:")
print(vector)

print("El numero mayor es {}, se encuentra en la posicion {}".format(vector[posMayor], posMayor))

#Fin del codigo ***********************************************




