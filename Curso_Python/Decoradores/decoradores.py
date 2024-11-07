def cambiar_letras(tipo):
    
    def mayuscula (text):
        print(text.upper())
        
    def minuscula (text):
        print(text.lower())
    
    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula
    
def una_funcion(funcion):
    return funcion

operacion = cambiar_letras('may')

operacion('palabra')

def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

# @decorar_saludo siempre estara decorada la función 
def mayuscula (text):
    print(text.upper())
    
def minuscula (text):
    print(text.lower())
    
mayuscula_decorada = decorar_saludo(mayuscula) #Así escojo si la quiero decorar o no 
mayuscula_decorada("Python")