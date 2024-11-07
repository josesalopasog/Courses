def chequear_3_cifras(lista):
    
    lista_2 = []
    
    for n in lista: 
        if n in range(100,1000):
            lista_2.append(n)
        else:
            pass
    return lista_2
    
resultado = chequear_3_cifras([555,99,600])
print(resultado)

#Ejercicio 1
#Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, 
# y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

def todos_positivos(lista_2):
    
    for n in lista_2: 
        if n < 0: 
            return False
        else:
            pass
    return True

lista_numeros_2 = [0,1,2,3]

resultado_2 = todos_positivos(lista_numeros_2)
print(resultado_2)

#Ejercicio 2 
#Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre 
# y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

def suma_menores(lista_3):
    lista_numeros = 0
    for n in lista_3:
        if (n>0) & (n<1000):
            lista_numeros += n
        else: 
            pass
    return lista_numeros

lista_numeros_4 = [10,20,1000,-1]

resultado_3 = suma_menores(lista_numeros_4)
print(resultado_3)

#Ejercicio 3 
# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), 
# y devuelva el resultado de dicha cuenta.

def cantidad_pares(lista_4):
    cant_pares = 0
    for n in lista_4:
        if n%2 == 0:
            cant_pares += 1
        else:
            pass
    return cant_pares

lista_numeros = [1,2,3,4,5,6,7,8]

print(cantidad_pares(lista_numeros))
