def suma (*args):
    total = 0
    
    for arg in args: 
        total +=arg 
    return total

print(suma(5,6,7,8,9))

def suma_2 (*args):
    return sum(args)

print(suma_2(5,6,7,8,9))

#Ejercicio 1
#Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

def suma_cuadrados (*args):
    total = 0
    for arg in args:
        total += arg**2
    return total

print(suma_cuadrados(5,6,-7,8))

#Ejercicio 2 
#Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos 
#(es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos (*args):
    total = 0
    for arg in args:
        if arg < 0: 
            total += arg*(-1)
        else:
            total +=arg
    return total

print(suma_absolutos(4,5,-4,5,-1))

#Ejercicio 3 
#Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.
def numeros_persona (nombre,*args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"
    