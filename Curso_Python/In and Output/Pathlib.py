from pathlib import Path, PureWindowsPath

ruta_ios = Path('C:/Users/Usuario/Desktop/Python 2')
ruta_windows = PureWindowsPath(ruta_ios)
archivo = Path('C:\\Users\\Usuario\\Desktop\\Curso Python\\In and Output\\pruebas.txt')
leer_archivo = archivo.read_text() #Metodo para leer el texto 
nombre_archivo = archivo.name #Metodo para traer el nombre del archivo
sufijo_archivo = archivo.suffix #Metodo para traer el tipo,sufijo o extención del archivo
solo_nombre_archivo = archivo.stem #Metodo para traer el nombre sin el sufijo

print(leer_archivo)
print(nombre_archivo)
print(sufijo_archivo)
print(solo_nombre_archivo)

if not archivo.exists():
    print("Este archivo no existe")
else:
    print(f"El archivo {solo_nombre_archivo} existe")
    
print(ruta_windows)