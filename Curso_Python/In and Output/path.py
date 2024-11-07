from pathlib import Path

base = Path.home()
guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
guia3 = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
guia4 = Path(Path.home(),"Europa")
en_europa = guia3.relative_to(Path("Europa")) #relative_to devuelve un nuevo objeto PATH relacionado con el argumento determinado 
en_esp = guia3.relative_to(Path("Europa","España"))

print(base)
print(guia)
print(guia2)
print(guia.parent.parent)

print(en_europa)
print(en_esp)

for i in Path(guia4).glob('**/*.txt'):
    print(i)


#Ejercicios
ruta_base = Path.home()