texto = input("Escribe un texto: ")
letras = input("Escribe tres letras separadas por un espacio: ")

conjunto_1 = texto.split(" ")
conjunto_2 = letras.split(" ")
texto.lower()

q_1 = texto.count(conjunto_2[0])
q_2 = texto.count(conjunto_2[1])
q_3 = texto.count(conjunto_2[2])

conjunto_3 = texto.split(" ")
conjunto_3.reverse()
texto_invert = " ".join(conjunto_3)

verificacion = "Python" in conjunto_1
dic = {True:"Si",False:"No"}

print(f"""
      Punto 1:
      La cantidad de veces que aparece la primera '{conjunto_2[0]}' es {q_1} veces.
      La cantidad de veces que aparece la primera '{conjunto_2[1]}' es {q_2} veces.
      La cantidad de veces que aparece la primera '{conjunto_2[2]}' es {q_3} veces.
      Punto 2: 
      El texto tiene {len(conjunto_1)} palabras.
      Punto 3:
      El texto inicia con la letra {texto[0]} y termina con la letra {texto[-1]}
      Punto 4:
      El texto invertido es: {texto_invert}
      Punto 5:
      ¿La palabra python se encuentra en el texto? {dic[verificacion]}
      """)
