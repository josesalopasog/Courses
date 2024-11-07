#Ejercio 
#Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros 
#Si la suma de los 3 numeros es mayor a 15, va a devolver el numero mayor
#Si la suma de los 3 numeros es menor a 10, va a devovler el el numero menor 
#Si la suma de los 3 numeros es un valor entre 10 y 15 (incluidos va a delvor el numero del valor intermedio)

def devolver_distintos(int_1,int_2,int_3):
    lista = [int_1,int_2,int_3]
    lista.sort()
    suma_ints = int_1+int_2+int_3
    if suma_ints > 15:
        return lista[-1]
    elif suma_ints < 10:
        return lista[0]
    elif (suma_ints >= 10) & (suma_ints <= 15):
        return lista[1]

def solicitar_numero():
    num = ' '
    val = num.isnumeric()
    while (val == False):
        num = input("  -Numero: ")
        if num.isnumeric():
            num = int(num)
            return num
        else:
            pass
        
print("Escribe tu primer numero: ")
num_1 = solicitar_numero()

print("Escribe tu segundo numero: ")
num_2 = solicitar_numero()

print("Escribe tu tercer numero: ")
num_3 = solicitar_numero()

resultado = devolver_distintos(num_1,num_2,num_3)
print(resultado)