from random import *

user = input("Hola, como te llamas? \n -Nombre:")
number = randint(1,100)
lifes = 8

print(f"Hola {user}, vamos a jugar un juego")
print("Voy a pensar en un numero del 1 al 100 y tu lo tienes que adivinar, pero solo tienes 8 intentes")
start = str(input("Entonces, ¿Estas listo para jugar?(Si/No) \n -Respuesta:"))
start_low = start.lower()

match start_low:
    case "si":
        while lifes > 0:
            number_guess = int(input("Escribe un numero del 1 al 100: "))
            if number_guess == number:
                print(f"\n\t¡Felicitaciones! El numero que estaba pensado era el {number} muchas gracias por jugar\n")
                break
            elif ((number_guess < 1) | (number_guess > 100)):
                lifes -= 1 
                print(f"\n\tEl numero esta fuera del rango. Te quedan {lifes} intentos\n")
                continue
            elif (number_guess > number) & ((number_guess > 0) & (number_guess < 101)):
                lifes -= 1 
                print(f"\n\tEl numero es menor al que estoy pensando. Te quedan {lifes} intentos\n")
            elif (number_guess < number) & ((number_guess > 0) & (number_guess < 101)):
                lifes -= 1 
                print(f"\n\tEl numero es mayor al que estoy pensando. Te quedan {lifes} intentos\n")
        else:
            print("\n\tNo adivinaste el numero. Intentalo en otra ocasión, muchas gracias por jugar.\n")
    case "no":
        print("Vale, hasta luego!")
    case _:
        print("Escribe una respuesta valida. Hasta luego!")

