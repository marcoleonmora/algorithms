#***************************************************
# Algoritmo para convertir una nota numerica (1 a 20)
# en la letra equivalente asi: A (19-20), B (16-18)
# C (13-15), D (10-12), E (1-9)
#
# Programo: MLM
# Version: 1.0
# Fecha: 29/03/2019
# Cambios:
#***************************************************/
print("")
print("NOTA EQUIVALENTE")
print("")

nota = -1 #valor inicial, para entrar en el ciclo

#Pedir la nota, validando el rango
while nota < 0 or nota >20:
    nota=int(input("Escriba la nota entre 1 y 20: "))

if  nota >= 20:
    letra ="A"
elif nota >= 16:
    letra ="B"
elif nota >= 13:
    letra ="C"
elif nota >= 10:
    letra="D"
else:
    letra="E"           
            
print("La nota equivalente a {} es {}".format(nota, letra))
