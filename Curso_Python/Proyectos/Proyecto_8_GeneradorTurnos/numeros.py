import os

def GeneradorTurnos():
    contador = 0 
    while True:
        contador += 1 
        yield contador

turno_perfumeria = GeneradorTurnos()
turno_farmacia = GeneradorTurnos()
turno_cosmeticos = GeneradorTurnos()

def DecoradorTurnos (area):
    match area:
        case 1:
            os.system('cls')
            print(f"Tu turno es:\n\n\tP-{next(turno_perfumeria)}\n\nEspere para ser atendido")
        case 2:
            os.system('cls')
            print(f"Tu turno es:\n\n\tF-{next(turno_farmacia)}\n\nEspere para ser atendido")
        case 3:
            os.system('cls')
            print(f"Tu turno es:\n\n\tC-{next(turno_cosmeticos)}\n\nEspere para ser atendido")
            
def select_option(n):
    while True:
        try:
            user_input = int(input(f"Selecciona una de las opciones> "))
            # Verificar si el número está en el rango válido
            if 1 <= user_input <= n:
                print(f"\nHas seleccionado la opción {user_input}.\n")
                return user_input
            else:
                print(f"Número inválido. Debe ser un número entre 1 y {n}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")    

      




