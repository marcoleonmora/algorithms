#******************************************
# Algoritmo para calcular y mostrar
# el área de un cubo o de un cilindro
# Programo: MLM
# Version: 1.0
# Fecha: 27/03/2019
#*****************************************/
import math

print ("   CALCULO DEL VOLUMEN")
print ("")
print ("1- Volumen del cubo")
print ("2- Volumen del cilindro")

#Obtener opcionión seleccionada 
opcion = int(input("Seleccione la opcionion deseada: "))
print ("")
volumen = 0
#Según opcion pedir parámetros y Calcular volumen
if opcion == 1:
    l = int(input("Ingrese el lado del cubo: "))
    volumen = l*l*l
elif opcion == 2:
    r = int(input("Ingrese el radio del cilindro: "))
    a = int(input("Ingrese la altura  del cilindro: "))
    volumen = (math.pi * r * r * a)
else:
    print ("La opción no es valida")

# Mostrar resultado
if volumen > 0:
    print ("El volumen es {}".format(volumen))
