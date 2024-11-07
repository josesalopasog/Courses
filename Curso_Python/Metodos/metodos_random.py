from random import *

#Metodo randint 
aleatorio_1 = randint(1,50)
print(aleatorio_1)

#Metodo uniform
aleatorio_2 = round(uniform(1,5),1)
print(aleatorio_2)

#Metodo Random
aleatorio_3 =random()
print((aleatorio_3))

#Metodo Choice
colores = ['azul','rojo','verde','amarallo']
aleatorio_4 = choice(colores)
print(aleatorio_4)

#Metodo Shuffle
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)


