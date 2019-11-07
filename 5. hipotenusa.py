#**************************************
# algoritmo para determinar la hipotenusa 
# de un triángulo rectángulo, dadas las 
# longitudes de sus dos catetos.
# Programo: MLM
# Version: 1.0
# Fecha: 27/03/2019
#**************************************/

#Ingresar catetos
a = int(input("Ingrese el valor del primer cateto: "))
b = int(input("Ingrese el valor del segundo cateto: "))

#Calcular hipotenusa ()
h = (a*a + b*b)**(1/2)

#Mostrar el resultado
print("La hipotenusa del triangulo de lados {} y {} es igual a {}".format(a, b, h))

