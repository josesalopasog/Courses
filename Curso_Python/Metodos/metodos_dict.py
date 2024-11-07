diccionario = {
    'nombre' : "José",
    'apellido' : "Salopaso",
    'edad' : 26
}

claves = diccionario.keys() # keys(): nos sirve para ver los keys de un conjunto. Nos devuleve un objeto dict_item
traer = diccionario.get('edad') #get(): trae el valor de una key
items = diccionario.items() # items(): nos trae los valores dentro de las keys.

print(claves)
print(traer)
print(items)