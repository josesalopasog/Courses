def saludar_persona(nombre):
    print("Hola" + nombre)
    
saludar_persona("Jose")

#Ejercicio 1 
# Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"

def saludar():
    print("¡Hola mundo!")
    
#Ejercicio 2 
# Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, 
# y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"
# Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")
    
nombre_persona = "Jose"

bienvenida(nombre_persona)

#Ejercicio 3 
#Declara una función llamada cuadrado, que tome como argumento un número cualquiera, 
# y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).

def cuadrado(un_numero):
    un_numero = un_numero**2
    print(un_numero)

un_numero = 2

cuadrado(un_numero)

def es_par(n):
    if n%2 == 0:
        return True
    elif n%2 == 1:
        return False
    
print(es_par(3))