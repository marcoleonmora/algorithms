# Mostrar los números de 1 a 300, contar los impares
# y la sumatoria de todos

suma = 0
impares = 0
print("NUMEROS DEL 1 AL 300")
for i in range(301):
	print("{}, ".format(i)  ,end = '')
	suma = suma + i
	if i % 2 == 1:
		impares += 1

#Mostrar el resultado de la sumatoria
print ("")
print ("Todos los numeros suman {}".format(suma))
print ("existen {} numeros impares".format(impares))
