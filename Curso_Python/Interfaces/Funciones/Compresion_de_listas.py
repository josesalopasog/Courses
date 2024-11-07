palabra = 'python'

lista = [letra for letra in palabra]
lista_nums = [n for n in range(0,21,2)]
lista_nums_2 = [n/2 for n in range(0,21,2)]
lista_nums_3 = [n if n * 2 > 10 else 'no'for n in range(0,21,2)]

print(lista)
print(lista_nums)
print(lista_nums_2)
print(lista_nums_3)

#Ejemplo 2

pies = [10,20,30,40,50]
metros = [p*3.281 for p in pies]

print(metros)

#Ejercicios 1
#Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]

print(valores_cuadrado)

#Ejercicio 2
valores_pares = [num if num % 2 == 0 else 0 for num in valores]
for n in valores_pares:
    valores_pares.remove(0)
print(valores_pares)

#Ejercicio 3 

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [((t)-32)*5/9 for t in temperatura_fahrenheit]

print(grados_celsius)