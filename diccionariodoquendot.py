#creando dicionarios en python

persona= {
    'nombre': "Daniela Oquendo",
    'edad' : 28,
    'estatura' : 1.55,
    'ya desayuno' : True,
    'equiposFavoritoss' : ['nacional', 'liverpool', 'olimpiakos', 'pique']
}

#creando un diccionario vacio
ciudad={}

#accedamos a un diccionario
print(persona)
print(ciudad)

#acceder a un solo atributo o clave del diccionario
nombre=persona["nombre"]
print(nombre)
print(persona ["nombre"])

persona["nombre"]="james rodriguez"
print(persona["nombre"])

persona["saldoEnCuenta"]=0
print(persona["saldoEnCuenta"])
print (persona)

#recorriendo un diccionario
for valor in persona.values():
    print(valor)