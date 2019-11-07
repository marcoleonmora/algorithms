#/**********************************************************
# Muestra el nombre del dia correspondiente a una fecha.
# Programo: MLM
# Version: 1.0
# Fecha: 02/04/2019
# Cambios:
#**********************************************************/

#**********************************************************
# Valida una fecha en formato DD/MM/AAAA
# convierte a enteros los componentes de la fecha
# y comprueba que estén en los rangos correctos.
# PARAMETROS: cadena[10] fecha
# RETORNA: Diccionario datosFecha{}
# EXCEPCION:
#*********************************************************/
def validarFecha(fecha):
        # Se define un 'diccionario' para devolver varios datos en él:
        datosFecha = {"nDia": 0, "nMes": 0, "nAnio": 0, "ok": True }
        
        datosFecha["nDia"] = int(fecha[0:2])            #Toma los dias
        datosFecha["nMes"] = int(fecha[3:5])            #Toma los meses
        datosFecha["nAnio"] = int(fecha[6:10])          #Toma los años
        
        if datosFecha["nDia"] < 1 or datosFecha["nDia"] > 31:
                datosFecha["ok"] = False
        if  datosFecha["nMes"] < 1 or datosFecha["nMes"] > 12:
                datosFecha["ok"] = False
        if datosFecha["nAnio"] < 1800:
                datosFecha["ok"] = False
        
        return (datosFecha)

#**********************************************************
# Presenta la pantalla principal con los mensajes correspondientes
# Ingresa la fecha en formato DD/MM/AAAA y la valida
# si la fecha es correcta, la separa y carga en variables globales
# PARAMETRO:
# RETORNA:
# EXCEPCION:

#*********************************************************/
def pedirDatos():
    print("")
    print("---------------- DIA DE UNA FECHA ----------------")
    print("")

    while True:
        fecha = input("Ingrese la fecha en el formato DD/MM/AAAA: ")
        fechaNumeros = validarFecha(fecha) 
        if fechaNumeros["ok"]==True:
                return fechaNumeros
                
#**********************************************************
# Calcula el nombre del día de la semana de una fecha
# utiliza el algoritmo de la Congruencia de Zeller
# http://es.wikipedia.org/wiki/Congruencia_de_Zeller
# PARAMETROS: entero dia, mes, anio
# RETORNA: cadena[12] nombreDia
# EXCEPCION:
#*********************************************************/
def calcularDia(dia, mes, anio):
        nombreDia = {0:"Domingo", 1:"Lunes", 2:"Martes", 3:"Miercoles", 4:"Jueves", 5:"Viernes", 6:"Sabado"}
        a = int((14 - mes) // 12)
        ya = anio - a
        m = int(mes + (12 * a) - 2)
        d = int((dia + ya + (ya // 4) - (ya // 100) + (ya // 400) + (31 * m ) // 12) % 7)
        diaSem = nombreDia[d]
        return(diaSem)


#/**********************************************************
# PROGRAMA PRINCIPAL
#***********************************************************/
fechaNumeros = pedirDatos()
nDia = fechaNumeros["nDia"]
nMes = fechaNumeros["nMes"]
nAnio = fechaNumeros["nAnio"]
dia = calcularDia(nDia,nMes,nAnio)
print("El día corresponde a un {}".format(dia))
