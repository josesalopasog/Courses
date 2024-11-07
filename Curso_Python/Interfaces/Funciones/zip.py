nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Mexico'] 

#Ejemplo
combinados = list(zip(nombres,edades,ciudades))

for nombre,edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
print(combinados)

#Ejercicio 1 
# Muestra en pantalla frases como la del siguiente ejemplo:
# "La capital de Alemania es Berlín"

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

ident = list(zip(capitales,paises))

for capitales,paises in ident: 
    print(f"La capital de {paises} es {capitales}")
    
#Ejercicio 2 
#Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.

marcas = ["Adidas","Arturo Calle","Nike"]
productos = ["Zapatos","Camisetas","Pantalones"]

mi_zip = zip(marcas,productos)

#Ejercicio 3 
#Crea el zip con las traducciones los números del 1 al 5 en español, 
#portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

español = ["uno","dos","tres","cuatro","cinco"]
portugues = ["um","dois","três","quatro","cinco"]
ingles = ["one","two","three","four","five"]

numeros = list(zip(español,portugues,ingles))

print(numeros)
