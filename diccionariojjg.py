#creando diccionarios en python
persona={
    'nombre':"Juan Jose",
    'edad':33,
    'estatura':1.62,
    'yaDesayuno':True,
    'equiposFavoritos':['nacional','liverpool','olimpiakos','pique']
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

persona["nombre"]="james rodriguez"
print(persona["nombre"])
print(persona)

persona["saldoEnCuenta"]=0
print(persona["saldoEnCuenta"])
print(persona)

#Recorreindo un diccionario
for valor in persona.values():
    print(valor)