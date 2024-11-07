monedas = 5
respuesta ='s'
nombre = input("Tu nombre:")



#Ejemplo 1
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1  
else:
    print("Se acabaron las monedas")
    
#Ejemplo 2 
while respuesta == 's':
    respuesta = input("quieres seguir? (s/n)")
else:
    print("Gracias")
    
#Ejemplo 3 Pass

while respuesta == 's':
    pass  #Pass se utiliza para guardar el espacio del while en el codigo

#Ejemplo 4 - Break

for letra in nombre: 
    if letra == 'r':
        break
    print(letra)
    
#Ejemplo 4 - Continue

for letra in nombre: 
    if letra == 'r':
        continue
    print(letra)