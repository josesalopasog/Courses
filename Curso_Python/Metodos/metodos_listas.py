#Crear una lista con la función lista()
lista = list(["José Salopaso","H",25,"0+",1998])
lista_numerica = [4,3,2,5,7,8,9,6,True,False]

print(f"""Lista original: {lista}
      """)

#Devolver cantidad de elementos en una lista
list_lenght = len(lista)

#Agregar elementos a una lista 
lista.append("Julio")                   #APPEND agrega el elemento en una posición disponible
lista.insert(5,13)                      #INSERT agrega el elemento en una posición especifica
lista.extend(["Bogotá","Colombia"])     #EXTEND agrega los elementos de una lista a la lista original

print(f"""
      - Cantidad de elementos en la lista con la función LEN: {list_lenght}
      - Agregando un elemento nuevo a la lista original con el metodo APPEND, INSERT y EXTEND: {lista}
      """)

#Eliminando elementos de la lista 
lista.pop(-1) #Por su indice - con "-n" se elimina el valor dado de atras hacia adelante
lista.remove("H")

print(f"""
      - Eliminando valores de la lista con el petodo POP y REMOVE: {lista}
      """)
lista.clear()
print(f"""- Borrando todos los valores de la lista con CLEAR: {lista}
      """)

#Ordenar valores de una lista numerica
print(f"Lista Original: {lista_numerica}")

lista_numerica.reverse() #Reordena la lista del ultimo valor al primero
print(f"""
      - Reordenando los elementos del ultimo al primero con el metodo REVERSE: {lista_numerica}""")
lista_numerica.sort() #Ascendente 
print(f""" 
      - Ordenada de manera ascendente con el metodo SORT: {lista_numerica}""")
lista_numerica.sort(reverse=True) #Descendete
print(f"""
      - Ordenada de manera descendente con el metodo SORT y el parametro REVERSE: {lista_numerica}
      """)