#**********************************************************
# Muestra el calendario de un mes. Se ingresa el mes y el año
# Programo: MLM
# Version: 1.0
# Fecha: 03/04/2019
# Cambios:
#*********************************************************/

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
    datosFecha = {"nMes": 0, "nAnio": 0, "ok": True }

    datosFecha["nMes"] = int(fecha[0:2])            #Toma los meses
    datosFecha["nAnio"] = int(fecha[3:7])          #Toma los años
    
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
    print("---------------- CALENDARIO DEL MES ----------------")
    print("")

    while True:
        fecha = input("Ingrese EL Mes y el Año en formato MM/AAAA: ")
        fechaNumeros = validarFecha(fecha) 
        if fechaNumeros["ok"]==True:
            return fechaNumeros

#**********************************************************
# Calcula el numero del dia en la semana, del primer dia de un mes
# utiliza el algoritmo de la Congruencia de Zeller
# http://es.wikipedia.org/wiki/Congruencia_de_Zeller
# PARAMETROS: entero  mes, anio
# RETORNA: entero d
# EXCEPCION:
#*********************************************************/
def calcularDia(mes, anio):
    a = int((14 - mes) // 12)
    ya = anio - a
    m = int(mes + (12 * a) - 2)
    d = int((1 + ya + (ya // 4) - (ya // 100) + (ya // 400) + (31 * m ) // 12) % 7)
    return(d)

#**********************************************************
# Despliega los titulos iniciales del calendario
# PARAMETROS: 
# RETORNA: 
# EXCEPCION:
#*********************************************************/
def mostrarTitulos(mm, aa):
    print("")
    print("      {} de {}".format(mm, aa))
    print("|----|----|----|----|----|----|----|")
    print("| Do | Lu | Ma | Mi | Ju | Vi | Sa |")
    print("|----|----|----|----|----|----|----|")


#**********************************************************
# Despliega cuadros vacios antes del primer dia  del calendario
# PARAMETROS: entero dia: primer dia 
# RETORNA: 
# EXCEPCION:
#*********************************************************/
def mostrarCuadros(dia):
    for i in range(dia):
        print("|    ", end="")


#**********************************************************
# Despliega el calendario del mes
# PARAMETROS: diccionario fechaNumero {nMes", "nAnio", "ok"}} 
# RETORNA: 
# EXCEPCION:
#*********************************************************/
def mostrarCalendario(fechaNumero):
    meses = ["", "Enero", "Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre", "Diciembre"]
    diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nMes = fechaNumero["nMes"]
    nAnio = fechaNumero["nAnio"]
    numDias = diasMes[nMes]
    diaIni = calcularDia(nMes,nAnio)     #numero del dia semanal para el primero del mes

    mostrarTitulos(meses[nMes], nAnio)   
    mostrarCuadros(diaIni)

    #ciclo para mostrar los numeros
    j = diaIni # para controlar los cuadros por semana
    i = 1 #para controlar el dia del mes
    while i <= numDias:
        while j < 7 and i <= numDias:        #para controlar los cuadros por semana
            if i < 10:
                print("|  {} ".format(i), end="") #caso numeros de un digito
            else:
                print("| {} ".format(i), end="") 
            j += 1
            i += 1
        if j == 7:          
            print("|")    #Barra final solo si termina fila    
            print("|----|----|----|----|----|----|----|")
            j = 0        #otra semana (nueva fila)

    mostrarCuadros(7-j) #muestra los cuadros faltantes de la ultima semana
    print("|")   #cierra el ultimo cuadro
    print("|----|----|----|----|----|----|----|") 


#/**********************************************************
# PROGRAMA PRINCIPAL
#***********************************************************/

fechaNumero = pedirDatos()
mostrarCalendario(fechaNumero)
