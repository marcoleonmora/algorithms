#/**********************************************************
# Muestra el valor a pagar por cada empleado con diferentes 
# denominaciones y el valor total de la nómina.
# solicitar el nombre del empleado (son cinco empleados) 
# y la cantidad de horas extras trabajadas.
# Programo: MLM
# Version: 3.0
# Fecha: 31/03/2019
# Cambios: 
#**********************************************************/

#/**********************************************************
# Presenta la pantalla principal con los mensajes correspondientes
# PARAMETRO:
# RETORNA: 
# EXCEPCION: 
#**********************************************************/
def mostrarInicio():
    print(" ****** PAGO DE NOMINA ******")
    print(" ")
    print("Ingrese los datos de cada empleado.")
    print(" ")

#/**********************************************************
# Pide el nombre y el número de horas extras al empleado i
# PARAMETROS: lista nombres, por referencia 
#             lista hh, por referencia  
# RETORNA: 
# EXCEPCION: 
#*********************************************************/
def pedirDatos(nombres, hh):
    nombres.append(input(" Nombre del empleado {}? ".format(i+1)))
    hh.append(float(input(" Número de horas extras? ")))
    print("")
 
#**********************************************************
# devuelve cantidad de billetes de cada denominacon a cancelar, 
# y la cantidad de billetes acumulados por denominacion
# PARAMETROS: entero salario, array billetes
# RETORNA: 
# EXCEPCION: 
#**********************************************************/
def calcularBilletes(m, billetes):
    monto = m
    for i in range(6):
        billetes[1][i] = monto // billetes[0][i]  # numero de billetes a un empleado 
        monto = (monto % billetes[0][i])
        billetes[2][i] +=  billetes[1][i]          # numero de billetes acumulado

#**********************************************************
# muestra la cantidad de billetes de cada denominacon por empleado, 
# PARAMETROS: array billetes
# RETORNA: 
# EXCEPCION: 
#**********************************************************/
def mostrarBilletes(billetes):
    # almacena el texto de las denominaciones de los billetes
    denomBilletes = ["cincuenta mil", "veinte mil", "diez mil", "cinco mil", "dos mil", "mil"]

    for i in range(6):
        if billetes[1][i] > 0:
            print("{} billetes de {}, ".format(int(billetes[1][i]), denomBilletes[i]), end="")
 #       print("") #nueva linea


#/**********************************************************
# muestra y devuelve el valor del salario a pagar
# PARAMETROS: cadena empleado, entero hh
# RETORNA: entero salario
# EXCEPCION: 
#**********************************************************/
def pagarSalario(empleado, hh, billetes):
    salario = 800000 + hh *20000
    print("El salario del empleado {} es ${:0,.2f}".format(empleado, salario))
    calcularBilletes(salario, billetes)
    mostrarBilletes(billetes)
    print("")
    return (salario)

#/**********************************************************
# PROGRAMA PRINCIPAL
#**********************************************************/
mostrarInicio()

nombres = []        #Contendra los nombres de los empleados
hh = []             #Contendra las horas extrar de los empleados
 
billetes = [[50000, 20000, 10000, 5000, 2000, 1000],    #valor de cada denominacion
            [0, 0, 0, 0, 0, 0],                         #numero de billetes por empleado
            [0, 0, 0, 0, 0, 0]]                         #numero de billetes acumulados

#Se piden los datos
for i in range(5):
    pedirDatos(nombres, hh)   #los arreglos pasan por referencia         
    
nomina = 0

#Calcula valor de cada salario y muestra total y denominaciones
for i in range(5):
    nomina += pagarSalario(nombres[i], hh[i], billetes)   #billetes pasa por referencia, es array  
    
print("")                       #Se muestra el total
print("El valor total de la nómina es ${:0,.2f}".format(nomina))
    
