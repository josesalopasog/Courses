def tachar_letra(abecedario, letra_a_tachar):
    tachado = [f"~~{letra}~~" if letra == letra_a_tachar else letra for letra in abecedario]
    return tachado

# Crear la lista del abecedario QWERTY
abecedario_qwerty = list("qwertyuiopasdfghjklzxcvbnm")

# Letra a tachar
letra_a_tachar = 'a'

# Obtener el abecedario con la letra tachada
abecedario_tachado = tachar_letra(abecedario_qwerty, letra_a_tachar)

# Imprimir el resultado
print(" ".join(abecedario_tachado))