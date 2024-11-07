mi_archivo = open('prueba.txt')
todas = mi_archivo.readlines() #.read() para leer


for i in mi_archivo:
    print("Aqui dice: " + i)

linea = mi_archivo.readline()
print(linea)

linea = mi_archivo.readline()
print(linea.rstrip())

linea = mi_archivo.readline()
print(linea)


mi_archivo.close()
