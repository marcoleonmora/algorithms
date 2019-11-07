#/**********************************************************
# Programa que lee los datos básicos de cinco estudiantes 
# (número de matrícula, nombres, sexo, carrera, semestre)
# y muestra los datos de un estudiante particular a partir 
# del número de matrícula.
# Utilza la libreria Tkinter para la interfaz grafica 
# Los datos de los estudiantes se digitan al inicio
# Programo: MLM
# Version: 1.0
# Fecha: 10/06/2019
# Cambios: 
#**********************************************************/
from tkinter import * 
#from tkinter import ttk

#**********************************************************
# Limpia los campos del formulario
# PARAMETROS: 
# EXCEPCION: 
#**********************************************************
def limpiarForm():
    numMatricula.set("")
    nombre.set("")
    sexo.set("")
    carrera.set("")
    semestre.set("")

# MANEJADORES DE EVENTOS CLICK
#**********************************************************
# Se ejecuta al pulsar el boton btnGuardar
# crea un diccionario, toma los datos del formulario
# inserta el diccionario en la lista y lo limpia
# PARAMETROS:   lista se define global.
# RETORNA: 
# EXCEPCION: 
#**********************************************************
def btnGuardarclicked():
    global lista
    #diccionario:
    alum = {'numMatricula': 0, 'nombre':"", 'sexo':"", 'carrera': "", 'semestre': 0}

    #lee los datos del formulario
    alum['numMatricula'] = numMatricula.get()
    alum['nombre'] = nombre.get()
    alum['sexo'] = sexo.get()
    alum['carrera'] = carrera.get()
    alum['semestre'] = semestre.get()

    #Agrega registro (diccionario) a la lista
    lista.append(alum)

    #limpia el formulario
    limpiarForm()

#**********************************************************
# Se ejecuta al pulsar el boton btnConsultar
# toma el numero de matricula y lo busca en la lista.
# si lo encuentra, despliega datos en el formulario
# si no, da un aviso de no encontrado en el campo nombre
# PARAMETROS:   lista se define global.
# RETORNA: 
# EXCEPCION: 
#**********************************************************
def btnMostrarclicked():
    global lista
    codigo = numMatricula.get()
    #borra los demas campos
    limpiarForm()

    posEsta = -1
    for i in range(len(lista)):
        if codigo == lista[i]['numMatricula']:
            posEsta = i
            break
    
    #Si lo encontro, lo muestra
    if posEsta > -1:
        numMatricula.set(lista[posEsta]['numMatricula'])
        nombre.set(lista[posEsta]['nombre'])
        sexo.set(lista[posEsta]['sexo'])
        carrera.set(lista[posEsta]['carrera'])
        semestre.set(lista[posEsta]['semestre'])
    else:
        nombre.set('Matricula no encontrada')
    return

#/********************************************************** 
# PROGRAMA PRINCIPAL
#**********************************************************/
#La lista que contendra los registros
lista =[]
# Define la interfaz grafica
gui = Tk()
gui.title("Datos de Estudiantes")
gui.geometry("400x300")
gui.config(bg="grey")
contenedor = Frame()
contenedor.pack()
contenedor.config(width="350", height="280",  pady=20 , padx=20 )

#Etiquetas
lbl1 = Label(contenedor, text="Matricula", anchor="e", width=10, pady=5).grid(column=0, row=0)
lbl2 = Label(contenedor, text="Nombre", anchor="e", width=10, pady=5).grid(column=0, row=1)
lbl3 = Label(contenedor, text="Sexo", anchor="e", width=10, pady=5).grid(column=0, row=2)
lbl4 = Label(contenedor, text="Carrera", anchor="e", width=10, pady=5).grid(column=0, row=3)
lbl5 = Label(contenedor, text="Semestre", anchor="e", width=10, pady=5).grid(column=0, row=4)

#variables asociadas a las cajas de entrada
numMatricula = StringVar()
nombre= StringVar()
sexo = StringVar()
carrera= StringVar()
semestre= StringVar()

#cajas de entrada
txtNumMatricula = Entry(contenedor, textvariable=numMatricula, width=30).grid(column=1, row=0)
txtNombre = Entry(contenedor, textvariable=nombre, width=30).grid(column=1, row=1)
txtSexo = Entry(contenedor,textvariable=sexo,  width=30).grid(column=1, row=2)
txtCarrera = Entry(contenedor,textvariable=carrera,  width=30).grid(column=1, row=3)
txtSemestre = Entry(contenedor,textvariable=semestre,  width=30).grid(column=1, row=4)

# crea botones y asigna el evento click a manejador
btnGuardar = Button(contenedor, text="Guardar ", width=15,  pady=10, command=btnGuardarclicked)
btnGuardar.grid(column=0, row=6)
btnConsultar = Button(contenedor, text="Consultar ", width=15,  pady=10, command=btnMostrarclicked)
btnConsultar.grid(column=1, row=6)


#ciclo infinito, en espera de eventos en la interfaz grafica
gui.mainloop() 
#Fin del codigo ***********************************************




