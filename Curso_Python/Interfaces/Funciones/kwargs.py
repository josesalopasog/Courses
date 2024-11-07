def suma(**kwargs):
    
    total = 0 
    
    for clave,valor in kwargs.items():
        print(f"{clave}={valor}")
        total += valor
        
    return total

print(suma(x=3,y=5,z=2))

def suma_2(num1,num2,*args,**kwargs):
    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")
    
    for arg in args:
        print(f"arg = {arg}")
        
    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")
 
args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

suma_2(15,50,*args,**kwargs)

#Ejercicio 1 
#Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
def cantidad_atributos(**kwargs):
    cant = 0
    for clave,valor in kwargs.items():
        cant += 1
    return cant
print(cantidad_atributos(**kwargs))

#Ejercicio 2 
#Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). 
# La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    lista = []
    for clave,valor in kwargs.items():
        lista.append(valor)
    return lista

print(lista_atributos(**kwargs))

#Ejercicio 3 
def describir_persona(nombre,**descripcion):
    print(f"Caracteristicas de {nombre}:")
    for clave, valor in descripcion.items():
        print(f"{clave}={valor}")
        
describir_persona("Jose",color_ojos='cafe',color_pelo='negro',color_piel='blanco')
    
        