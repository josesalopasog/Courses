lista_1 = ['Juan','Jose','Carlos','Belen','Fran']
lista_2 = ['a','b','c','d']
lista_3 = [1,2,3,4,5]
lista_4 = [[1,2],[3,4],[5,6]]
mi_valor = 0 
cadena = 'Python'
    
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

dic = {
    'clave1' : 'a',
    'clave2' : 'b',
    'clave3' : 'c'
}

for nombre in lista_1:
    if nombre.startswith('J'):
        print(f"Hola {nombre}") 

for letra in lista_2:
    numero_letra = lista_2.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")  
    
for numero in lista_3:
    mi_valor = mi_valor + numero
    print(mi_valor) 
    
for contar_letras in cadena: 
    print(contar_letras)
    
for a,b in lista_4:
    print(a)
    print(b)
    
for a in dic.items():
    print(a)
    
for a,b in dic.items():
    print(a,b)
    
for num in lista_numeros:
    if num%2 == 0:
        suma_pares = suma_pares + num
    elif num%2 == 1:
        suma_impares = suma_impares + num

print(f"La suma de los pares es: {suma_pares} y la de los impares: {suma_impares}")