#***************************************************
# Algoritmo para convertir una nota numerica (1 a 20)
# en la letra equivalente asi: A (19-20), B (16-18)
# C (13-15), D (10-12), E (1-9)
#
# Programo: MLM
# Version: 2.0, con repeticion
# Fecha: 29/03/2019
# Cambios:
#***************************************************/

#Convierte la nota numerica en la letra equivalente
def convertir(n):
    if  nota >= 20:
        letra ="A"
    elif nota >= 16:
        letra ="B"
    elif nota >= 13:
        letra ="C"
    elif nota >= 10:
        letra="D"
    elif nota >= 1:
        letra="E"
    else:
        letra = "O"
    return letra          

#Programa principal -------------------------------
print("NOTA EQUIVALENTE")
print("")

while True:
    nota = -1 # un valor inicial, para entrar en el ciclo

    # Pedir la nota, validando el rango, repite hasta que sea correcto
    while nota < 0 or nota >20:
        nota=int(input("Escriba la nota entre 1 y 20, 0 para salir: "))

    if nota > 0:
        letra = convertir(nota)
        print("La nota equivalente a {} es {}".format(nota, letra))
        print()
    else:
        break   #Si es cero, sale del ciclo while 

