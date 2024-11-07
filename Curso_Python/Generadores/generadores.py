def mi_funcion():
    lista = []
    for i in range(1,5):
        lista.append(i*10)
    return lista

def mi_generador():
    for i in range(1,5):
        yield i*10
    
print(mi_funcion())

g = mi_generador()
print(next(g))
print(next(g))

def mi_generador2():
    x = 1
    yield x
    x += 1
    yield x 
    x += 1
    yield x
    
g2 = mi_generador2()
print(next(g2)) 
print(next(g2)) 
print(next(g2)) 

#Ejemplo 1 
#Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1, 
# y entregando un número consecutivo superior cada vez que sea llamada mediante next.
  
def infinitos():
    numero = 0
    while True:
        numero = numero+1 
        yield numero
          
generador = infinitos()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

#Ejercicio 2 
#Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7, 
# y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).

def multiplos_siete ():
    numero = 1
    contador = 1 
    while True:
        numero = contador*7
        contador +=1 
        yield numero
        
generador = multiplos_siete()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

#Ejercicio 3 
#Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:
#"Te quedan 3 vidas"
#"Te quedan 2 vidas"
#"Te queda 1 vida"
#"Game Over"
#Almacena el generador en la variable perder_vida

def generador_vidas():
    total_vidas = 3
    while True:
        if total_vidas > 1:
            yield f"Te quedan {total_vidas} vidas"
            total_vidas -=  1
        elif total_vidas == 1:
            yield f"Te queda {total_vidas} vida"
            total_vidas -=  1
        elif total_vidas == 0:
            yield "Game Over"  

perder_vida = generador_vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
