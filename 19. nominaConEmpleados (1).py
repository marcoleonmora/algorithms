#/**********************************************************
# Muestra el valor a pagar por cada empleado y el valor total de la nómina
# solicitar el nombre del empleado (son cinco empleados) 
# y la cantidad de horas extras trabajadas.
# Programo: MLM
# Version: 2.0
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
 
#/**********************************************************
# muestra y devuelve el valor del salario a pagar
# PARAMETROS: entero i
# RETORNA: real salario
# EXCEPCION: 
#**********************************************************/
def pagarSalario(empleado, hh):
    salario = 800000 + hh *20000
    print("El salario del empleado {} es ${:0,.2f}".format(empleado, salario))
    print("")
    return (salario)

#/**********************************************************
# PROGRAMA PRINCIPAL
#**********************************************************/
mostrarInicio()
nombres = [] #Contendra los nombres de los empleados
hh = []     #Contendra las horas extrar de los empleados

for i in range(5):
    pedirDatos(nombres, hh)           #Se piden los datos
    
nomina = 0

for i in range(5):
    nomina += pagarSalario(nombres[i], hh[i])   #Se muestra el salario  
    
print("")                       #Se muestra el total
print("El valor total de la nómina es ${:0,.2f}".format(nomina))
    
