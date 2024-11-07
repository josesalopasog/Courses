from numeros import *

print("¡Bievenido/a!")
while True:
    print("Seleccione a que categoria se quiere dirigir: \n\n\t1. Perfumeria\t2. Farmacia\t3.Cosmeticos\n")
    n = select_option(3)
    DecoradorTurnos(n)
    print("\nQue deseas hacer ahora:\n\n\t1. Pedir otro turno\t2. Salir\n")
    o = select_option(2)
    if o == 1:
        os.system('cls')
        continue
    elif o ==2:
        print("Hasta luego") 
        break