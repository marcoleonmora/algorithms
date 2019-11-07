#/**********************************************************
# Carga un vector de  50 enteros con números aleatorios
#  Lo ordena de menor a mayor utilizando el método de selección. 
# Recibe un número y determina en qué posición esta, 
# si no se encuentra, determina en qué posición debería estar.
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
    for i in range(0, 10):
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
def ordenarSeleccion(vector):
    for i in range(0, len(vector)-1):
        pos = i
        menor = vector[i]
        for j in range(i+1, len(vector)):
            if vector[j] < menor:
                pos = j
                menor = vector[j]

        if vector[i] > menor: 
               aux = vector[i]
               vector[i] = vector[pos]
               vector[pos] = aux
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
# Recibe un número y determina en qué posición esta, 
# si no se encuentra, determina en qué posición debería estar.
# PARAMETROS:   lista vector
#               entero num
# RETORNA:      entero pos
#               booleano encontrado
# EXCEPCION: 
#*********************************************************/
def buscarBinario(vector, num):
    inf = 0
    sup = len(vector)
    
    while inf <= sup:
        pos = (inf + sup)//2
        if vector[pos] == num:
            return pos, True
        elif num < vector[pos]:
            sup = pos -1
        else:
            inf = pos + 1
            if inf == len(vector):
                pos += 1
                break
    return pos, False

#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
print()
print("------ ORDENAMIENTO POR SELECCION ------")
vector = ordenarSeleccion(generarNumeros())
print()
print("Contenido del vector ordenado:")
print(vector)
num = leerNumero("Ingrese un numero entero positivo: ")

#devuelve true o false si lo encontro o no y  posicion.
posNum, encontrado = buscarBinario(vector, num)

if(encontrado):
    print("El numero {} se encuentra en la posición {}.".format(num, posNum))
else:
    print("El numero {} Debería estar en la posición {}.".format(num, posNum))

#Fin del codigo ***********************************************




