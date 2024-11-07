from pathlib import Path
import os

ruta = 'C:\\Users\\Usuario\\Desktop\\Curso Python\\In and Output\\pruebas.txt'
elemento_base = os.path.basename(ruta)
elemento_directorio = os.path.dirname(ruta)
elemento = os.path.split(ruta)

print(f"Este es el elemento base: {elemento_base}")
print(f"Este es el directorio: {elemento_directorio}")
print(f"Este es tu elemento: {elemento}")


ruta1 = os.getcwd() # os.getcwd para traer el directorio 
ruta2 = os.chdir('C:\\Users\\Usuario\\Desktop\\Python 2') #or.chdir para cambiar de directorio
# ruta3 = os.makedirs('C:\\Users\\Usuario\\Desktop\\Python 2\\Otra') os.makedirs sirve para crear carpetas
# os.rmdir('C:\\Users\\Usuario\\Desktop\\Python 2\\Otra') os.rmdir Sirve para eleminar carpetas 

print(ruta1)

archivo = open('Otro_Archivo.txt')
print(archivo.read())
archivo.close()

carpeta = Path('C:/Users/Usuario/Desktop/Python 2') #Para abrir archivos en cualquier sistema operativo
archivo_2 = carpeta / 'Otro_Archivo.txt'

mi_archivo = open(archivo_2)
print(mi_archivo.read())
archivo.close()
