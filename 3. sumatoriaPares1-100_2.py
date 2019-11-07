# Mostrar los números pares desde 1 hasta 100
# y la sumatoria de ellos

suma = 0
for i in range(1,101):
	if i % 2 == 0:
	  suma += i
	  print("{}, ".format(i)  ,end = '')
	  print("{}, ".format(i))

#Mostrar sumatoria
print("")
print ("La sumatoria es {}".format(suma) )

