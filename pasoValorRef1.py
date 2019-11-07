# Ejemplo de paso por valor

# funcion -------------------
def doblar_valor(numero):
    numero *= 2
    print(numero)

# Programa principal -------
numero = 20
doblar_valor(numero)
print(numero)

# Ejemplo de paso por referencia

# funcion -------------------
def doblar_valores(numeros):
    for i in range(0, len(numeros)):
        numeros[i] *= 2

# Programa principal -------
ns = [10,50,100]
#print(ns)

doblar_valores(ns)
#print(ns)
