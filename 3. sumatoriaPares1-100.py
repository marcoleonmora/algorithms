
# Mostrar los números pares desde 1 hasta 100
# y la sumatoria de ellos

suma = 0
for i in range(1,101): #para que repita hasta 100
	if i % 2 == 0:
	  suma += i
	  print(i)

#Mostrar sumatoria
print ("La sumatoria es {}".format(suma) )

