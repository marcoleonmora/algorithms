# Algoritmo para calcular el promedio de los 
# numeros ingresados por teclado, entre 1 y 20
# termina al ingresar cero
# Programo: 
# Version: 1.0
# Fecha: 
# Cambios:
#------------------------------------------------
suma=0
cantidad=0
print("CALCULO DEL PROMEDIO")
n = 1		#Algun valor diferente de cero, para ingresar en el ciclo
while n != 0:
    #Ingresar numeros
    n = int(input("Ingrese un numero entre 1 y 20 (0 para salir): "))
    
    if 0 < n <=20:          #Valida el rango para hacer sumatoria
        suma += n
        cantidad += 1
    elif n != 0:
        print("número fuera de rango!")
        
#Calcular promedio
prom = suma/cantidad
print("El promedio es {} ".format(prom))
