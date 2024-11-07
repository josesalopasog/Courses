import zipfile
import shutil

#Para comprimir:
#mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')

#mi_zip.write('mi_texto_A.txt')
#mi_zip.write('mi_texto_B.txt')

#mi_zip.close()

#Para descomprimir
#zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')
#zip_abierto.extractall()

#Para comprimir toda una carpeta con shutil: 
#carpeta_origen = 'C:\\Users\\Usuario\\Desktop\\Python 2\\Recetas'
#archivo_destino = 'Todo_Comprimido'
#shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

#Para descomprimir con shutil:
shutil.unpack_archive('Todo_Comprimido.zip','Recetas','zip')