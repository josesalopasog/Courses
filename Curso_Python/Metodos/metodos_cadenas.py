cadena_1 = "jOSEsAloPasO"
print(f"Cadena original {cadena_1}")
# Función DIR
print(f""" Función DIR:
      {dir(cadena_1)}
      """) #Devuelve lista de atributos validos del objeto pasado.

# Metodos MAYUS y MINUS
fix = {
    1 : cadena_1.upper(),     # UPPER - Convierte string en mayusculas.
    2 : cadena_1.lower(),     # LOWER - Convierte strinng en minusculas.
    3 : cadena_1.capitalize() # CAPITALIZE - Convierte primera en mayuscula y el resto en minusculas.
}
print(f"""Metodos MAYUS y MINUS:
      {fix}
      """)

# Metodos para buscar valores
search = cadena_1.find("O") # FIND - Busca un valor y devuelve en la posición en que se encuentra. Devuelve un "-1" si no encuentra un valor.
search2 = cadena_1.index("O") # INDEX - Busca un valor y devuelve en la posición en que se encuentra. Lanza una exepción si no encuentra un valor.
print(f"""Metodo para buscar valores(FIND):
      -En la cadena hay por lo menos: {search} valor igual.
      """)
# Buscar una cadena en otra cadena y devolver cuantas veces se repite. 
count = cadena_1.count("O")
print(f"""Metodo para contar(COUNT): 
      -En la cadena se encontro: {count} valores iguales.
      """)
# Función para contar cuantos caracteres tiene una cadena
lenght = len(cadena_1)
print(f"""Función para contar cuantos caracteres tiene la cadena(LEN):
      - El texto tiene: {lenght} caracteres.
      """)
# Devolver True si un valor es numero o False si no lo es 
number = cadena_1.isnumeric()
print(f"""Metodo para decir si es numerico: 
      ¿El valor es numerico?: {number}
      """) 
# Devolver True si un valor es alfanumero o False si no lo es 
alphanumeric = cadena_1.isalpha()
print(f"""Metodo para decir si es alfa numerico: 
      ¿El valor es alfanumerico? {alphanumeric}
      """)
# Verificar si una cadena empieza con otra cadena escrita, si es así devuelve True si no devuelve False 
start = cadena_1.startswith("jOSE")
print(f"""Metodo para verificar si una cadena empieza con el valor dado (STARTSWITH):
      ¿La cadena empieza con el valor dado? {start}
      """)
# Verificar si una cadena termina con otra cadena escrita, si es así devuelve True si no devuelve False 
end = cadena_1.endswith("Salopaso")
print(f"""Metodo para verificar si una cadena termina con el valor dado (ENDSWITH):
      ¿La cadena termina con el valor dado? {end}
      """)
# Metodo para reemplazar valores de una cadena 
cadena_1 = cadena_1.lower()
replace = cadena_1.replace("jose","nombre_")
print(f"""Metodo para remplazar un valor(REPLACE): 
      -La cadena quedo de la siguiente manera: {replace}
      """)
# Separar cadenas con la cadena que le pasemos
split = replace.split("_")
print(f"""Metodo para separar cadenas(SPLIT):
      {split}""")