#Ejercicio de Calculos 
x = 2 
y = 3
z = 2  

operadores_comparacion = {
    'igual_que' : x==y,         # Los dos signos es comparación "=="
    'distinto_de' : x!=y,
    'es_menor_que' : x < y,
    'es_mayor_que' : x > y,
    'menor_o_igual' : x <= z, 
    'mayor_o_igual' : x >= z
}

credenciales_usuario_1 = {
    'user' : "José Salopaso",
    'password' : "José Salopaso" 
}

print(operadores_comparacion)
print(credenciales_usuario_1['user'] == credenciales_usuario_1['password'])
