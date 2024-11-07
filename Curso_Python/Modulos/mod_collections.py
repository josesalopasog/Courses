from collections import *

#Counters:
numeros = [8,5,5,9,6,4,1,2,8,9,7,5,6,4,4,5]
serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3])
frase = "al pan pan y al vino vino y pa tu c mi pepino"

print(Counter(numeros))
print(Counter(frase.split()))
print(serie.most_common(1))
print(list(serie))

#defaultdict
mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)

#namedtuple
Persona = namedtuple('Persona', ['nombre','altura','peso'])
ariel = Persona('Ariel',1.76,79)
print(ariel.altura)


#Ejercicio 1 
#Aplica un Counter (contador) sobre la lista de números entregada a continuación, y almacénalo en una variable llamada contador

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)

#Ejercicio 2 
#Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave buscada, se cargue con el string "Valor no hallado".
#Carga el diccionario, al menos, con el siguiente par de datos:
#palabra clave = edad
#valor = 44
#Utiliza el método defaultdict del módulo Collections.

mi_diccionario = defaultdict(lambda: "Valor no hallado")
mi_diccionario['edad'] = 44

#Ejercicio 3
#Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal que permite insertar y eliminar elementos por ambos extremos.
#Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa una deque a partir del módulo collections. Los elementos iniciales de la lista se brindan a continuación.

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

#La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre lista_ciudades.