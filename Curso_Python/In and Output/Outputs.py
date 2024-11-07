archivo = open('prueba1.txt','w') #Si se escribe con 'w' el archivo se regenera si se escribe con 'a' comienza a escribir desde la ultima linea
archivo.write("Nuevo texto\n")

lista = ['hola','mundo','aqui','estoy']

for i in lista:
    archivo.writelines(i + '\n')

archivo.close()

#Ejercicio 1
# Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.

archivo = open('prueba1.txt','a')
archivo.write("Nuevo inicio de sesión")
archivo.close()

archivo = open('prueba1.txt','r')
print(archivo.read())
archivo.close()

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

#Ejercicio 2 
# Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" .
# Inserta un tabulador entre cada elemento de la lista para separarlos.

archivo = open('registro.txt','a')
for i in registro_ultima_sesion:
    archivo.writelines(i + '\t')
archivo.close()

archivo = open('registro.txt','r')
print(archivo.read())
archivo.close()
