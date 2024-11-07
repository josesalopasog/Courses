from random import *

#Lista Inicial
palitos = ['-','--','---','----']

#Mezclar Palitos 
def mezclar(lista):
    shuffle(lista)
    return(lista)

#Pedirle Intento 
def probar_suerte():
    intento = ' '
    
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

#Comprobar Intento
def comprobar_intento(lista,intento):  
    if lista[intento - 1] == '-':
        print("Perdiste tienes el palito mas corto")
    else:
        print("Te has salvado")
    print(f"Este fue tu palito: {lista[intento - 1]}")

#Ejecución

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezclados,seleccion)

#Ejercicio 1 

#Lanzar los dados
def lanzar_dados():
    dado_1 = randint(1,6)
    dado_2 = randint(1,6)
    print(f"Tu primer dado cayo en: '{dado_1}' y tu segundo dado cayo en: '{dado_2}'")
    return(dado_1,dado_2)

def evaluar_jugada(num1,num2):
    suma_dados = 0
    for n in num1,num2:
        suma_dados += n 
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentablemente"
    elif (suma_dados >= 6) & (suma_dados < 10):
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

dados = lanzar_dados()
resultado = evaluar_jugada(dados[0],dados[1])

print(resultado)

#Ejercicio 2 

lista_numeros = [1,2,15,7,2,8,25]

def reducir_lista(lista):
    lista_nueva = []
    for n in lista: 
        if n not in lista_nueva:
            lista_nueva.append(n)
        elif n in lista_nueva:
            pass
    lista_nueva.sort()
    lista_nueva.pop(-1)
    return lista_nueva

def promedio(lista_numeros):
    suma = 0
    cant = 0
    for n in lista_numeros:
        suma += n
        cant += 1 
    return round(suma/cant,2)

lista_nueva = reducir_lista(lista_numeros)
lista_promedio = promedio(lista_nueva)

print(lista_nueva)
print(lista_promedio)

#Ejercicio 3 

def lanzar_moneda():
    resultado = choice(['Cara','Cruz'])
    return resultado

def probar_suerte(result,lista):
    if result == 'Cara':
        del lista [:]
        print("La lista se autodestruira")
        return lista
    elif result == 'Cruz':
        print("La lista fue salvada")
        return lista
           
print(probar_suerte(lanzar_moneda(),lista_numeros))


