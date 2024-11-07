lista = ["Jose Salopaso", "Ingeniero",True,25] #las listas se pueden modificar
tupla = ("Jose Salopaso", "Ingeniero:",True,25) #las duplas no se pueden modificar 
mi_set = set([1,2,3,4,5]) #Los Set son inmutables
otro_set = {1,2,3}

conjunto = {"Jose Salopaso", "Ingeniero:",True,25} 

# Reglas del conjunto:
# -Los conjuntos se recorren con un bucle 
# -No permite repetir variables
# -No accede al elemento. Ejemplo: conjunto{1}

diccionario = {
    'nombre' : "Jose Salopaso",   # key : value 
    'cargo' : "Ingeniero",        # clave : valor
    'aplica' : True,              # siempre se pone una coma por cada elemento
    'edad' : 25,
}

print(f"Usuario1: {lista[0]}")
print(f"Edad:{lista[2]}")

lista[0] = "Juan Diego" #tupla[0] = "Juan Diego" no sirve

print(f"Usuario 2: {lista[0]}")
print(diccionario["edad"]) # de esta manera si se puede acceder al elemento dentro del conjunto

s3 = mi_set.union(otro_set)
s3.add(6)
s3.remove(1)
print(s3)