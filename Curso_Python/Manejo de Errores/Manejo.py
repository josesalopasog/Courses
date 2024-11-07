def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(f"Gracias por sumar {n1 + n2}")
    
try:
    suma()
except:
    print("Algo no salio bien")
else: 
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")
    
#Funcion para solicitar un opción 
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

def cociente(num1,num2):
    
    try:    
        print(num1/num2)
    except TypeError: 
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
 
def abrir_archivo(nombre_archivo):
    
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError: 
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
               
cociente(2,0)