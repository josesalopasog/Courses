class Pajaro: 
    
    alas = True #Estos son atributos de clase, son los atributos que tendran todos los objetos
    
    def __init__(self,color,especie): #Init es el constructor de la clase , que sirve para ver que atributos necesita el objeto para que se pueda construir. | Self es la instancia del objeto
        self.color = color # self.color es el atributo que requiere un parametro
        self.especie = especie

    def piar (self):
        print("pio, mi color es {}".format(self.color))
        
    def volar(self,metros):
        print(f"El pajaro ha volado {metros}")
        
piolin = Pajaro('amarillo','canario')

piolin.piar()
piolin.volar(50)

#Ejercicio 1 
#Crea una clase Perro. Dicho perro debe poder ladrar. 
#Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".

class Perro:
    def ladrar(self):
        print("Guau!")
        
mi_perro = Perro()

mi_perro.ladrar()

#Ejercicio 2 
#Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").
#Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.

class Mago: 
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
        
merlin = Mago()
merlin.lanzar_hechizo()        

#Ejercicio 3
#Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje
#"La alarma ha sido pospuesta {cantidad_minutos} minutos"

class Alarma: 
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

