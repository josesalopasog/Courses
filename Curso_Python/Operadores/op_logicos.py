
#Operador Logica 'AND' 

operador_AND = {
    't&t' : True & True,   #Devuelve True  (1*1 = 1)  
    't&f' : True & False,  #Devuelve False (1*0 = 0)
    'f&t' : False & True, #Devuelve False (0*1 = 0)
    'f&f' : False & False #Devuelve False (0*0 = 0)  
}
 
#Operador Logica 'OR'
operador_OR = { 
    't|t' : True | True,  #Devuelve True  (1+1 = 1) suma boleana
    't|f' : True | False,  #Devuelve True  (1+0 = 1) 
    'f|t' : False | True,  #Devuelve True  (0+1 = 1)
    'f|f' : False | False  #Devuelve False (0+0 = 0) 
}

#Operador Logica 'NOT' 
operador_NOT = { 
    '!t' : not True,    #Devuelve False  (!1 = 0) 
    '!f' : not False  #Devuelve True   (!0 = 1)
}
  
print(f"""Valores operador AND: 
      {operador_AND}""")
print(f"""Valores operador OR:
      {operador_OR}""")
print(f"""Valores NOT: 
      {operador_NOT}""")
