import os 


#Class Persona con atributos nombre y apellidos 
class Persona:
    def __init__(self,nombre,apellidos):
        self.nombre = nombre
        self.apellidos = apellidos  
#Class Cliente hereda los atributos de persona y otros atributos como: numero de cuenta y balance 
class Cliente(Persona):
    def __init__(self, nombre, apellidos,numero_cuenta,balance=0):
        super().__init__(nombre, apellidos)
        self.numero_cuenta = numero_cuenta
        self.balance = balance     
    def __str__(self) -> str:
        return f"\n Estos son sus datos:\n\tNombre del usuario: {self.nombre} {self.apellidos}\n\tNumero de cuenta: {self.numero_cuenta}\n\tEste es tu balance: ${self.balance}"
    def Depositar(self):
        while True:
            try:
                deposit_ipunt = int(input("Ingrese la cantidad de dinero que quiere depositar>"))
                if 5000 <= deposit_ipunt <= 2000000:
                    self.balance += deposit_ipunt
                    return f"Su nuevo balance es ${self.balance}"
                elif deposit_ipunt < 5000:
                    print("El valor minimo que usted puede depositar es $5000.Ingrese otro valor.")
                elif deposit_ipunt > 2000000:
                    print("El valor maximo que usted puede depositar es $2000000.Ingrese otro valor.")
            except ValueError:
                print("Ingrese un numero entero")          
    def Retirar(self):
        while True:
            try:
                withdrawal_input = int(input("Ingrese la cantidad de dinero que quiere depositar>"))
                if 5000 <= withdrawal_input <= self.balance:
                    self.balance -= withdrawal_input
                    return f"Usted a retirado: ${withdrawal_input} Su nuevo balance es ${self.balance}"
                elif withdrawal_input < 5000:
                    print(f"El valor minimo que usted puede retirar es $5000.Ingrese otro valor.")
                elif withdrawal_input > self.balance:
                    print(f"El valor maximo que usted puede retirar es ${self.balance}.Ingrese otro valor.")
            except ValueError:
                print("Ingrese un numero entero")

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

#Base de los clientes 
cliente1 = Cliente("Jose","Salopaso",51300535) #Instanciando el objeto
os.system('cls')
print("¡Bienvenido/a!")

#Operación
option = 0
while option !=3:
    print(str(cliente1))
    print("\n Seleccione una de las opciones:\n\n\t1. Depositar\t2. Retirar\t3. Salir\n")
    option = select_option(3)
    match option:
        case 1:
            os.system('cls')
            print(cliente1.Depositar())
            continue
        case 2:
            if cliente1.balance !=0:
                os.system('cls')
                print(cliente1.Retirar())
                continue
            else:
                os.system('cls')
                print(f"Ustede tiene ${cliente1.balance} en su cuenta, favor deposite primero.")
                continue
        case 3: 
            os.system('cls')
            print("\n\t¡Hasta la proxima!\n")
            break

