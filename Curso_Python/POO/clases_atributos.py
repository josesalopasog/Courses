class Pajaro: 
    
    alas = True #Estos son atributos de clase, son los atributos que tendran todos los objetos
    
    def __init__(self,color,especie): #Init es el constructor de la clase , que sirve para ver que atributos necesita el objeto para que se pueda construir. | Self es la instancia del objeto
        self.color = color # self.color es el atributo que requiere un parametro
        self.especie = especie

mi_pajaro = Pajaro('negro','Tucan') # Aqui se asignan los atributos de instancia.'mi_pajaro' es la instancia

print(mi_pajaro.especie) #El .color es el atributo del objeto creado mi_pajaro
print(mi_pajaro.alas)

#Ejercicio 1 
# Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.
# Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.

class Casa:
    
    def __init__(self,color,cantidad_pisos):
        self.color = color 
        self.cantidad_pisos = cantidad_pisos
        
casa_blanca = Casa('blanco',4)

print(casa_blanca.color)

#Ejercicio 2 
# Crea una clase llamada Cubo, y asígnale el atributo de clase: caras = 6 y el atributo de instancia: color
# Crea una instancia cubo_rojo, de dicho color.

class Cubo:
    caras = 6
    def __init__(self,color):
        self.color = color

cubo_rojo = Cubo('rojo')

#Ejercicio 3
#Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase: real = False
#Crea una instancia llamada harry_potter con los siguientes atributos de instancia: especie = "Humano" magico = True edad = 17

class Personaje: 
    real = False
    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = 17
        
harry_potter = Personaje("Humano",True,17)