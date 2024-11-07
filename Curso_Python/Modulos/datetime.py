from datetime import * 
import datetime

mi_hora = datetime.time(17,35)
print(mi_hora.minute)

mi_dia = datetime.date(2024,8,8)
print(mi_dia.ctime())
print(mi_dia.today())

mi_fecha = datetime.datetime(2025,5,15,22,10,15,2500)

mi_fecha = mi_fecha.replace(month = 11)

print(mi_fecha)

nacimiento = datetime.date(1995,3,5)
defuncion = datetime.date(2095,6,19)

vida = defuncion - nacimiento

print(vida)

despierta = datetime.datetime(2022,10,5,7,30)
duerme = datetime.datetime(2022,10,5,23,45)

vigilia = duerme - despierta

print(vigilia.seconds)

#Ejercicio 1 
#Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999

mi_fecha = datetime.date(1999,2,3)
print(mi_fecha.ctime())

#Ejercicio 2 
#Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.

hoy = datetime.date.today()
print(hoy)

#Ejercicio 3 
#En una variable llamada minutos, almacena únicamente los minutos de la hora actual.

#Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43

minutos = datetime.datetime.now().minute
print(minutos)