lista = ['a','b','c']

for indice,item in enumerate(lista): 
    print(indice,item)
    
mis_tuplas = list(enumerate(lista))
print(mis_tuplas)

#Ejercicio 1
#Imprime en pantalla frases como la siguiente:'{nombre} se encuentra en el índice {indice}'
#Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante 

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')
    
#Ejercicio 2 
#Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

lista_indices = list(enumerate("Python"))
print(lista_indices)

#Ejercicio 3 
#Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)