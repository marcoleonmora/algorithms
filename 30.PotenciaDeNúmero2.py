#/**********************************************************
# Algoritmo recursivo mejorado que muestra el resultado 
# de un numero elevado a un exponente
# Programo: MLM
# Version: 2.0
# Fecha: 15/05/2019
# Cambios: 
#**********************************************************/

#/**********************************************************
# Lee un numero entero mayor a cero, validando
# PARAMETROS:   cadena msj
# RETORNA: entero num
# EXCEPCION: 
#*********************************************************/
def leerNumero(msj):
    num = -1
    print()
    while num < 0:
        try:             #Bloque para validar que el numero sea entero
            num =  int(input(msj))
        except ValueError:
            num = -1  #Caso de error, intenta de nuevo
    return num

#/**********************************************************
# Encuentra el Maximo comun divisor entre dos numeros
# utiliza un algoritmo recursivo mejorado
# PARAMETROS:   entero base, exp
# RETORNA: entero result
# EXCEPCION: 
#*********************************************************/
def calcularPotencia(n, p):
    if p == 0:
        pot = 1
    elif (p % 2) == 0:
        pot = calcularPotencia(n, p/2)
        pot *= pot
    else: 
        pot = calcularPotencia(n, (p-1)/2)
        pot *= pot * n
    return pot

#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
print()
print("------ POTENCIA DE UN NUMERO ------")

base = leerNumero("Ingrese el numero base:")
exp = leerNumero("Ingrese el exponente: ")
resultado = calcularPotencia(base, exp)
print()
print("El resultado de elevar {} a la potencia {} es {}".format(base, exp, resultado))

#Fin del codigo ***********************************************




