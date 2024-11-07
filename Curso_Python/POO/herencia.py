class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")
        
    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    
    def __init__(self, edad, color,altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
    
    def hablar(self):
        print("pio")
        
    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")

piolin = Pajaro(2,'negro',50)
piolin.nacer() # Hereda el metodo nacer de la clase Animal 
piolin.hablar()
piolin.volar(100)
mi_animal = Animal(3,'naranja')

print (piolin.color)


















#Ejercicio 1 
# Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. 
# Crea otra clase, Alumno, que herede de la primera estos atributos.

class Persona: #Clase 
    #Atributos de instanacia 
    def __init__(self,nombre,edad):
        #Instancia = Atributo
        self.nombre = nombre 
        self.edad = edad 
        
class Alumno(Persona): #Clase que herado los atributos de instancia de Persona
    pass

#Ejercicio 2 
# Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. 
# Crea otra clase, Perro, que herede de la primera sus atributos.

class Mascota: 
    def __init__(self,edad,nombre,cantidad_patas): #Definir que la clase mascota tiene los atributos de instancia 
        #Instancia = Atributo 
        self.edad = edad 
        self.nombre = nombre 
        self.cantidad_patas = cantidad_patas 

class Perro(Mascota):
    pass 

#Ejercicio 3 
# Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass). 
# Crea una clase llamada Automovil que herede estos métodos de Vehiculo.

class Vehiculo: 
    def acelerar(self):
        pass
    
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass

