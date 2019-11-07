#*********************************************************
# Programa OPERACIONES: Muestra la tabla con la operación seleccionada
#  y el numero ingresado. Repite hasta que se pulse "S"
# 
# Programo: MLM
# Version: 1.0
# Fecha: 30/03/2015
# Cambios:

#/**********************************************************
# Presenta el menu y devuelve el numero de opcion seleccionada
# 1: suma, 2: resta, 3: multiplicacion,4: division
# PARAMETRO:
# RETORNA:  menu
# EXCEPCION:
#**********************************************************/
def leerMenu():
    menu = -1
    while menu < 0 or menu > 5:
        print("***** TABLAS DE OPERACIONES BASICAS ******")
        print(" ")
        print("SUMA           1")
        print("RESTA          2")
        print("MULTIPLICACION 3")
        print("DIVISION       4")
        menu = int(input(".....? "))
    return menu
        
#/**********************************************************
# lee del teclado un numero (operando)
# PARAMETRO:
# RETORNA: entero op1
# EXCEPCION: si se escribe algo diferente a un entero,
# no controlado
# EXCEPCION:
#***********************************************************/

def leerNumero():
    op1 = int(input("Ingrese el numero al que se le generara la tabla: "))
    return (op1)

#/**********************************************************
# calcula la operacion entre dos numeros
# Segun el tipo de operacion (1: suma, 2: resta,
# 3: multiplicacion,4: division), devuelve
# el resultado de aplicar la operacion a op1 y op2
# PARAMETROS: entero operacion, op1, op2
# RETORNA: real res
# EXCEPCION:
#**********************************************************/
def calcularOp(operacion, op1, op2):
    res = 0
    if operacion == 1:
        res = (op1+op2)
    elif operacion == 2:
        res = (op1-op2)
    elif operacion == 3:
        res = (op1*op2)
    elif operacion == 4:
        res = (op1/op2)
    return(res)

#/**********************************************************
# Muestra la tabla
# Muestra la tabla para el numero y la opcion seleccionada
# PARAMETROS: entero op (indica el tipo de operacion)
# entero val (numero al que se le genera la tabla)
# RETORNA:
# EXCEPCION:
#**********************************************************/
def mostrarTabla(op, val):
    simbolo = " "
    if op == 1:
        simbolo = "+"
    elif op == 2:
        simbolo = "-"
    elif op == 3:
        simbolo = "x"
    elif op == 4:
        simbolo = "/"

    for i in range(1,11):
        res = calcularOp(op, val, i)
        print("{} {} {} = {}".format(val, simbolo, i, res))


#/**********************************************************
# Lee letra para continuar o salir
# Presenta un aviso y lee del teclado un caracter
# PARAMETRO:
# RETORNA: caracter sigue
# EXCEPCION:
#**********************************************************/       
def continuarSalir():
    sigue = " "
    print("")
    sigue = input("S para salir, otra tecla para continuar...")
    return(sigue)
    

#**********************************************************
# PROGRAMA PRINCIPAL
#*********************************************************/
op = " " 
while op != "s" and op != "S":
    operacion = leerMenu()
    numero = leerNumero()
    mostrarTabla(operacion, numero)
    op = continuarSalir()

