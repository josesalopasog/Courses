numero = 50
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

#Ejercicio 1

while numero > -1: 
    if numero%5 == 0:
        print(numero)
        numero -= 1
    elif numero%5 != 0:
        numero -= 1
        continue
    
 #Ejercicio 2    
for numero in lista_numeros: 
    if numero > 0:
        print(numero)
    else:
        break