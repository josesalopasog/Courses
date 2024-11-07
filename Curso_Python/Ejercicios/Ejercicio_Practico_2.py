#Ejercicio
#Escribe una función(Puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como párametro,
#y que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.

def juego_palabra (palabra):
    lista_sin_duplicados = []
    palabra_separada = list(palabra)
    for n in palabra_separada:
        if n not in lista_sin_duplicados:
            lista_sin_duplicados.append(n)
            lista_sin_duplicados.sort()
        elif n in lista_sin_duplicados:
            pass
    return lista_sin_duplicados
        
def pedir_palabra():
    palabra = '0'
    validacion = palabra.isalpha()
    while(validacion == False):
        palabra = input("Escribe una palabra: ")
        if palabra.isalpha():
            palabra = palabra.lower()
            return palabra
        else:
            pass

#-----------------------------------
#Solución Con Sets ya que por defecto no puede repetir valores
def letras_unicas(palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()
    
    return mi_lista
palabra_1 = pedir_palabra() 
print(letras_unicas(palabra_1))
#----------------------------------- 
    
palabra_2 = pedir_palabra()
print(juego_palabra(palabra_2))