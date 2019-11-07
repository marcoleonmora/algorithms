#PRIMOS: Algoritmo para comprobar si un numero ingresado 
#por teclado es primo o no.

#Solicitar numero
print ("NUMEROS PRIMOS")
numero = int(input("Ingrese un numero: "))

#Buscar si es par o primo
esPrimo = "Es primo"
#numero + 1: Se suma uno porque en Python el ciclo for 
# repite hasta el numero anterior al limite
for i in range(2, (numero +1) // 2):
    if numero % i == 0:
        esPrimo = "No es primo"

#Escribe el resultado
print ("El numero {} {}".format(numero, esPrimo))

