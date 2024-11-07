#Ejercicio
# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.

def solicita_numeros():
    lista_vacia = []
    number = ''
    validacion = (number != 'Exit')
    while validacion == True:
        number = input("Escribe un numero: ")
        if(number == 'Exit'):
            validacion = False
        elif(number.isnumeric()):
            number = int(number)
            lista_vacia.append(number)
        elif (number.isalpha()):
            pass 
    return tuple(lista_vacia)

def validacion_ceros(*args):
    for i in range(len(args)-1):
        if (args[i] == 0) and (args[i+1] == 0):
            return True
    return False

lista = solicita_numeros()
print(lista)
print(validacion_ceros(lista))

