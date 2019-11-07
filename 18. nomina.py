#/**********************************************************
# Muestra el valor a pagar por cada empleado y el valor total de la nómina
# solicitar el nombre del empleado (son cinco empleados) 
# y la cantidad de horas extras trabajadas.
# Programo: MLM
# Version: 1.0
# Fecha: 31/03/2015
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
# Pide el nombre del empleado y el número de horas extras
# muestra y devuelve el valor del salario a pagar
# PARAMETROS: 
# RETORNA: real salario
# EXCEPCION: 

#**********************************************************/
def pagarSalario():
    nombre = input("Nombre del empleado: ")
    hh = float(input("Número de horas extras: "))
    salario = 800000 + hh *20000
    print("El salario del empleado {} es ${:0,.2f}".format(nombre, salario))
    print("")
    return (salario)

#/**********************************************************
# PROGRAMA PRINCIPAL
#**********************************************************/
nomina = 0
mostrarInicio()
for i in range(5):      #i va de cero a cuatro
    nomina += pagarSalario()
print("")
print("El valor total de la nómina es ${:0,.2f}".format(nomina))
    
