#Ejercicio de Calculos 
x = 3 
y = 2
z = 2 
salario = 1100
gastos = 1200

operadores_comparacion = {
    'igual_que' : x==y,        
    'distinto_de' : x!=y,
    'es_menor_que' : x < y,
    'es_mayor_que' : x > y,
    'menor_o_igual' : x <= z, 
    'mayor_o_igual' : x >= z
}

if operadores_comparacion['igual_que'] == True:
    print("Los valores son iguales")
else:
    print("Los valores no son iguales")
    
    
if salario > 500 and salario <1000: 
    if salario - gastos > 0:
        print("Estas regular pero no estas gastando mucho")
    else:
        print("Estas regular y estas gastando mucho")
elif salario > 1000 and salario < 2500:
    if salario - gastos > 0:
        print("Estas mejorando pero no estas gastando mucho")
    else:
        print("Estas mejorando y estas gastando mucho")