def multiplicar(numero1,numero2):
    return numero1*numero2

resultado = multiplicar(5,10)
print(resultado)

#Ejercicio 1 
#Crea una función llamada potencia que tome dos valores numéricos como argumentos. 
# Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:


def potencia(num1,num2):
    return num1 ** num2

r_potencia = potencia(5,2)
print(r_potencia)

#Ejercicio 2 
# Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses),
# y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.
# Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.

def usd_a_eur(num):
    return num*0.9

dolares = 20 
conversion = usd_a_eur(dolares)

print(conversion)

#Ejercicio 3 
#Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, 
# invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas
# Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"
# También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.

def invertir_palabra (string):
    reverse = string[::-1]
    return reverse.upper()

palabra = "Curso"

res_2 = invertir_palabra(palabra)
print(res_2)