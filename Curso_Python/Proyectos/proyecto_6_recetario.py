from pathlib import Path
import os

path_base = Path('C:\\Users\\Usuario\\Desktop\\Python 2\\Recetas')
#------------------------
#Funciones       
def traer_categoria():
    categoria = [item for item in path_base.iterdir() if item.is_dir()]
    return categoria       
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
def mostrar_categoria():
    os.system('cls') 
    print("Estas son las categorias existentes: ")
    #--Seleccionar Categoria de la recetas--
    n=0
    lista_cat = []
    for categoria in traer_categoria():
        lista_cat.append(categoria) 
        n += 1 
        print(f"\t{n}. {categoria.relative_to(Path(path_base))}")
    return n,lista_cat
#------------------------
#Inicio del codigo
os.system('cls')      
print(f"Bienvenido/a, las recetas estan en:{path_base}\n")
menu_option = 0
#------------------------
while menu_option != 6:
    print("""Escoge una de las siguientes opciones:\n\n\t1. Leer una receta\n\t2. Agregar una receta\n\t3. Eliminar una receta\n\t4. Agregar una categoria\n\t5. Eliminar una categoria\n\t6. Para salir del menu\n""")
    menu_option = select_option(6)
    match menu_option:
        case 1: #Primera opción: Leer las recetas existentes 
            n,lista_cat = mostrar_categoria()
            n_cat = select_option(n) - 1      #Categoria escogida
            path_cat = Path(lista_cat[n_cat]) #Path de la categoria escogida

            #--Seleccionar Receta que desea leer--
            os.system('cls')
            n=0
            lista_recetas = []
            print("Estas son las recetas existentes:")  
            for receta in path_cat.glob('**/*.txt'):
                lista_recetas.append(receta)
                n += 1
                print(f"\t{n}.{receta.stem}")
            if lista_recetas == []:
                print("\n¡Lo siento, no hay recetas para mostrar!\n")
                print("\n ¿Que quieres hacer ahora? \n\t1. Volver al menu principal\n\t2. Salir del recetario\n")
                menu_option = select_option(2)
                if menu_option == 1:
                    os.system('cls')
                    continue
                elif menu_option ==2:
                    print("¡Hasta la proxima!\n")
                    break   
            else:      
                n_receta = select_option(n) - 1   #Receta escogida 
                leer_receta = Path(lista_recetas[n_receta]).read_text()
                os.system('cls')
                print(f"Esta es tu receta: \n {leer_receta}")
                #------------------------
                print("\n ¿Que quieres hacer ahora? \n\t1. Volver al menu principal\n\t2. Salir del recetario\n")
                menu_option = select_option(2)
                if menu_option == 1:
                    os.system('cls')
                    continue
                elif menu_option ==2:
                    print("¡Hasta la proxima!\n")
                    break
        case 2: #Segunda opción: Agregar una receta nueva              
            print("A cual categoria quieres agregar la receta: ")
            #--Seleccionar Categoria de la recetas--
            n,lista_cat = mostrar_categoria()
            n_cat = select_option(n) - 1      #Categoria escogida
            path_cat = Path(lista_cat[n_cat]) #Path de la categoria escogida    
            
            name_new_file = str(input("Escribe el nombre de la receta> "))+'.txt'
            path_new_file = os.path.join(path_cat,name_new_file)
            file_text = str(input("Escribe el contenido de la receta> "))
            with open(path_new_file, "w") as file:   #With sirve para abrir y cerrar el archivo sin codigo adicional. Se cierra automaticamente 
                file.write(file_text)
            print("\n ¿Que quieres hacer ahora? \n\t1. Volver al menu principal\n\t2. Salir del recetario\n")
            menu_option = select_option(2)
            if menu_option == 1:
                os.system('cls')
                continue
            elif menu_option ==2:
                print("¡Hasta la proxima!\n")
                break
        case 3: #Tercera Opción: Eliminar una receta
            os.system('cls') 
            print("Escoge de que categoria quieres eliminar la receta: ")
            #--Seleccionar Categoria de la recetas--
            n=0
            lista_cat = []
            for categoria in traer_categoria():
                lista_cat.append(categoria) 
                n += 1 
                print(f"\t{n}. {categoria.relative_to(Path(path_base))}")

            n_cat = select_option(n) - 1      #Categoria escogida
            path_cat = Path(lista_cat[n_cat]) #Path de la categoria escogida

            #--Seleccionar Receta que desea leer--
            os.system('cls')
            print("Estas son las recetas existentes, selecciona la opción que quieres eliminar: ")
            n=0
            lista_recetas = []
            for receta in path_cat.glob('**/*.txt'):
                lista_recetas.append(receta)
                n += 1
                print(f"\t{n}.{receta.stem}")
            if lista_recetas == []:
                print("\n¡Lo siento, no hay recetas para mostrar!\n")
                print("\n ¿Que quieres hacer ahora? \n\t1. Volver al menu principal\n\t2. Salir del recetario\n")
                menu_option = select_option(2)
                if menu_option == 1:
                    os.system('cls')
                    continue
                elif menu_option ==2:
                    print("¡Hasta la proxima!\n")
                    break   
            else:             
                n_receta = select_option(n) - 1   #Receta escogida 
                os.remove(lista_recetas[n_receta])
                os.system('cls')
                print("¡La receta a sido eliminada con exito!")
                #------------------------
                print("\n ¿Que quieres hacer ahora? \n\t1. Volver al menu principal\n\t2. Salir del recetario\n")
                menu_option = select_option(2)
                if menu_option == 1:
                    os.system('cls')
                    continue
                elif menu_option ==2:
                    print("¡Hasta la proxima!\n")
                    break
        case 4: #Cuarta opción: Crear una categoria
            cat_name = str(input("Escribe el nombre de la categoria que quieres crear> ")) 
            path_new_cat = f'{path_base}\{cat_name}'
            new_cat = os.makedirs(Path(path_new_cat))
            print(f"¡La categoria '{cat_name}' a sido creada con exito!")
            print("\n ¿Que quieres hacer ahora? \n\t1. Volver al menu principal\n\t2. Salir del recetario\n")
            menu_option = select_option(2)
            if menu_option == 1:
                os.system('cls')
                continue
            elif menu_option ==2:
                print("¡Hasta la proxima!\n")
                break
        case 5: #Quinta opción: Eliminar una categoria
            n,lista_cat = mostrar_categoria()
            n_cat = select_option(n) - 1      #Categoria escogida
            path_cat = Path(lista_cat[n_cat]) #Path de la categoria escogida 
            for receta in path_cat.glob('**/*.txt'):
                os.remove(receta)
            os.system('cls')
            print(f"La categoria {path_cat.relative_to(path_base)} a sido eliminada con exito.")
            os.rmdir(path_cat) 

            print("\n ¿Que quieres hacer ahora? \n\t1. Volver al menu principal\n\t2. Salir del recetario\n")
            menu_option = select_option(2)
            if menu_option == 1:
                os.system('cls')
                continue
            elif menu_option ==2:
                print("¡Hasta la proxima!\n")
                break            
        case 6: #Sexta opción: Salir del Menu
            print("¡Hasta la proxima!\n")
            break


