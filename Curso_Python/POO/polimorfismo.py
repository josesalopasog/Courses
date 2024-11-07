class Vaca: 
    def __init__(self,nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + "Dice Muuu")
        
class Oveja: 
    def __init__(self,nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + "dice beeee")
        
vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

animales = [vaca1,oveja1]

for animal in animales:
    animal.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)

#Ejercicio 1 
#La función incorporada en Python len() tiene un comportamiento polimórfico,
# ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), 
# devolviendo la cantidad de items o caracteres que lo componen.

#Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) 
# para cada uno de ellos su longitud con la función len().

palabra = "polimorfismo"
personajes = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

objetos = [palabra,personajes,tupla]

for i in objetos:
    print(len(i))
    
#Ejercicio 2 
#Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.

#Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. 
#Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
mago1= Mago()
arquero1 = Arquero()
samurai1 = Samurai()

personajes = [arquero1,mago1,samurai1]

for i in personajes: 
    i.atacar()
    
#Ejercicio 3 
#Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.

#Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), 
# y ejecutar su método defender() independientemente de qué tipo de personaje se trate.

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")
        
def personaje_defender(personajes):
    personajes.defender()