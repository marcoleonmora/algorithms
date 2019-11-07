#/**********************************************************
# Lee dos vectores de 10 enteros cada uno 
# Obtiene el promedio de cada vector y la suma.
# Programo: MLM
# Version: 1.0
# Fecha: 01/04/2019
# Cambios: 
#**********************************************************/

#/**********************************************************
# PROGRAMA PRINCIPAL
#**********************************************************/
vectorA = []
vectorB = []
promedio = 0.0
tamVector = 10
suma = 0

print("")
print("---------------- SUMA Y PROMEDIO DE VECTORES ----------------")
print("ELEMENTOS DEL VECTOR A:")
for i in range(tamVector):
    vectorA.append(int(input("Elemento [{}]:? ".format(i))))
print("")
print("ELEMENTOS DEL VECTOR B:")
for i in range(tamVector):
    vectorB.append(int(input("Elemento [{}]:? ".format(i))))

for i in range(tamVector):
    suma += (vectorA[i]+vectorB[i])
promedio = suma / (tamVector * 2)

print("")
print("La suma de todos los elementos es {} y el promedio es {}".format(suma, promedio))

