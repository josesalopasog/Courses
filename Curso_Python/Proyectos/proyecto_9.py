import os 
import re
import time
import math
from pathlib import *
from datetime import datetime 

path_principal = Path('C:\\Users\\Usuario\\Desktop\\Curso Python\\Proyectos\\Proyecto Día 9\\Mi_Gran_Directorio')

def ns_search():
    formato = r'N\D{3}-\d{5}'
    lista_archivos = [] 
    i = 0
    cuenta = 0
    print("ARCHIVO   \t NRO.SERIE")
    print("-------   \t ---------")
    for archivo in path_principal.glob('**/*.txt'):
        lista_archivos.append(archivo)
        texto_in_archivo = str(open(lista_archivos[i]).readlines())
        comprobacion = re.findall(formato,texto_in_archivo)
        if comprobacion:
            print(f"{Path(lista_archivos[i]).name}\t{comprobacion}")
            cuenta += 1
            i += 1
        else:
            i += 1
    print(f"\nNúmeros encontrados:{cuenta}")
    
def fecha():
    today = datetime.now()
    return f"{today.day}/{today.month}/{today.year}"

def print_linea(numero):
        print("-"*numero) 

os.system('cls')
print_linea(50)      
print(f"La fecha de búsqueda: {fecha()}\n")      
#ns = ns_input()
inicio = time.time()
ns_search()
final = time.time()
print(f"Duración de la busqueda: {math.ceil(final-inicio)} segundos")
print_linea(50)   

