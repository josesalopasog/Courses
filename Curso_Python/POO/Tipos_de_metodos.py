#Metodos de instancia: son metodos que pueden ser llamados: acceden y modifican atributos de un objeto, puede acceder a otros metodos y modificar el estado de la clase
#Metodos de clase: estos metodos no estan asociados a la instancia si no a la clase misma. Son llamados desde la misma clase. 
#Metodos estaticos: No pueden modificar el estado ni de clase ni de la instanacia. 

class Pajaro: 
    
    alas = True #Estos son atributos de clase, son los atributos que tendran todos los objetos
    
    def __init__(self,color,especie): #Init es el constructor de la clase , que sirve para ver que atributos necesita el objeto para que se pueda construir. | Self es la instancia del objeto
        self.color = color # self.color es el atributo que requiere un parametro
        self.especie = especie

    def piar (self):
        print("pio, mi color es {}".format(self.color))
        
    def volar(self,metros):
        print(f"El pajaro ha volado {metros}")
        self.piar()
        
    def pintar_negro(self):
        self.color = 'negro'
        
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False # Si tengo acceso a los atributos de clase
       
    @staticmethod
    def mirar():
        print("El pajaro mira")
        
Pajaro.poner_huevos(3)

piolin = Pajaro('amarillo','canario')
piolin.pintar_negro()
piolin.volar(50)
piolin.alas = False

#Ejercicio 1 
#Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"

class Mascota: 
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

#Ejercicio 2 
# Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. 
# El valor predeterminado del atributo vivo, debe ser False.

class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True

#Ejercicio 3
#Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, 
# que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas

class Personaje:
    
    def __init__(self,cantidad_flechas):
        self.cantidad_flechas = int(cantidad_flechas)
    
    def lanzar_flecha(self):
        flechas = self.cantidad_flechas-1
        print(flechas)
        
arquero = Personaje(50)
arquero.lanzar_flecha()