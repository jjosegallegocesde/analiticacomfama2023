#creando diccionarios en python 
persona={
    'nombre':"Valeria",
    'edad':18,
    'estatura':1.60,
    'yaDesayuno':True,
    'equiposFavoritos':['dim','liverpool','olimpiakos','pique']
}

#creando un diccionario vacio
ciudad={}

#accedamos a un diccionario
print(persona)
print(ciudad)

#acceder a un solo atributo o clave del diccionario
nombre=persona["nombre"]
print(nombre)

print(persona["nombre"])

persona["nombre"]="James rodriguez"
print(persona["nombre"])
print(persona)

persona["saldoCuenta"]=0
print(persona["saldoCuenta"])
print(persona)

#recorriendo un diccionario
for valor in persona.values():
    print(valor)

