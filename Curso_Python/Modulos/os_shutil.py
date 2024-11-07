import os
import shutil 
import send2trash


#Creando el archivo
#archivo = open('curso.txt','w')
#archivo.write('Texto de prueba')
#archivo.close()
#print(os.listdir())

#Moviendo el archivo
#shutil.move('curso.txt', "C:\\Users\\Usuario\\Desktop")

#Mandando archivo a la papelera
#send2trash.send2trash('curso.txt')


ruta = "C:\\Users\\Usuario\\Desktop\\Python 2\\Recetas"

for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son: ")
    for arch in archivo:
        print(f"\t{arch}")
    print('\n')    
