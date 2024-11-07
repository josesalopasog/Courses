def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(hasta):
    contador = 0
    for num in range(2, hasta + 1):
        if es_primo(num):
            print(num, end='-')
            contador += 1
    print()  # Para nueva línea después de imprimir todos los primos
    return contador

#-------------------
def contar_primos_1(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
            else:
                primos.append(iteracion)
                iteracion += 2
    print(primos)
    return len(primos)

# Ejemplo de uso:
numero = 100
cantidad_primos = contar_primos(numero)
print(f"Cantidad de números primos entre 0 y {numero}: {cantidad_primos}")
#print(contar_primos_1(7))