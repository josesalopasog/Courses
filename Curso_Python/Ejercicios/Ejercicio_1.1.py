curso = {
    0 : 1.5,
    1 : 2.5,
    2 : 4.0,
    3 : 7.0,
}
dif = {
    0 : int(((curso[1]-curso[0])/curso[0])*100),
    1 : int(((curso[3]-curso[0])/curso[0])*100),
    2 : int(((curso[2]-curso[0])/curso[0])*100),
}

prom_material_1 = int(((5-4)*100)/5)
prom_material_2 = int(((3.5-1.5)*100)/3.5)


print(f"""
      La diferencia procentual entre el curso y curso mas rapido es: {dif[0]}% 
      La diferencia procentual entre el curso y curso mas rapido es: {dif[1]}%
      La diferencia procentual entre el curso y curso mas rapido es: {dif[2]}%
      
      Promedio reducido curso 1: {prom_material_1} %
      Promedio reducido curso 2: {prom_material_2} %
       """)
