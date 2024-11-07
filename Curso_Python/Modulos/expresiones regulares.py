#Caracteres especiales
#Car   Descripción              Ejemplo 
#\d    Digito Numérico          v\d.\d\d
#\w    Caracter alfanumerico    \w\w\w-\w\w
#\s    Espacio en blanco        numero\s\d\d
#\D    No numérico              \D\D\D\D
#\W    No alfanuméroco          \W\W\W
#\S    No espacio blanco        \S\S\S

#Cuantificadores
#Car   Descripción              Ejemplo 
# +    1 o más veces            código_\d-\d+
#{n}   se repite n veces        \d-\d{4}
#{m,m} se repite de n a m veces \w{3,5} 
#{n,}  desde n hacia arriba     -\d{4,}-
# *    0 ó más veces            \w\s*\w
# ?    1 ó ninguna              casas?

import re
 
texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

patron = 'ayuda'

busqueda = re.search(patron,texto)
busqueda2 = re.findall(patron,texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())
    
print(busqueda2)

texto2 = "llama al 564-525-6588 ya mismo"
patron2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado2 = re.search(patron2, texto2)
print(resultado2.group())
print(resultado2.group(2))

#Ejemplo 1

clave = input("Clave: ")
patron = r'\D{1}\w{7}'
chequear = re.search(patron,clave)

print(chequear)

#Ejemplo 2 

texto = "No atendemos los lunes en la tarde"
buscar = re.search(r'lunes|jueves',texto)
buscar2 = re.search(r'....demos..',texto)
buscar3 = re.search(r'^\D',texto)
buscar4 = re.search(r'\D$',texto)
buscar5 = re.findall(r'[^\s]+',texto)

print(buscar)
print(buscar2)
print(buscar3)
print(buscar4)
print(buscar5)

#Ejercicio 1 
#Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email dado como argumento contiene "@" 
#(entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" 
# para el caso de un usuario de Brasil).

#Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados, 
# debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.

def verificar_email(email):
    patron = r'\S+@\S+\.com\S?' #Para encontrar puntos en la cadena poner \. 
    validacion = re.findall(patron,email)
    if validacion:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")
        
email = 'usuario@hostcom'

verificar_email(email)
    
#Ejercicio 2 
#Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". Si se encuentra el patrón, 
#la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", debe informarle al usuario "No has saludado" imprimiendo 
# el mensaje en pantalla.
def verificar_saludo(frase):
    validacion = re.search(r'Hola',frase)
    if validacion:
        print("Ok")
    else: 
        print("No has saludado")
        
verificar_saludo("como estas")

#Ejercicio 3
# El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). 
# Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. Si el patrón es correcto, mostrar 
# al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".

def verificar_cp(cp):
    verificacion = re.findall(r'\w{2}\d{4}',cp)
    if verificacion:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
        
verificar_cp("X11234")