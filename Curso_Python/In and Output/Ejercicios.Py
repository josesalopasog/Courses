#Ejercicio 1 
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
def abrir_leer(nommbre_archivo):
    archivo = open(nommbre_archivo,'r')
    read = archivo.read()
    return read
#Ejercicio 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
def sobrescribir(nombre_archivo):
    archivo = open(nombre_archivo,'w')
    archivo.write("contenido eliminado")
#Ejercicio 3 
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, 
# y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.  
def registro_error(nombre_archivo):
    archivo = open(nombre_archivo,'a')
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()