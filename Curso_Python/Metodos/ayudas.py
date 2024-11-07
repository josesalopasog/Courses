dic = {'clave1':100,'clave2':500}

a = dic.popitem()
print(a)
print(dic)

#Ejercicio 1 

print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#'))

#Ejercicio 2
#Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando el método insert():
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 

frutas.insert(3,"naranja")
print(frutas)

#Ejercicio 3 
#Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). 
#Almacena dicho resultado en la variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)