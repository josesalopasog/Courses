precios_cafe = [('capuccino',1.5),('expresso',1.2),('moka',1.9)]

def cafe_mas_caro(lista_precios):
    
    precio_mayor = 0
    cafe_caro = ' '
    
    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio 
            cafe_caro = cafe
        else: 
            pass
    return (cafe_caro,precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El cafem mas caro es {cafe} cuyo precio es {precio}")

