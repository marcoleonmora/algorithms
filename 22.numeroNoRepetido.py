#/**********************************************************
# Ingresa en un vector de tamaño 8, números en el rango de 1 al 10 sin repetir.
# Programo: MLM
# Version: 1.0
# Fecha: 01/04/2019
# Cambios: 
#**********************************************************/

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
            break
    return rep

#/**********************************************************
# PROGRAMA PRINCIPAL
#**********************************************************/
vectorA = []
tamVector = 8

print("")
print("---------------- NUMEROS NO REPETIDOS ----------------")

for i in range(tamVector):
    repetido = True         #Inicia con valor verdad para ingresar al while
    while repetido:
        numero = 0          #Inicia con valor 0 para ingresar al while
        while numero < 1 or numero > 10:
            try:             #Bloque para validar que el numero sea entero
                numero =  int(input("ingrese un entero: "))
            except ValueError:
                numero = 0  #Caso de error, intenta de nuevo

        #cuando el numero esta en el rango 1 a 10, verifica que no este repetido
        repetido = verificarRepetido(vectorA, numero)
        if not repetido:
            vectorA.append(numero) #Si no esta repetido, lo agrega al vector


#Para terminar mustra todo el vector 
print("El vector es:")
print(*vectorA, sep = ", ")


