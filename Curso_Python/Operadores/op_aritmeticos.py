x = 6
y = 3

operadores_aritmeticos = {
    'suma' : x+y,          #suma(+)
    'resta' : x-y,         #resta(-)
    'producto' : x*y,      #producto(*)
    'división' : x/y,      #división(/) - Siempre devuelve un float 
    'exponente' : x**y,    #exponente(^)
    'división_baja' : x//y, #división que devuelve solo el entero redondeado hacia abajo
    'modulo' : x%y         #Devuelve el resto de la división
}

print(operadores_aritmeticos)
print(type(operadores_aritmeticos['división'])) #type() identifica que tipo de dato es la variable