#/*********************************************************
# Algoritmo que muestra las tablas de multiplicar, de una
# al diez.
# Programo: MLM
# Version: 1.0
# Fecha: 29/03/2019
# Cambios:
#*********************************************************/

print("**** TABLAS DE MULTIPLICAR ****")

for multiplicador in range(1,11):
    for multiplicando in range(1,11):
        print("{} X {} = {}".format(multiplicador, multiplicando,(multiplicador * multiplicando)))
    print(" ")


#    input("Ingrese una tecla para continuar...")
#print(" ")


