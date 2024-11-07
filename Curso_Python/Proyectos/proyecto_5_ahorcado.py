from random import * 
from os import system

def pedir_letras():
        letra = ' '
        validacion = False
        while validacion == False:
            letra = input("Escribe una letra o adivina la palabra: ").lower()
            if letra.isalpha() == True:
                lista_letras = list(letra)
                break
            else:
                print("Escribe un valor correcto")
        return lista_letras       
                
def palabra_oculta(palabra):
    palabra_oculta = []
    for i in palabra:
        palabra_oculta.append('_')

    return palabra_oculta 

def valor_en_lista(lista1, lista2):
    for valor in lista1:
        if valor in lista2:
            return True
    return False

palabra = choice(["amor", "amigo", "casa", "perro", "gato", "coche",
    "arbol", "flor", "libro", "silla", "mesa", "ventana",
    "puerta", "camino", "ciudad", "pueblo", "río", "mar",
    "sol", "luna", "estrella", "cielo", "nube", "montaña",
    "valle", "bosque", "campo", "granja", "parque", "jardin",
    "escuela", "colegio", "universidad", "trabajo", "oficina",
    "tienda", "mercado", "supermercado", "hospital", "clinica",
    "iglesia", "templo", "museo", "teatro", "cine", "restaurante",
    "hotel", "bar", "cafe", "plaza", "calle", "avenida", "camino",
    "carretera", "puente", "tunnel", "playa", "costa", "isla",
    "desierto", "selva", "ciudad", "pueblo", "aldea", "campo",])

lista_palabra = list(palabra)
lista_palabra_oculta = palabra_oculta(lista_palabra)
vidas = 8 
letras_usadas = []  
print("¡Juguemos al ahorcado!")
print(f"\nAdivina la palabra: {lista_palabra_oculta}\n-Tienes Vidas: {vidas}\n")

while (vidas != 0):
    while ((lista_palabra_oculta != lista_palabra)):
        palabra_guess = pedir_letras() 
        system('cls')
        
        val_1 = (palabra_guess == lista_palabra)
        val_2 = (lista_palabra_oculta == lista_palabra)
        
        if val_1 or val_2:
            print(f" ¡Felicidades adivinaste la palabra! \n {lista_palabra}")
            break
        elif vidas == 0:
            break
        else: 
            posicion = 0
            if valor_en_lista(palabra_guess, lista_palabra) == True:
                letras_usadas.append(palabra_guess)
                print(f"\n¡Muy bien! Esa letra esta en la palabra. \n Estas son las letras que has usado {letras_usadas} ")
            else:
                letras_usadas.append(palabra_guess)
                vidas -=1
                print(f"\n¡Lo siento! Esa letra no esta en la palabra. \n Estas son las letras que has usado {letras_usadas} ")
        
            for i in palabra_guess:
                for j in lista_palabra:
                    if i == j:
                        lista_palabra_oculta[posicion] = i
                        posicion +=1
                    else:
                        posicion +=1
        print(f"\nPalabra a adivinar: {lista_palabra_oculta}\n- Vidas: {vidas}\n")
    else:
        print(f" ¡Felicidades adivinaste la palabra! \n {lista_palabra}")
        break
else:
    print("Se te acabaron las vidas. Intentalo en otra ocasión")

